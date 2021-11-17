name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
frange = open(name)
hcount,newlist = dict(),list()

for line in frange:
    line = line.split()
    if 'From' in line and len(line) > 2:
        hourv = line[5].split(':')
            #line = ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
                #line[5] = '09:14:16'
                #hourv = ['09', '14', '16']
        hcount[hourv[0]] = hcount.get(hourv[0], 0) + 1
for k,v in hcount.items():
    newlist.append((k,v))
newlist.sort()
for k,v in newlist:
    print (k,v)
#listcomprehension = sorted ( [ (k,v) for k,v in hcount.items() ], reverse=False )
#print(listcomprehension)
