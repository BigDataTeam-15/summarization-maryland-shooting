import re
from os import listdir
from os.path import isfile, join


path = "/home/cs4984cs5984f18_team15/articles_small/"

files = [f for f in listdir(path) if isfile(join(path, f))]

for each_file in files:
        print each_file
        with open(path+each_file, "r") as f:
                for line in f:
                        if  "high school" and "Great Mills" and "Rollins" in line:                           
                                name = re.search( r'([^.]*?( identified)[^.]*(?=shooter|)[^.]*\.)',line,re.I)                               
                                age = re.search( r'(shooter)[^.]*[0-9][1-9]-year-old', line, re.I)
                                gender = re.search(r'([^.]*?(male|female)[^.]*(?=shot)[^.]*\.)',line,re.I)
                                race = re.search(r'([^.]*?\b(race\b)[^.]*\.)',line,re.I)
                                relation_to_place = re.search(r'([^.]*?(?=shooter)[^.]*(employee|student)[^.]*\.)',line,re.I)
                                relation_to_ppl = re.search(r'([^.]*?(relation)[^.]*(?=shooter)[^.]*\.)',line,re.I)
                                shooter_die = re.search(r'([^.]*?(?=shooter)[^.]*(die|died|dead|killed|shot)[^.]*\.)',line,re.I)
                                history = re.search(r'([^.]*?(?=shooter)[^.]*(diagnosed|mental|history|illness|before)[^.]*\.)',line,re.I)
                                #To find the desired result, change the query below according 
                                if (history): print("=======>"+history.group(0))
