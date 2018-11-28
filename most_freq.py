import nltk
import pyspark
import json
from pprint import pprint
from pyspark.sql import SparkSession
from nltk.collocations import *
import string

import nltk.collocations
import nltk.corpus
import collections

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

#path = "/home/cs4984cs5984f18_team15/script/sentences/part-00000-bf4738be-c8dc-4b3a-9f3e-501f8e420e2a-c000.json"
#path = "/home/cs4984cs5984f18_team15/script/sentences/part-00000-df24903a-c0b9-4e79-85a7-f97de2918e4c-c000.json"
sentences = ""

#with open("/home/cs4984cs5984f18_team15/script/sentences/part-00000-df24903a-c0b9-4e79-85a7-f97de2918e4c-c000.json", "r") as f:
#       for line in f:
#               data = json.loads(line)
#               if data["Sentences_t"] != "":
#                       sentences = sentences + " " + data["Sentences_t"]



#print(type(sentences))
import re
from os import listdir
from os.path import isfile, join

##event = "newsroom"
path = "/home/cs4984cs5984f18_team15/regex_classified/school/"

files = [f for f in listdir(path) if isfile(join(path, f))]

for each_file in files:
        print each_file
        with open(path+each_file, "r") as f:
                for line in f:
                        sentences = sentences + " " + line

all_words = [x.strip(string.punctuation) for x in sentences.split()]

print("The top 15 most common words")

newStopWords = set(nltk.corpus.stopwords.words('english'))

all_words_freq = nltk.FreqDist(w.lower() for w in all_words if ((w.lower() not in newStopWords)))
print(all_words_freq.most_common(15))

sentences_without_stopwords = [w for w in all_words if ((w.lower() not in newStopWords))]

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = BigramCollocationFinder.from_words(sentences_without_stopwords)
print("The top 15 most common collocations")
most_common_colloc = finder.nbest(bigram_measures.raw_freq, 15)
print(most_common_colloc)
i=0
for k,v in finder.ngram_fd.items():
        if k in most_common_colloc: print(k,v)
