export WORK_DIR=/user/cs4984cs5984f18_team15/15_Shooting_Maryland_small

"Creating sequence files

mahout seqdirectory -i /user/cs4984cs5984f18_team15/15_Shooting_Maryland_big/manually-labelled-common-shooting -o ${WORK_DIR}/logistic_regression/shooting_sequence -ow


"Converting sequence files to vectors"

mahout seq2sparse -i ${WORK_DIR}/logistic_regression/shooting_sequence -o ${WORK_DIR}/logistic_regression/shooting_vectors  -lnorm -nv  -wt tfidf


 "Creating training and holdout set with a random 80-20 split of the generated vector dataset"
  mahout split -i ${WORK_DIR}/logistic_regression/shooting_vectors/tfidf-vectors --trainingOutput ${WORK_DIR}/logistic_regression/train_vectors --testOutput ${WORK_DIR}/logistic_regression/test_vectors  --randomSelectionPct 40 --overwrite --sequenceFiles -xm sequential

  echo "Training Naive Bayes model"
 mahout trainnb -i ${WORK_DIR}/logistic_regression/train_vectors -o ${WORK_DIR}/logistic_regression/models -el -li ${WORK_DIR}/logistic_regression/labelindex -ow -c

 echo "Self testing on training set"

mahout testnb -i ${WORK_DIR}/logistic_regression/train_vectors -m ${WORK_DIR}/logistic_regression/models -el -l ${WORK_DIR}/logistic_regression/labelindex -ow -o ${WORK_DIR}/logistic_regression/shooting_testing -c

echo "Testing on holdout set"

mahout testnb -i ${WORK_DIR}/logistic_regression/test_vectors -m ${WORK_DIR}/logistic_regression/models -l ${WORK_DIR}/logistic_regression/labelindex -ow -o ${WORK_DIR}/logistic_regression/shooting_testing_holdout -ow $c
