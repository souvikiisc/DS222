#!/bin/bash

hdfs dfs -rm -r /user/souvikk/acc_train

hdfs dfs -rm -r /user/souvikk/train_a1

hadoop jar /usr/hdp/2.6.1.0-129/hadoop-mapreduce/hadoop-streaming.jar -libjars /home/souvikk/mlld/assignment1/custom.jar -outputformat com.custom.CustomMultiOutputFormat -mapper /home/souvikk/mlld/assignment1/mapper.py -reducer /home/souvikk/mlld/assignment1/reducer_1.py -input /user/ds222/assignment-1/DBPedia.full/full_train.txt -output /user/souvikk/train_a1 -numReduceTasks 1

hadoop jar /usr/hdp/2.6.1.0-129/hadoop-mapreduce/hadoop-streaming.jar -cacheFile /user/souvikk/train_a1/class_word_count/part-00000#ref1 -cacheFile /user/souvikk/train_a1/doc_count/part-00000#ref2 -cacheFile /user/souvikk/train_a1/class_total_word_count/part-00000#ref3 -mapper /home/souvikk/mlld/assignment1/mapper_test.py -reducer /home/souvikk/mlld/assignment1/reducer_test_1.py -input /user/ds222/assignment-1/DBPedia.full/full_test.txt -output /user/souvikk/acc_train -numReduceTasks 1
