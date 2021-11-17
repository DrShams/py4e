fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:### IN HERE WE STORE 'w' as GLOBAL VALUE
        #idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1
        #print(w,'has',di[w], 'matches')
#print(di)

newlist = list()
for k,v in di.items():
    #print(k,v)
    newtuple = (v,k)
    newlist.append(newtuple)
newlist = sorted(newlist, reverse=True)
#print(newlist[0:5])

for v,k in newlist[0:5]:
    print(k,v)
