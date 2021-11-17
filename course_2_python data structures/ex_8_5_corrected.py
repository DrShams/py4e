fname = input("Enter file name: ")
frange = open(fname)
newlist=[]
for each in frange:
    ###each = each.rstrip()
    if each.startswith('From') and len(each.split()) == 7:
        print(each.split()[1])
        newlist.append(each.split()[1])
        ###pieces = each.split()[1].split('@')
print("There were", len(newlist), "lines in the file with From as the first word")
