fname = input("Enter file name: ")
fline = 0#fuck
try:
    fline = open(fname, 'r')
except:
    print("That file is not exists please retype the name of the file")
    fname = input("Enter file name: ")
fuck_1 = fuck_2 = 0
fuck_1 = float(fuck_1)
for iline in fline:
    #print(iline.rstrip().lower(),type (fline))
    if 'X-DSPAM-Confidence' in iline:
        #print(iline.rstrip())
        min_value = max_value = None
        for i in iline:
            try:
                number = int(i)
                if (min_value == None):
                    #or min_value > iline.find(i) is NOT NECESSARY
                    min_value = iline.find(i)#text.find('0') of 0.8475
                    #THERE IS A DIFFERENCE BETWEEN find and rfind!!!
                if(max_value == None or max_value < iline.rfind(i)):
                    max_value = iline.rfind(i)#text.find('5') of 0.8475
            except:
                continue
        number = float(iline[min_value:max_value+1])
        fuck_1 += number
        fuck_2 += 1
print("Average spam confidence:",fuck_1/fuck_2)
    #break
