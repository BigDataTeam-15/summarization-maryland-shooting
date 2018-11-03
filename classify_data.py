"""
Generate articles-vectors (Steps : seqdirectory, seq2sparse) from the big unlabelled dataset and then split them into two folders (hacky way to get unlabbelled dataset to work with testnb)
> mahout split -i ${WORK_DIR}/articles-vectors/tfidf-vectors --trainingOutput ${WORK_DIR}/articles-1-vectors --testOutput ${WORK_DIR}/articles-2-vectors --randomSelectionPct 50 --overwrite --sequenceFiles -xm sequential
> mahout testnb -i ${WORK_DIR}/articles-1-vectors -m ${WORK_DIR}/school-labelled-model -l ${WORK_DIR}/school-labelled-labelindex -ow -o ${WORK_DIR}/school-labelled-testing-1 -c
> mahout testnb -i ${WORK_DIR}/articles-2-vectors -m ${WORK_DIR}/school-labelled-model -l ${WORK_DIR}/school-labelled-labelindex -ow -o ${WORK_DIR}/school-labelled-testing-1 -c
> mahout testnb -i ${WORK_DIR}/articles-1-vectors -m ${WORK_DIR}/newsroom-labelled-model -l ${WORK_DIR}/newsroom-labelled-labelindex -ow -o ${WORK_DIR}/newsroom-labelled-testing-2 -c
> mahout testnb -i ${WORK_DIR}/articles-2-vectors -m ${WORK_DIR}/newsroom-labelled-model -l ${WORK_DIR}/newsroom-labelled-labelindex -ow -o ${WORK_DIR}/newsroom-labelled-testing-2 -c

Use seqdumper to get human readable data
> mahout seqdumper -i ${WORK_DIR}/school-labelled-testing-1/part-m-00000 > school-classified-by-model-1.txt
> mahout seqdumper -i ${WORK_DIR}/school-labelled-testing-2/part-m-00000 > school-classified-by-model-2.txt
> mahout seqdumper -i ${WORK_DIR}/newsroom-labelled-testing-1/part-m-00000 > newsroom-classified-by-model-2.txt
> mahout seqdumper -i ${WORK_DIR}/newsroom-labelled-testing-2/part-m-00000 > newsroom-classified-by-model-2.txt

Run following python script to get articles classified into appropriate folders
"""
import subprocess

event = "newsroom" # change event accordingly

path = "/home/cs4984cs5984f18_team15/"
file_name = event +"-classified-by-model-2.txt"

source_path = path +"articles/"
dest_path = path +"classified-by-model/"+ event +"-shooting/"

sentences_in_doc = []
article_no = 0
with open(path+file_name, "r") as f:
        for line in f:
                words = line.split(" ")
                if words[0] == "Key:":
                        f = words[1].replace(":","")
                        value = words[3]
                        value = value.replace("{","").replace("}","")
                        values = value.split(",")
                        values[0] = values[0][2:]
                        values[1] = values[1][2:]
                        if float(values[0]) > float(values[1]): #for newsroom > ; for school <
                                print "Relevant"
                                process = subprocess.Popen(['cp '+source_path+f+' '+dest_path], shell=True)
                        else:
                                print "Irrelevant"

