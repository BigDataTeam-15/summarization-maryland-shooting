import nltk
import pyspark
import json
from nltk.collocations import *
from nltk.corpus import wordnet as wn

import nltk.collocations
import nltk.corpus
import collections

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

import re
from os import listdir
from os.path import isfile, join
import string
#path = "/home/cs4984cs5984f18_team15/script/sentences/part-00000-bf4738be-c8dc-4b3a-9f3e-501f8e420e2a-c000.json"
#path = "/home/cs4984cs5984f18_team15/script/sentences/part-00000-df24903a-c0b9-4e79-85a7-f97de2918e4c-c000.json"
sentences = ""

#with open(path, "r") as f:
#        for line in f:
#                data = json.loads(line)
#                if data["Sentences_t"] != "":
                        #out.write(data["Sentences_t"])
                        #out.write("\n")
#                        sentences = sentences + " " + data["Sentences_t"]


newStopWords = set(nltk.corpus.stopwords.words('english'))
total_words = len(sentences.split())
path = "/home/cs4984cs5984f18_team15/regex_classified/school/"

files = [f for f in listdir(path) if isfile(join(path, f))]

for each_file in files:
        print each_file
        with open(path+each_file, "r") as f:
                for line in f:
                        sentences = sentences + " " + line

all_words = [x.strip(string.punctuation) for x in sentences.split()]

newStopWords = set(nltk.corpus.stopwords.words('english'))

#all_words_freq = nltk.FreqDist(w.lower() for w in all_words if ((w.lower() not in newStopWords)))
all_words = [wordnet_lemmatizer.lemmatize(w.lower()) for w in all_words if (w.lower() not in newStopWords)]
#print(all_words_freq.most_common(15))

#all_words = [wordnet_lemmatizer.lemmatize(w.lower()) for w in sentences.split() if ((w.lower() not in newStopWords) and ('.' not in w) and (',' not in w) and (';' not in w) and ('!' not in w) and ('-' not in w) and ('&' not in w) and ('\'' not in w) and ('\"' not in w) and ('*' not in w) and ('`' not in w) and (':' not in w) and (';' not in w) and ('/' not in w) and ('?' not in w) and ('(' not in w) and (')' not in w) and ('[' not in w) and (']' not in w) and ('|' not in w) and ("\\" not in w))]
#print(all_words[0:100])

all_words_freq = nltk.FreqDist(all_words)

most_common_word = [word[0] for word in all_words_freq.most_common(20)]
most_common_pos = nltk.pos_tag(most_common_word)
print(most_common_pos)

print("Nouns: ")
nouns = [wt[0] for wt  in most_common_pos if (wt[1] == 'NN' or wt[1] == 'NNS')]
print(nouns)
print("Verbs: ")
verbs = [wt[0] for wt in most_common_pos if (wt[1] == 'VB' or wt[1] == 'VBD' or wt[1] == 'VBG' or wt[1] == 'VBN')]
print(verbs)
