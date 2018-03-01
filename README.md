# Hadoop-HDFS-MapReduce

Write a MapReduce code to count phrases (pair of words, taken sequentially) in lines of text as follows. The default input key for the TextInput format is the line number. In this program , the required output is the count of word pairs. 

NOTE: punctuation will NOT count; so the words is ‘(1991)’ and ‘1991’ are the same. Therefore, you must parse your file: remove all characters not in this set: [a-z, A-Z, 0-9] ; ‘the-cat’ and ‘the cat’ should be counted as the same pair.

<b>e.g.</b> line:

<b>Input:</b> (k,v) = (1,“the cat in the hat is the best cat in the hat”)

<b>Output:</b> (k2,v2) = (“the cat”, 1), (“cat in”,2),(‘in the’,2),(‘the hat’,2’),(‘hat is’,1), etc

If the line contains a single word, then that becomes the ‘pair’.
For this code,use the input file: adventures.txt

Note: The code MUST run in Hadoop.
