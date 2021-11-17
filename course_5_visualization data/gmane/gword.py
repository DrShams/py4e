import sqlite3
import time
import zlib
import string

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.execute('SELECT id, subject FROM Subjects')
subjects = dict()
for message_row in cur :
    subjects[message_row[0]] = message_row[1]

# cur.execute('SELECT id, guid,sender_id,subject_id,headers,body FROM Messages')
cur.execute('SELECT subject_id FROM Messages')
counts = dict()
for message_row in cur :
    text = subjects[message_row[0]]
    text = text.translate(str.maketrans('','',string.punctuation))  #no punctuation
    text = text.translate(str.maketrans('','','1234567890'))        #no counts dictionary count
    text = text.strip()#removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
    text = text.lower()
    words = text.split()#make a list with words
    for word in words:
        if len(word) < 4 : continue                                 #no short words with less than 4 word
        counts[word] = counts.get(word,0) + 1

x = sorted(counts, key=counts.get, reverse=True)#sort with highest rank words to lowest
highest = None
lowest = None
for k in x[:100]:#we take only top 100 words
    if highest is None or highest < counts[k] :
        highest = counts[k]#43506
    if lowest is None or lowest > counts[k] :
        lowest = counts[k]#330
print('Range of counts:',highest,lowest)

# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20
fhand = open('gword.js','w')
fhand.write("gword = [")
first = True
for k in x[:100]:
    if not first : fhand.write( ",\n")
    first = False
    size = counts[k]
    size = (size - lowest) / float(highest - lowest)#1.0 - the highest; 0.00034 - third from the end; 0.0 and 0.0 the last words
    size = int((size * bigsize) + smallsize)#100 will be for the word SAKAI and 20 for the lowest words ->FONT SIZE
    fhand.write("{text: '"+k+"', size: "+str(size)+"}")
fhand.write( "\n];\n")
fhand.close()

print("Output written to gword.js")
print("Open gword.htm in a browser to see the vizualization")
