# Import nltk 
import nltk
import pyspark 
import json
from pprint import pprint
from pyspark.sql import SparkSession
from nltk.collocations import *

import nltk.collocations
import nltk.corpus
import collections


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

path = "/home/cs4984cs5984f18_team15/script/sentences/part-00000-bf4738be-c8dc-4b3a-9f3e-501f8e420e2a-c000.json"
sentences = ""

with open("/home/cs4984cs5984f18_team15/script/sentences/part-00000-bf4738be-c8dc-4b3a-9f3e-501f8e420e2a-c000.json", "r") as f:
	for line in f:
		data = json.loads(line)
		if data["Sentences_t"] != "":
			sentences = sentences + " " + data["Sentences_t"]




print("The top 100 most common words")

newStopWords = set(nltk.corpus.stopwords.words('english'))

all_words = nltk.FreqDist(w.lower() for w in sentences.split() if ((w.lower() not in newStopWords) and ('.' not in w) and (',' not in w) and (';' not in w) and ('!' not in w) and ('-' not in w) and ('&' not in w) and ('\'' not in w) and ('\"' not in w) and ('*' not in w) and ('`' not in w) and (':' not in w) and (';' not in w) and ('/' not in w) and ('?' not in w) and ('(' not in w) and (')' not in w) and ('[' not in w) and (']' not in w) and ('|' not in w) and ("\\" not in w)))
print(all_words.most_common(100))

sentences_without_stopwords = [w for w in sentences.split() if (w.lower() not in newStopWords and ('.' not in w) and (',' not in w) and (';' not in w) and ('!' not in w) and ('-' not in w) and ('&' not in w) and ('\'' not in w) and ('\"' not in w) and ('*' not in w) and ('`' not in w) and (':' not in w) and (';' not in w) and ('/' not in w) and ('?' not in w) and ('(' not in w) and (')' not in w) and ('[' not in w) and (']' not in w) and ('|' not in w) and ("\\" not in w))]

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = BigramCollocationFinder.from_words(sentences_without_stopwords)
print("The top 100 most common collocations")
print((finder.nbest(bigram_measures.raw_freq, 100)))

#collocation_words = nltk.FreqDist(w.lower() for w in finder if ((w.lower() not in newStopWords) and ('.' not in w) and (',' not in w) and (';' not in w) and ('!' not in w) and ('-' not in w) and ('\'' not in w) and ('\"' not in w) and ('*' not in w) and ('`' not in w) and (':' not in w) and (';' not in w) and ('/' not in w) and ('?' not in w) and ('(' not in w) and (')' not in w) and ('[' not in w) and (']' not in w) and ('|' not in w) and ("\\" not in w)))
#print(collocation_words.most_common(100))

