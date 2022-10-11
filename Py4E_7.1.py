#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. 
# Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt
#file 'words.txt' is at C:\Py4e\Assignments



filename = input("Enter the filename:")

try:
    fhand = open(filename)
    
    for line in fhand:
        stripline = line.strip()
        print(stripline.upper())
        
except:
    print("invalid filename entered",filename)
    
