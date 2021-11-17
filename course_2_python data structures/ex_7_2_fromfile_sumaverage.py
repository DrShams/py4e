import re#newline
fname = input("Enter file name: ")
if(len(fname) < 1):
    fname = 'mbox-short.txt'
fline = open(fname, 'r')
f_1 = 0.0#float
numlist = list()
for line in fline:
    #if not 'X-DSPAM-Confidence' in iline: continue
    #number = float(iline[20:])
    #f_1 += number
    #numlist.append(number)
    stuff = re.findall('^X-DSPAM-C.*: ([0-9.]+)',line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    f_1 += num
    numlist.append(num)

print("Average spam confidence:",f_1/len(numlist))
#or instead of f_1 we can use sum(numlist) ???
#print(iline.rstrip().lower(),type (fline))
