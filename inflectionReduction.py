from util import *

from nltk.stem import WordNetLemmatizer
#from nltk.stem import PorterStemmer

class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = None
		
		reducedText = []
        #porter_stemmer_object = PorterStemmer()
		wordnet_lemmatizer_object = WordNetLemmatizer()
		
		for sentence in text:
			reduced_sentence = []
			for word in sentence: 
				reduced_sentence.append(wordnet_lemmatizer_object.lemmatize(word))
                #reduced_sentence.append(porter_stemmer_object.stem(word))
			reducedText.append(reduced_sentence)
			
		return reducedText


