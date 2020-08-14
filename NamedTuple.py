#Understand namedtuple() works 

from collections import namedtuple

a = namedtuple("courses","name,technology")

s = a("data science","python")

print s

q = a._make(["compiler design","java"])

print q