purse = dict()
purse['money'] = 999999
purse['cars'] = 2
purse['health'] = 100
purse['freedom'] = '53%'

#print(purse['health'])
purse['health'] = purse['health'] - 1
print(sorted(purse.items()))        ###that print KEYS AND VALUES
print(sorted(purse))                ###that ptiny only KEYS
print(purse)
for (k,v) in sorted(purse.items()): ###that give us sorted in KEY order
    print('dict k v',k,v)
#tups = purse.items()
#print('tups',tups)
#print('dict',purse)
#print(purse)
#print(len(purse))

newdict = dict()
newdict = { 'money[usd]' : 9999999, 'cars' : 5, 'health' : 80, 'freedom' : '55%' }
#print(newdict)
newvalue = { }#that means we define dictionary
#print(newvalue,type(newvalue))
mostcname = dict()
mostcname['Ruslan'] = 1
mostcname['Liaisan'] = 1
#print(mostcname)
#print(mostcname['WhoWillbe']) DOEST EXISTS
mostcname['Liaisan'] = mostcname['Liaisan'] + 1 #class dict
#print(mostcname)

newname = ['Robert',88,55.66,'Ruslan'] #class list
for name in newname:
    #if name not in mostcname:
    #    mostcname[name] = 1
    #else:
    #    mostcname[name] = mostcname[name] + 1
    mostcname[name] = mostcname.get(name, 0) + 1#if it exists it return current value +1  if not retunr0 0 + 1
#print(mostcname)
x = mostcname.get('Tamara', 0)
#print(x) #0 because Arab doesm't exists and we assign him 0
x = mostcname.get('Ruslan', 0)
#print(x) #2 because Ruslan exists we get the value
#print(mostcname)
#print(type(mostcname),len(mostcname),type(newname))
#print('items',mostcname.items())
#print('keys',mostcname.keys()) # THAT WORKS WELL!
#print('values',mostcname.values())
stuff = dict()
#print(stuff.get('candy',-1))
x , y = 3, 4
print (y)
