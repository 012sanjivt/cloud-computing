hadoop fs -rmr output_matrix
hadoop jar /opt/hadoop/contrib/streaming/hadoop-*streaming*.jar \
-file /home/vcslstudent/Downloads/Project2/Project2Mapper.py    -mapper /home/vcslstudent/Downloads/Project2/Project2Mapper.py \
-file /home/vcslstudent/Downloads/Project2/Project2Reducer.py   -reducer "/home/vcslstudent/Downloads/Project2/Project2Reducer.py "$1" "$2" "$3" "$4 \
-input /user/vcslstudent/input/inputfile2.txt -output /user/vcslstudent/output_matrix