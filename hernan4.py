# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for lx in fh :
    ly = lx.rstrip()
    lu = ly.upper()
    print(lu)
