# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt


fname = input("enter the filename:")
fh = open(fname)
lst = list()
noduplst = list()

for line in fh:
    temp = line.rstrip()
    words = temp.split()
    for word in words:
        lst.append(word)
    
for dup in lst:
    if dup in noduplst:
        continue
    else:
        noduplst.append(dup)
        noduplst.sort()
        

print(noduplst)
