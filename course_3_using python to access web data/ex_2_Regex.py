import re                               #1 REGULAR EXPRESSION
fname = input("Enter file name: ")#regex_sum_42
if (len(fname) < 1): fname = 'regex_sum_1030205.txt'
hand = open(fname,'r')
numlist = list()
for line in hand:
    line = line.rstrip()                #clean before working
    stuffs = re.findall('[0-9]+',line)
    # ([0-9.]+)
        # ( ) - these parentheses means EXTRACT INFORMATION
        # [0-9.]
            # extract any numbers from 0 to 9
        # + one or more time
    if len(stuffs) == 0 : continue      #if we have only 0 matches on the line skip it
    for stuff in range(len(stuffs)):    #range(len(stuffs)) return count of number between each line
        num = int(stuffs[stuff])
        numlist.append(num)
    #ending
    f_1 = str(sum(numlist))
print('There are',len(numlist),'values and the sum ends with',f_1[-3::])
#here [-3::] means start:stop:increment
    # -3 start from the end of the string -3
    # : second column empty means to the end of the string
    # : third increment (1 by default)
#print('There are %d values with a sum =%d' %(len(numlist),sum(numlist) )  )
    # print in tuple way %d - type integer
