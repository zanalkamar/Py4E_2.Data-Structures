# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of
# the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time 
# and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = "mbox-short.txt"
# fname = input("enter the filename:")

fh = open(fname)
lst = list()
newlst = list()
counts = dict()

for line in fh:
    if not line.startswith("From "):
        continue
    words = line.split()
    lst.append(words[5].split(":")[0])
    # words1 = [int(x) for x in lst]
# print(words1)
    
for hour in lst:
    if hour in counts:
        counts[hour] = counts[hour] + 1
    else:
        counts[hour] = 1
        
lst = sorted([(value,count) for value,count in counts.items()])
for value,count in lst:
    print(value,count)


            
        
    
    
# Desired Output
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1


    
    