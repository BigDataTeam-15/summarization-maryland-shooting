import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.collocations import *
import re
import string
from os import listdir
from os.path import isfile, join
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('maxent_ne_chunker')

import spacy
from spacy import displacy
from collections import Counter

nlp = spacy.load('en_core_web_sm')
#doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
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

all_words = [wordnet_lemmatizer.lemmatize(w) for w in all_words if (w.lower() not in newStopWords)]


all_words_freq = nltk.FreqDist(all_words)

most_common_word = [word[0] for word in all_words_freq.most_common(20)]

#print(most_common_word)

most_common_pos = nltk.pos_tag(most_common_word)
#print(most_common_pos)
most_common_sentence = " ".join(most_common_word)

#ne_tree = nltk.ne_chunk(most_common_pos)
#print(ne_tree)

sentences_without_stopwords = [w for w in all_words if ((w.lower() not in newStopWords))]

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = BigramCollocationFinder.from_words(sentences_without_stopwords)
most_common_colloc = finder.nbest(bigram_measures.raw_freq, 30)
most_common_bigrams = [k[0]+" "+k[1] for k,v in finder.ngram_fd.items() if k in most_common_colloc]
most_common_sentence = ", ".join(most_common_bigrams)
doc = nlp(most_common_sentence.decode("utf-8"))
#doc=nlp(sentences.decode('utf8'))
print([(X.text, X.label_) for X in doc.ents])
