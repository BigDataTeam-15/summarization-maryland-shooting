#Convert data into Mahout format
mahout seqdirectory -i ${WORK_DIR}/ArticleSentences/newsroom-shooting  -o clustering/articles_seq_newsroom

#To get the output vectors
mahout seq2sparse -i clustering/articles_seq_newsroom -o clustering/articles_vectors_newsroom

#To obtain the centroids
mahout canopy -i clustering/articles_vectors_newsroom/tfidf-vectors -o clustering/articles_centroids_newsroom -dm org.apache.mahout.common.distance.SquaredEuclideanDistanceMeasure -t1 500 -t2 250

mahout clusterdump –dt sequencefile –d clustering/articles_vectors_school/dictionary.file-* -i clustering/articles_centroids_school/clusters-0-final  –o report.txt

#To create model using K means
mahout kmeans –i clustering/articles_vectors_newsroom/tfidf-vectors –c clustering/articles_centroids_school/clusters-0-final –o clustering/articles_school_clusters –dm org.apache.mahout.common.distance.SquaredEuclideanDistanceMeasure –cd 1.0 –x 20 –cl
