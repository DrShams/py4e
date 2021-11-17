lotto_list = [ 5, 3, 55, 53, 88, 55 ,55]
lotto_tuple = (15, 13, 155, 153, 188, 200, 999, 999) #does not have to build up structures
lotto_tuple_2 = (88, 1, 34, 153, 188, 200, 999, 999)
print(dir(lotto_list))
(x,y) = (lotto_tuple[0] , lotto_tuple[1])
print(y)
lotto_list.sort()               #1 2 3 4 5
lotto_list.reverse()            #5 4 3 2 1
if lotto_tuple_2 > lotto_tuple:
    print('lotto_tuple_2 yes')
else:
    print('lotto_tuple no')
#print(dir(lotto_list))
print('tuple dir',dir(lotto_tuple))
#lotto_tuple.sort()             ###CANNOT DO IT WITH TUPLE
#lotto_tuple.append('book')     ###CANNOT DO IT WITH TUPLE
print('lotto_list.count',lotto_list.count(55))
print('lotto_tuple.count',lotto_tuple.count(999))
print('lotto',type(lotto_list),lotto_list[2])       #mutable
print('lotto_2',type(lotto_tuple),lotto_tuple[2])   #immutable!
print(sorted(lotto_list))
print('sorted(lotto_tuple)',sorted(lotto_tuple))
print('sorted(lotto_tuple_2)',sorted(lotto_tuple_2))
stuff = list()
stuff.append('book')
stuff.append(69)
print(stuff)
if (69 in stuff):
    print("yes")
else:
    print("no")
x = 'potato was fucking                  ; good'
z = x.split()
y = x.split(';')
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From') : continue
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    #print(pieces)
#print(len(line))
x = list(range(5))
#print(type(x))

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])
