#Document classification with CBayes classification algorithm using mahout

export WORK_DIR=/user/cs4984cs5984f18_team15/15_Shooting_Maryland_big/

#Convert the manually labelled dataset into a < Text, Text > SequenceFile.
mahout seqdirectory -i ${WORK_DIR}/manually-labelled -o ${WORK_DIR}/manually-labelled-seq -ow

#Convert and preprocesses the dataset into a < Text, VectorWritable > SequenceFile containing term frequencies for each document.
mahout seq2sparse -i ${WORK_DIR}/manually-labelled-seq -o ${WORK_DIR}/manually-labelled-vectors -lnorm -nv -wt tfidf

#Split the preprocessed dataset into training and testing sets.
mahout split -i ${WORK_DIR}/manually-labelled-vectors/tfidf-vectors --trainingOutput ${WORK_DIR}/manually-labelled-train-vectors --testOutput ${WORK_DIR}/manually-labelled-test-vectors --randomSelectionPct 40 --overwrite --sequenceFiles -xm sequential
 
#Train the classifier.
mahout trainnb -i ${WORK_DIR}/manually-labelled-train-vectors -el -o ${WORK_DIR}/manually-labelled-model -li ${WORK_DIR}/manually-labelled-labelindex -ow -c

#Test the classifier.
mahout testnb -i ${WORK_DIR}/manually-labelled-test-vectors -m ${WORK_DIR}/manually-labelled-model -l ${WORK_DIR}/manually-labelled-labelindex -ow -o ${WORK_DIR}/manually-labelled-testing -c
