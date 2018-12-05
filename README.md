# Description 
The repo contains scripts used to summarize articles related to Maryland Shooting

# Tools Used
- NLTK
- SpaCy
- Apache Mahout
- Hadoop Cluster

# 
# Modules


 -  A set of most frequent important words
  
  - A set of WordNet synsets that cover the words
  
-  A set of words constrained by POS, e.g., nouns and/or verbs
  
 - A set of words/word stems that are discriminating features (that also are helpful in a classifier for the relevant webpages)
  
 - A set of frequent & important named entities
  
-  A set of important topics, e.g., identified using LDA
  
 - An extractive summary, as a set of important sentences, e.g., identified by clustering
  
 - A set of values for each slot matching collection semantics
  
 - A readable summary explaining the slots & values
  
 - A readable abstractive summary, e.g., from deep learning
 
This is a part of course project for Fall 2018 CS4984/5984: Big Data Text Summarization

# How To Run

The developers' manual can be found in the project report.

To run codes use python filename.py 

Filename corresponds to the developers' manual in the project report at https://www.overleaf.com/read/fwjcdbdfwvmr
(Be sure to change the path to the json file according to your own data path)
