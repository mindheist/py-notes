# reference : https://www.youtube.com/watch?v=ZdDOauFIDkw

import re
#print (re.split(r'\s*','here are some words'))
# in the above simply split by space only
print (re.split(r'\s{2}','here are some  words'))
# in the above split based on two spaces
print (re.split(r'[a-d]','here are some randome stuff'))
print (re.split(r'([a-d])','here are some randome stuff'))
# the difference between line 8 and 9 is the grouping
print (re.split(r'[a-z]','fdhgfhsfDGFHDSGHHgsfaasgFFGNDFASdfADfd'))
print (re.split(r'([a-z])','fdhgfhsfDGFHDSGHHgsfaasgFFGNDFASdfADfd'))
