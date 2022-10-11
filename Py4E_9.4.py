# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary 
# that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through 
# the dictionary using a maximum loop to find the most prolific committer.

from itertools import count


fname = "mbox-short.txt"
# fname = input("Enter the filename")

# fname = input("enter the filename:")
fh = open(fname)
lst = list()
counts = dict()
counter = None


for line in fh:
    if not line.startswith("From "):
        continue
    words = line.split()
    lst.append(words[1])
    


for sort in lst:
    if sort in counts:
        counts[sort] = counts[sort] + 1
    else:
        counts[sort] = 1

# print(counts)

for high,count in counts.items():
    if counter is None or count > counter:
        counter = count
        largest = high
        highest = count
        
        
print (largest, "", highest)


    

