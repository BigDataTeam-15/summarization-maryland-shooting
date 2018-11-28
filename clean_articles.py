import re
from os import listdir
from os.path import isfile, join

##event = "newsroom"
path = "/home/cs4984cs5984f18_team15/articles/"
unwanted_words = ["cevario","share","delete","drugs","subscribe","broadcastng","mexico","soccer","related stories","label","feedback","florida","cleveland","archive","advertisement","news","weather","reuters","account","log","email","password","reply","twitter","facebook","video","podcast","login","signup","copyright","cookies","reserved","forecast","material","newsletter","users","..."]

files = [f for f in listdir(path) if isfile(join(path, f))]

for each_file in files:
        print each_file
        with open(path+each_file, "r") as f:
                article_no = each_file.replace("Article","").replace(".txt","")
                sentence_no = 0
                for line in f:
                        sentences = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', line)
                        new_line = ""
                        for sentence in sentences:
                                if any(word in str.lower(sentence) for word in unwanted_words) or len(sentence)>400 or len(sentence)<30:
                                        print("Skipping Article"+article_no)
                                else:
                                        new_line = new_line + " " + sentence

                        if new_line:
                                with open("cleaned_articles/Article"+str(article_no)+".txt", "w+") as op:
                                        op.write(new_line)
                                        op.close()
