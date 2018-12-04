
from __future__ import division
import nltk
from nltk.corpus import PlaintextCorpusReader

'''path = "/home/cs4984cs5984f18_team15/"'''
school_root = '/home/cs4984cs5984f18_team15/classified-small-log-newsroom/relevant/'
school_wordlists = PlaintextCorpusReader(school_root, ".*\.txt")
school = school_wordlists.raw()

tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")

schoolToken = tokenizer.tokenize(school)

'''print(schoolToken)'''


'''#Topic identification using LDA (gensim) example-Code:
#Created on Oct 15, 2014
#Authors: Xuan Zhang and Tarek Kanan'''
from gensim import corpora, models
from nltk.corpus import stopwords
#Call the NLTK stop words list
stoplist = stopwords.words('english')

documents = schoolToken
#Remove the stop words
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]
#Build the dictionary and the corpus
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
#Define the LDA model and the number of topics.
notopics = 3
lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=notopics)
#Printing the topic with their probabilities
print "\n\n", notopics, "Topics with their corresponding probabilities\n"
for i in range(0, lda.num_topics):
	print "Topic", i+1, ":", lda.print_topic(i)

