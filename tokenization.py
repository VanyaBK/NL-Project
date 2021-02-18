from util import *

from nltk.tokenize import TreebankWordTokenizer



class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = None
		tokenizedText = []
   
		for sentence in text:
			tokenizedText.append(sentence.split())
		
		for index,sentence in enumerate(tokenizedText):
			for idx,words in enumerate(sentence):
				if(words[len(words)-1] == ','):
					words = words[:-1]
					sentence[idx] = words.lower()
				else:
					sentence[idx] = words.lower()
			tokenizedText[index] = sentence

		
            
		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""
		
		tokenizedText = None
		tokenizedText = []
        
		for sentence in text:
			tokenizedText.append(TreebankWordTokenizer().tokenize(sentence))
		
		for idx,sentence in enumerate(tokenizedText):
			for i,word in enumerate(sentence):
				sentence[i] = word.lower()
			tokenizedText[idx] = sentence

      
		return tokenizedText