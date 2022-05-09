# In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.
#We provide two files for this assignment. One is a sample file where we give you
#the sum for your testing and the other is the actual data you need to process for the assignment.
#Sample data: (There are 90 values with a sum=445833)
#Actual data: (There are 87 values and the sum ends with 774)
#The basic outline of this problem is to read the file, look for integers using
#the re.findall(), looking for a regular expression of '[0-9]+' and then converting
#the extracted strings to integers and summing up the integers.
fname = input('Enter file name: ')
fhand = open(fname)
for line in fhand :
    line = line.split()
print(line)
