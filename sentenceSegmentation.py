from util import *


class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = None
		sentence = ''
		segmentedText = []
		
		for idx,character in enumerate(text):
			if((character=='.') or (character=='?') or (character=='!') or (character==';') or (character==':') or (character=='"')):
					sentence+=character				# The punctuation marks can be used to infer what the sentence conveys
					segmentedText.append(sentence)
					sentence=''
			else:
				sentence+=character

		return segmentedText





	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

		segmentedText = None
		segmentedText = []
        
		tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
		segmentedText = tokenizer.tokenize(text)
		
		return segmentedText