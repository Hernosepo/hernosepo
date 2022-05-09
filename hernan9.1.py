#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
fname = input('Como se llama el archivo? ')
fhand = open(fname)
encarta = dict()
lst = list()
for line in fhand :
    if not line.startswith('From ') : continue
    words = line.split()
    hour = words[5]
    hour = hour.split(':')
    piece = hour[0]
    #print(piece)
    for word in piece :
        encarta[word] = encarta.get(word,0) + 1
    #for k,v in encarta.items() :
    #    tupper = (v,k)
    #    lst.append(tupper)
    #    lst = sorted(lst, reverse=True)
    #for v,k in lst :
    #    print(k,v)
