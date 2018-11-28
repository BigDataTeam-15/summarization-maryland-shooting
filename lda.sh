
export WORK_DIR=/user/cs4984cs5984f18_team15/15_Shooting_Maryland_big/

#NEWSROOM

#Converting text documents to SequenceFile format
mahout seqdirectory –i ${WORK_DIR}/newsroom –o ${WORK_DIR}/n-seq -c UTF-8

#Creating vectors from SequenceFile
mahout seq2sparse –i ${WORK_DIR}/n-seq –o ${WORK_DIR}/n-vectors -wt tf --namedVector

#Creating integer IDs from text IDs
mahout rowid -i ${WORK_DIR}/n-vectors/tf-vectors -o ${WORK_DIR}/n-matrix

#Invoking LDA (CVB version) algorithm
mahout cvb -i ${WORK_DIR}/n-matrix/matrix -o ${WORK_DIR}/n-ldaOut -k 50 –x 10 –dt ${WORK_DIR}/n-topicOut -dict ${WORK_DIR}/n-vectors/dictionary.file-0

#Output the computed topics (the output should be on the file system, not on Hadoop)
mahout vectordump -i ${WORK_DIR}/n-ldaOut -d ${WORK_DIR}/n-vectors/dictionary.file-0 -o n-ldaTopics -dt sequencefile –sort ${WORK_DIR}/n-ldaOut –vs 1

#SCHOOL

#Converting text documents to SequenceFile format
mahout seqdirectory –i ${WORK_DIR}/school –o ${WORK_DIR}/s-seq -c UTF-8

#Creating vectors from SequenceFile
mahout seq2sparse –i ${WORK_DIR}/s-seq –o ${WORK_DIR}/s-vectors -wt tf --namedVector

#Creating integer IDs from text IDs
mahout rowid -i ${WORK_DIR}/s-vectors/tf-vectors -o ${WORK_DIR}/s-matrix

#Invoking LDA (CVB version) algorithm
mahout cvb -i ${WORK_DIR}/s-matrix/matrix -o ${WORK_DIR}/s-ldaOut -k 50 –x 10 –dt ${WORK_DIR}/s-topicOut -dict ${WORK_DIR}/s-vectors/dictionary.file-0

#Output the computed topics (the output should be on the file system, not on Hadoop)
mahout vectordump -i ${WORK_DIR}/s-ldaOut -d ${WORK_DIR}/s-vectors/dictionary.file-0 -o s-ldaTopics -dt sequencefile –sort ${WORK_DIR}/s-ldaOut –vs 1
