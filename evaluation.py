from util import *

# Add your import statements here

import math



class Evaluation():

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = -1

		#Fill in code here
		#print(query_doc_IDs_ordered)
		count = 0
		i     = 0
		while (i<k ):
			if (query_doc_IDs_ordered[i] in true_doc_IDs):
				count=count+1
			i=i+1
		precision = count/k

		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		meanPrecision = -1
		total_precision = 0

		#Fill in code here
		#print(len(query_ids))
		count = 0
		for i in query_ids:
			true_doc_IDs=[]
			flag=0
			for dic in qrels:
				if(int(dic["query_num"]) == i):
					flag = 1
					true_doc_IDs.append(int(dic["id"]))
				elif(flag == 1):
					break
			#print(count,len(doc_IDs_ordered))
			total_precision = total_precision + self.queryPrecision(doc_IDs_ordered[count] , i , true_doc_IDs, k)
			count = count+1
		meanPrecision = total_precision/count

		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = -1

		#Fill in code here

		count = 0
		i     = 0
		while (i<k and i<len(query_doc_IDs_ordered)):
			if (query_doc_IDs_ordered[i] in true_doc_IDs):
				count=count+1
			i=i+1
		if(len(true_doc_IDs) > 0):
			recall = count/len(true_doc_IDs)
		else:
			recall = 1

		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

		meanRecall = -1
		total_recall = 0

		#Fill in code here

		count = 0
		for i in query_ids:
			true_doc_IDs=[]
			flag=0
			for dic in qrels:
				if(int(dic["query_num"]) == i):
					flag = 1
					true_doc_IDs.append(int(dic["id"]))
				elif(flag == 1):
					break
			total_recall = total_recall + self.queryRecall(doc_IDs_ordered[count] , i , true_doc_IDs, k)
			count = count+1
		meanRecall = total_recall/count

		return meanRecall


	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		fscore = -1
		Rak = -1
		Pak = -1

		#Fill in code here

		count = 0
		i     = 0
		while (i<k and i<len(query_doc_IDs_ordered)):
			if (query_doc_IDs_ordered[i] in true_doc_IDs):
				count=count+1
			i=i+1
		Pak = count/k
		Rak = count/len(true_doc_IDs)
		if(Pak + Rak > 0):
	        	fscore = 2 * Pak * Rak / (Pak + Rak)
		else:
			fscore = 0

		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		meanFscore = -1
		total_Fscore = 0

		#Fill in code here

		count = 0
		for i in query_ids:
			true_doc_IDs=[]
			flag=0
			for dic in qrels:
				if(int(dic["query_num"]) == i):
					flag = 1
					true_doc_IDs.append(int(dic["id"]))
				elif(flag == 1):
					break
			total_Fscore = total_Fscore + self.queryFscore(doc_IDs_ordered[count] , i , true_doc_IDs, k)
			count = count+1
		meanFscore = total_Fscore/count

		return meanFscore
	

	def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The dictionary of (ID : relevance)  of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		nDCG = -1

		#Fill in code here

		i = 0
		DCG = 0
		ideal_order = []
		#print(len(query_doc_IDs_ordered))
		while(i<k):
			#print(query_doc_IDs_ordered[i])
			if(query_doc_IDs_ordered[i] in true_doc_IDs):		
				DCG = DCG + true_doc_IDs[query_doc_IDs_ordered[i]]/math.log( (i+2) , 2)
				ideal_order.append(true_doc_IDs[query_doc_IDs_ordered[i]])
			i=i+1
		ideal_order.sort(reverse = True)
		iDCG = 0
		i = 0
		while(i< len(ideal_order)):
			iDCG = iDCG + ideal_order[i]/math.log( (i+2) , 2)
			i=i+1
		if(iDCG > 0):
			nDCG = DCG/iDCG
		else:
			nDCG = 0

		return nDCG


	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""

		meanNDCG = -1
		totalNDCG = 0		

		#Fill in code here

		count = 0
		for i in query_ids:
			true_doc_IDs={}
			flag=0
			for dic in qrels:
				if(int(dic["query_num"]) == i):
					flag = 1
					true_doc_IDs[int(dic["id"])] = 5-int(dic["position"])
				elif(flag == 1):
					break
			totalNDCG = totalNDCG + self.queryNDCG( doc_IDs_ordered[count] , i , true_doc_IDs, k)
			count = count+1
		meanNDCG = totalNDCG/count

		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precisionai
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		avgPrecision = -1

		#Fill in code here

		count = 0
		total_precision=0
		i     = 0
		
		while (i < k and i<len(query_doc_IDs_ordered)):
			if(query_doc_IDs_ordered[i] in true_doc_IDs):
				total_precision = total_precision + (count+1)/(i+1)
				count = count+1
			i=i+1
		if(count > 0):
			avgPrecision = total_precision/count
		else:
			avgPrecision = 0

		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		meanAveragePrecision = -1
		total_precision = 0

		#Fill in code here

		count = 0
		for i in query_ids:
			true_doc_IDs=[]
			flag=0
			for dic in q_rels:
				if(int(dic["query_num"]) == i):
					flag = 1
					true_doc_IDs.append(int(dic["id"]))
				elif(flag == 1):
					break
			total_precision = total_precision + self.queryAveragePrecision(doc_IDs_ordered[count] , i , true_doc_IDs, k)
			count = count+1
		meanAveragePrecision = total_precision/count

		return meanAveragePrecision

