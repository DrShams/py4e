import re                               #1 REGULAR EXPRESSION
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    #if re.search('^From:' , line):     #1 REGULAR EXPRESSION
    #if 'From:' in line:                #2 IT'S THE SAME AS #1
    #if line.startswith('From:'):       #2
    #y = re.findall('^From.(\S+@\S+)',line)   #3 LIST class OF THE MATCHES mail address only
    if '@' in line:
    #VERSION 1 old way
        pos_from = line.find('@')
        pos_end = line.find(' ',pos_from)#4 THAT COULD BE NOT SO IT MIGHT RETURN -1
        host = line[pos_from+1 : pos_end]#5 SKIP POSITION WHICH CONTAIN '@'
        #print(host)
    #VERSION 2 double split pattern
        words = line.split()
        email = words[1]                #6 IN THE LINE mail could be not on [1] !
        #print(email)
        pieces = email.split('@')
    #VERSION 3 regular expressions pattern with re import
        regvalue = re.findall('@([^ ]*)',line)  #7 [^ ] MATCH non-black character * match many of them
                                                #7 [] MATCH not!
                                                #7 ^ BEGIN WITH
                                                #7 ( ) THATS WE WANT TO EXTRACT
        #print(regvalue)                 ###GREAT DECISION
        regvalue = re.findall('^From .*@([^ ]*)',line) #8 IT COULD NOT contain FROM so we will get BLANK lines
        #print(regvalue)
    ###
    stuff = re.findall('^X-DSPAM-C.*: ([0-9.]+)',line)
    # ^ start with X-DSPAM word
    # . matches any character after X-DSPAM-C
    # * one or more times
    # X-DSPAM and : this the words/characters we searching for
    # ([0-9.]+)
        # ( ) - these parentheses means EXTRACT INFORMATION
        # [0-9.]
            # extract any numbers from 0 to 9
            # . and dot character cause we need float (ex. 0.8475)
        # + one or more time
    #print(stuff)

    if len(stuff) != 1 : continue
    #print(stuff, line)
    num = float(stuff[0])
    numlist.append(num)
#print(numlist)

x = 'My car is cost around ♦721000 roubles when I bought it in the beginning 2018'
price = re.findall('\♦[0-9.]+',x)
#print('so the price was',price,'but what shit sign mean "♦"??? I can all it through ALT+num4')
#print(type(price))
# MORE ABOUT REGULAR EXPRESSIONS
# https://docs.python.org/3/howto/regex.html
# CHEAT CODE SHEET FROM CHUCK
# https://www.coursera.org/learn/python-network-data/supplement/2WnqH/python-regular-expression-quick-guide
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
#y = re.findall('^F.{1,}:', x) #THE SAME CODE
    # ^ Beginning from 'F' word
    # . any characters
    # + 1 or more time . any character after F before :
    # : it should be finished by this sign

    #OUTPUT
    #From: Using the :
print(y)
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
print(y)
