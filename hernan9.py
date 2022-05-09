fname = input('Como se llama el archivo? ')
fhand = open(fname)
encarta = dict()
lst = list()
for line in fhand :
    words = line.split()
    for word in words :
        encarta[word] = encarta.get(word,0) + 1
for k,v in encarta.items() :
    tupper = (v,k)
    lst.append(tupper)
lst = sorted(lst, reverse=True)
for v,k in lst[:10] :
    print(k,v)
