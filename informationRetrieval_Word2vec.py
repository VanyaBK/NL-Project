from util import *

# Add your import statements here
import numpy as np
from numpy import dot
from numpy.linalg import norm
from gensim.models import Word2Vec
from gensim.models import KeyedVectors


class InformationRetrieval():

    def __init__(self):
        self.index = {}

    def buildIndex(self, docs, docIDs):
        """
        Builds the document index in terms of the document
        IDs and stores it in the 'index' class variable
        Parameters
        ----------
        arg1 : list
            A list of lists of lists where each sub-list is
            a document and each sub-sub-list is a sentence of the document
        arg2 : list
            A list of integers denoting IDs of the documents
        Returns
        -------
        None
        """
        doc_vector = {}
        word_doc_count = {}
        
        for i,document in enumerate(docs):
            doc_vector[docIDs[i]] = {}
			

        for i,documents in enumerate(docs):
            sentence_list = []
            for sentence in documents:
                word_list = []
                for words in sentence:
                    word_list.append(words)
                    word_doc_count[words] = 0
                sentence_list.append(word_list)
            doc_vector[docIDs[i]] = sentence_list
        
        term_freq = {}
		
		
        for i,documents in enumerate(docs):
            term_freq[docIDs[i]] = {}
			
		
        for i,documents in enumerate(docs):
            sentence_list = doc_vector[docIDs[i]]
            sentence_list = [item for sublist in sentence_list for item in sublist]
            for word in sentence_list:
                term_freq[docIDs[i]][word] = sentence_list.count(word)
            sentence_list = np.unique(sentence_list)
            for w in sentence_list:
                word_doc_count[w] = word_doc_count[w] + 1
				
		
        IDF = {}
        N = len(docs)
        for i in word_doc_count:
            IDF[i] = np.log(N/word_doc_count[i])
			
        centroid_vector = {}
        model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)#GoogleNews-vectors-negative300.bin file has to be present in the code folder
        model.save("word2vec.model")
        for i,document in enumerate(docs):

            if(len(doc_vector[docIDs[i]])==0):
                continue
            else:
                model_2 = Word2Vec(size=300, min_count=1)
                model_2.build_vocab(doc_vector[docIDs[i]])
                total_examples = model_2.corpus_count
                model_2.build_vocab([list(model.vocab.keys())], update=True)
                model_2.intersect_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True)
                model_2.train(doc_vector[docIDs[i]], total_examples=total_examples, epochs=model_2.iter)#Fine tuning for Cranfield Dataset

            sentence_list = doc_vector[docIDs[i]]
            sentence_list = [item for sublist in sentence_list for item in sublist]
            sentence_list = np.unique(sentence_list)
            temp = np.zeros(300)
            den = 0
            for w in sentence_list:
                if w in model.wv:
                    temp = temp + model_2.wv[w]*term_freq[docIDs[i]][w]*IDF[w]
                    den = den + term_freq[docIDs[i]][w]*IDF[w]
            if den!=0 :
                temp = temp/den
            centroid_vector[docIDs[i]] = temp
			
        
        index = {}                
        index["centroid_vector"] = centroid_vector
        index["IDF"] = IDF
        self.index = index

    def rank(self, queries):
        """
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
        """

        doc_IDs_ordered = []
        centroid_doc_vector = self.index["centroid_vector"]
        IDF = self.index["IDF"]
        
        query_vector = {}
			

        for i,query in enumerate(queries):
            sentence_list = []
            for sentence in query:
                word_list = []
                for words in sentence:
                    word_list.append(words)
                sentence_list.append(word_list)
            query_vector[i] = sentence_list
        
        term_freq = {}
		
		
        for i,query in enumerate(queries):
            term_freq[i] = {}
			
		
        for i,query in enumerate(queries):
            sentence_list = query_vector[i]
            sentence_list = [item for sublist in sentence_list for item in sublist]
            for word in sentence_list:
                term_freq[i][word] = sentence_list.count(word)
		
        model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)	
        model.save("word2vec.model")		
        for i,query in enumerate(queries):
            if(len(doc_vector[docIDs[i]])==0):
                continue
            else:
                model_2 = Word2Vec(size=300, min_count=1)
                model_2.build_vocab(doc_vector[docIDs[i]])
                total_examples = model_2.corpus_count
                model_2.build_vocab([list(model.vocab.keys())], update=True)
                model_2.intersect_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True)
                model_2.train(doc_vector[docIDs[i]], total_examples=total_examples, epochs=model_2.iter)
            
            sentence_list = query_vector[i]
            sentence_list = [item for sublist in sentence_list for item in sublist]
            sentence_list = np.unique(sentence_list)
            temp = np.zeros(300)
            den = 0
            for w in sentence_list:
                
                if w in IDF: 
                    if w in model.wv:
                        temp = temp + model_2.wv[w]*term_freq[i][w]*IDF[w]
                        den = den + term_freq[i][w]*IDF[w]

            if den!=0 :
                temp = temp/den
            cosine_similarity = {}
            for id in centroid_doc_vector:
                cosine_similarity[id] = dot(temp,centroid_doc_vector[id])/(norm(temp)*norm(centroid_doc_vector[id]))
            cosine_similarity = {k: v for k, v in sorted(cosine_similarity.items(), key=lambda item: item[1])}
            docs_ranked = []
            for id in cosine_similarity:
                docs_ranked.append(id)
            docs_ranked = docs_ranked[::-1] 
            doc_IDs_ordered.append(docs_ranked)
        
        return doc_IDs_ordered




