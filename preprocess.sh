
#copy event folder to HDFS:
hadoop fs -put /home/public/cs4984_cs5984_f18/unlabeled/data/cs4984cs5984f18_team15 /user/cs4984cs5984f18_team15/15_Shooting_Maryland_big

#run ArchiveSpark script:
export JAVA_HOME=/usr/java/jdk1.8.0_171/

spark2-shell -i ArchiveSpark_sentence_extraction.scala --files /home/public/cs4984_cs5984_f18/unlabeled/lib/en-sent.bin --jars /home/public/cs4984_cs5984_f18/unlabeled/lib/archivespark-assembly-2.7.6.jar,/home/public/cs4984_cs5984_f18/unlabeled/lib/archivespark-assembly-2.7.6-deps.jar,/home/public/cs4984_cs5984_f18/unlabeled/lib/stanford-corenlp-3.5.1.jar,/home/public/cs4984_cs5984_f18/unlabeled/lib/opennlp-tools-1.9.0.jar

#copy JSON file to home folder:
hadoop fs -get /user/cs4984cs5984f18_team15/15_Shooting_Maryland_big/sentences . 
