import nltk
import pyspark
import json
from pprint import pprint
from pyspark.sql import SparkSession
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

path = "/home/cs4984cs5984f18_team15/script/sentences/part-00000-bf4738be-c8dc-4b3a-9f3e-501f8e420e2a-c000.json"

sentences = ""

with open(path, "r") as f:
        for line in f:
                data = json.loads(line)
                if data["Sentences_t"] != "":
                        #out.write(data["Sentences_t"])
                        #out.write("\n")
                        sentences = sentences + " " + data["Sentences_t"]


newStopWords = set(nltk.corpus.stopwords.words('english'))
total_words = len(sentences.split())
all_words = [wordnet_lemmatizer.lemmatize(w.lower()) for w in sentences.split() if ((w.lower() not in newStopWords) and ('.' not in w) and (',' not in w) and (';' not in w) and ('!' not in w) and ('-' not in w) and ('&' not in w) and ('\'' not in w) and ('\"' not in w) and ('*' not in w) and ('`' not in w) and (':' not in w) and (';' not in w) and ('/' not in w) and ('?' not in w) and ('(' not in w) and (')' not in w) and ('[' not in w) and (']' not in w) and ('|' not in w) and ("\\" not in w))]
#print(all_words[0:4])

all_words_freq = nltk.FreqDist(all_words)

most_common_word = all_words_freq.most_common(20)
print(most_common_word)

synset_sets = []
hyper_hypo_sets = []
for word, freq in most_common_word:
	#print(word,wn.synsets(word))
	each_synset = set()
	each_hyper_hypo = set()
	for each_word_syn in wn.synsets(word):
		for lemma in each_word_syn.lemmas():
			each_synset.add(str(lemma.name()).lower())
		for hypernym in each_word_syn.hypernyms():
                        each_hyper_hypo.add(str(lemma.name()).lower())
		for hyponym in each_word_syn.hyponyms():
                        each_hyper_hypo.add(str(lemma.name()).lower())


	synset_sets.append(each_synset)
	hyper_hypo_sets.append(each_hyper_hypo)
print("List of common synsets")
print(synset_sets)

print("List of hypernyms and hyponyms")
print(hyper_hypo_sets)

count = 0
for each_synset in synset_sets:
	count = 0
	for word in all_words:
		if word in each_synset:
			count = count +1
	print(count, each_synset)



