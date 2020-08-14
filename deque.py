#Understand how deque and its operations

from collections import deque

a = ["l","a","l","i","t","h"]

d = deque(a)

print d 	#Prints the deque

d.append("python")	#Appends the python at last

print d

d.appendleft("machine learning")	#Inserts the element at the beginning of the list

print d

d.pop()	#Pops the last element from the deque

print d

d.popleft()	#Pops the first element from the deque

print d