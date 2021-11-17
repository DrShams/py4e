fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
frange = open(fname)
newlist=[]#list()
mailsdict={}#dict()
for each in frange:
    each = each.rstrip() #delete additional spaces
    if each.startswith('From') and len(each.split()) == 7:
        mail = each.split()[1]
        newlist.append(mail)
        mailsdict[mail] = mailsdict.get(mail, 0) + 1
        #pieces = each.split()[1].split('@')
        #print(pieces[0])
maxmailcount = max(mailsdict.values())#type dict
maxmailcounter = max(mailsdict, key=mailsdict.get)#THAT IS THE PROBLEM HOW TO GET THIS MAX COUNTER
print(maxmailcounter, maxmailcount)
