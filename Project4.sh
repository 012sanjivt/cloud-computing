hadoop fs -rmr output_kmers
hadoop jar /opt/hadoop/contrib/streaming/hadoop-*streaming*.jar \
-file /home/vcslstudent/Downloads/Project4/Project4Mapper.py    -mapper /home/vcslstudent/Downloads/Project4/Project4Mapper.py \
-file /home/vcslstudent/Downloads/Project4/Project4Reducer.py   -reducer /home/vcslstudent/Downloads/Project4/Project4Reducer.py \
-input /user/vcslstudent/input/ecoli.fa -output /user/vcslstudent/output_kmers