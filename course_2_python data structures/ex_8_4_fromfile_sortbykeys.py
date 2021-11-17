fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
frange = open(fname)
data=[]
for each in frange:
    words=each.split()
    for word in words:
        if word not in data:
            data.append(word)
print(sorted(data))
