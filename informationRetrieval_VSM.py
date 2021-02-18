from util import *

# Add your import statements here
import numpy as np



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
            for sentence in documents:
                for words in sentence:
                    word_list.append(words)
        
        word_list = np.unique(word_list)
        inverted_index = {}
        doc_vector = {}
        
        for i,document in enumerate(docs):
            doc_vector[docIDs[i]] = {}
        
        for word in word_list:
            doc_list = []
            for i,document in enumerate(docs):
                count = 0
                for sentence in document:
                    for words in sentence:
                        if(words == word):
                            count = count + 1
                if(count!=0):
                    doc_list.append(docIDs[i])
                    doc_vector[docIDs[i]][word] = count
            inverted_index[word] = doc_list
        
        
        index = {}                
        index["doc_vector"] = doc_vector
        index["inverted_index"] = inverted_index
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

        #Fill in code here
        doc_vector = self.index["doc_vector"]
        inverted_index = self.index["inverted_index"]
        #print(inverted_index)
        
        N = len(doc_vector)
        
        IDF = {}
        for word in inverted_index:
            IDF[word] = np.log(N/len(inverted_index[word]))
        
        mod_doc_vector = {}
        for doc_id in doc_vector:
            mod = 0
            for word in doc_vector[doc_id]:
                doc_vector[doc_id][word] = doc_vector[doc_id][word] * IDF[word]
                mod = mod + (doc_vector[doc_id][word] * doc_vector[doc_id][word])
            mod_doc_vector[doc_id] = mod
        
        
        for query in queries:
            docs_ranked = []
            query_vector = {}
            word_list = []
            doc_retrieved = []
            for sentence in query:
                for word in sentence:
                    word_list.append(word)
            word_list = np.unique(word_list)
            #print(word_list)
            for word in word_list:
                if word.lower() in inverted_index:
                    doc_retrieved.append(inverted_index[word.lower()])
            doc_retrieved = [val for sublist in doc_retrieved for val in sublist]
            doc_retrieved = np.unique(doc_retrieved)
            doc_retrieved = doc_retrieved.tolist()
            for word in word_list:
                count=0
                for sentence in query:
                    for words in sentence:
                        #print(word,words)
                        if(word==words):
                            count=count+1
                if(count != 0):           
                    if word.lower() in IDF:
                        query_vector[word.lower()] = count * IDF[word.lower()]
                    else:
                        query_vector[word] = count * np.log(N) # Using a smoothing factor of 1 in the denominator
            mod = 0
            for word in query_vector:
                #print(word)
                mod = mod + (query_vector[word] * query_vector[word])
            cosine_similarity = {}
            for docs in doc_retrieved:
                num = 0
                for word in query_vector:
                    if word in doc_vector[docs]:
                        num = num + (doc_vector[docs][word] * query_vector[word])
                cosine_similarity[docs] = num/(np.sqrt(mod)*np.sqrt(mod_doc_vector[docs]))
            
            sorted_cosine = {k: v for k, v in sorted(cosine_similarity.items(), key=lambda item: item[1])}    
            for docs in sorted_cosine:
                docs_ranked.append(docs)
            docs_ranked = docs_ranked[::-1] 
            doc_IDs_ordered.append(docs_ranked)
        
                                
        #print(doc_IDs_ordered)
        return doc_IDs_ordered




