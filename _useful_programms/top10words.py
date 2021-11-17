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
largest = -1
word = None

newlist = list()
for key,val in di.items():
    if val > largest:
        largest = val
        word = key
    newtup = (val, key)
    newlist.append(newtup)
#newlist = sorted(newlist)    ###By default it sorted only bu KEY???                 from 999 value to 0
newlist = sorted(newlist, reverse=True)    ###By default it sorted only bu KEY???   from 0 value to 999
for val, key in newlist[0:10]:
    print(key,val)
#print(newlist)

print('The most common word',word,'it has',largest, 'matches')
print('The last word of this file in the end',w,'it has',di[w] ,'matches')

listcomprehension = sorted ( [ (v,k) for k,v in di.items() ], reverse=True ) [0:10]
print(listcomprehension)###???
#s = {key: val for key, val in enumerate('ABCD') if val not in 'CB'} ###LIST COMPREHENSION???
#print(s,type(s))
