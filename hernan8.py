# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
fname = input("Enter file:")
fh = open(fname)
encarta = dict()
bg = None
bc = None
for line in fh :
    if line.startswith('From: ') :
        words = line.split()
        words = words[1:]
        for word in words :
            encarta[word] = encarta.get(word, 0) + 1
            for word,count in encarta.items() :
                if bc is None or count > bc :
                    bg = word
                    bc = count
print(bg,bc)
