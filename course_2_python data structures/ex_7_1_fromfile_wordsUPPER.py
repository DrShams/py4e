fname = input("Enter file name: ")
fline = open(fname, 'r')
for i in fline:
    print(i.rstrip().upper())
