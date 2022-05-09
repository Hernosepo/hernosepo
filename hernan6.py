fname = input("Enter file name: ")
fh = open(fname)
lst = list()
sol = []
for line in fh:
    line = line.split()
    lst = line + lst
    for count in lst :
        if count not in sol :
            sol.append(count)
sol.sort()
print(sol)
