import re
from os import listdir
from os.path import isfile, join

##event = "newsroom"
path = "/home/cs4984cs5984f18_team15/cleaned_articles/"
school_words = ["austin","rollins","mills"]
newsroom_words = ["capital","gazette","ramos","jarred"]

files = [f for f in listdir(path) if isfile(join(path, f))]

for each_file in files:
        print each_file
        with open(path+each_file, "r") as f:
                article_no = each_file.replace("Article","").replace(".txt","")
                for line in f:
                        if any(word in str.lower(line) for word in school_words):
                                with open("regex_classified/school/Article"+str(article_no)+".txt", "w+") as op:
                                        op.write(line)
                                        op.close()
                        else:
                                with open("regex_classified/newsroom/Article"+str(article_no)+".txt", "w+") as op:
                                        op.write(line)
                                        op.close()
