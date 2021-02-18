from util import *

# Add your import statements here
import numpy as np
import gensim
from gensim import corpora, models

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
        word_list = []
        for documents in docs:
            temp = []
            for sentence in documents:
                for words in sentence:
                    temp.append(words)
            word_list.append(temp)

        dictionary_LDA = corpora.Dictionary(word_list)
        dictionary_LDA.filter_extremes(no_below=3)
        corpus = [dictionary_LDA.doc2bow(list_of_tokens) for list_of_tokens in word_list]

        num_topics = 20
        lda_model = models.LdaModel(corpus, num_topics=num_topics, \
                                  id2word=dictionary_LDA, \
                                  passes=4, alpha=[0.01]*num_topics, \
                                  eta=[0.01]*len(dictionary_LDA.keys()))#Building LDA Model

        index = {}
        index["docs"] = corpus
        index["ldamodel"] = lda_model
        index["docIDs"] = docIDs
        print("DONE")
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
        docs_retrieved = []

        lda_model = self.index["ldamodel"]
        docs = self.index["docs"]
        docIDs = self.index["docIDs"]
        word_list = []

        for query in queries:
            docs_ranked = []
            temp = []
            word_list = []
            for sentence in query:
                for word in sentence:
                    temp.append(word)
            for word in temp:
                #print(word)
                if isinstance(word,np.ndarray):
                    print("YES")
                else:
                    word_list.append(word)

            word_list = np.unique(word_list)
            word_list = [word_list]
            dictionary_LDA = corpora.Dictionary(word_list)
            dictionary_LDA.filter_extremes(no_below=3) 
            query_lda = lda_model[dictionary_LDA.doc2bow(word_list)]#Calculating query's topic distribution
            for i,doc in enumerate(docs):
                docs_retrieved.append((gensim.matutils.cossim(query_lda,lda_model[doc]),docIDs[i]))

            docs_retrieved.sort(reverse = True)
            for doc in docs_retrieved:
                docs_ranked.append(doc[1])
            doc_IDs_ordered.append(docs_ranked)
            
        return doc_IDs_ordered




