from util import *

# Add your import statements here
import numpy as np
import gensim
import copy
import math
from gensim.models import LsiModel
from gensim.models import TfidfModel
from gensim import similarities
from gensim import corpora, models
class InformationRetrieval():

    def __init__(self):
        self.param = {}


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
        # Finding Vocabulary of Documents
        word_list=[]
        for doc in docs:
            for sentence in doc:
                for word in sentence:
                    word_list.append(word)
        vocabulary =  list(set(word_list))
        texts = []
        for doc in docs:
            text = []
            for sentence in doc:
                for word in sentence:
                    text.append(word)
            texts.append(text)

       
        dictionary = corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]
        tfidfmodel = TfidfModel(corpus)
        corpus_tfidf = tfidfmodel[corpus]
        lsimodel = LsiModel(corpus_tfidf, id2word=dictionary, num_topics=300) #Training LSI Model
        corpus_lsi = lsimodel[corpus_tfidf]
        index = similarities.MatrixSimilarity(corpus_lsi)
        param = {}
        param["tfidfmodel"] = tfidfmodel
        param["lsimodel"] = lsimodel
        param["dictionary"] = dictionary
        param["index"] = index
        param["docIDs"] = docIDs
        self.param = param
        

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
        tfidfmodel = self.param["tfidfmodel"]
        lsimodel = self.param["lsimodel"]
        dictionary = self.param["dictionary"]
        index = self.param["index"]
        docIDs = self.param["docIDs"]
        texts = []
        for query in queries:
            text = []
            for sentence in query:
                for word in sentence:
                    text.append(word)
            texts.append(text)
        corpus = [dictionary.doc2bow(text) for text in texts]
        corpus_tfidf = tfidfmodel[corpus]
        corpus_lsi = lsimodel[corpus_tfidf]
        for i in range(len(queries)):
            sim = index[corpus_lsi[i]]
            doc_IDs = copy.deepcopy(docIDs)
            li = []
            for j in range(len(docIDs)):
                li.append([sim[j] , doc_IDs[j]])
            li.sort()
            sort_index = []
            for x in li:
                sort_index.append(x[1])
            sort_index.reverse()
            doc_IDs_ordered.append(sort_index)
        return doc_IDs_ordered
