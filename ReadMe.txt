#Project 3: Finding common friend in MapReduce


Program Description:

Mapper:

Mapper takes the input from inputfile.txt in the following format:
<UserID><,><FriendID1><space><FriendID2>----<FriendIDN>
For each userID received from the inputfile, mapper emits the key as user and a friend and the friendlist as value for all the user-friend pair 
for the received line. Same thing happens in the mapper until everything is received from the inputfie. Mapper sort the key before emitting.

Reducer:

Reducer receives the output of mapper in the form of <key, value> where key is the combination of userID-friendID and value is the list
of friendID for that key combination. Since there is always two records for the same key, at first pass, the friendlist for that key is stored 
in a list. During the second pass, the stored list is interesected with the current list to find the common/mutual friend for that
key(userID-friendID pair).
Reducer then emits the output in the format:
<userID1><,><userID2><space><[><friendID1><,friendID2>---<friendIDN><]>	


	# To run on MapReduce framework:
		Create a directory "Project3" in "/home/vcslstudent/Downloads/".
		Copy files "inputfile.txt", "Project3.sh", "Project3Mapper.py", "Project3Reducer.py" in Project3.
		Give permissions to all the files for execution as "chmod +x <filenames>".
		Create "input" directory in hadoop filesystem, "hadoop fs -mkdir input"
		Copy "inputfile.txt" to hadoop filesystem with command "hadoop fs -put <filename> input"
		Run sh file as :
			./Project3.sh
		See the output as "hadoop fs -cat /user/vcslstudent/output_mutual/part-00000".