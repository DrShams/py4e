#database
import sqlite3
conn = sqlite3.connect('mydictwords.sqlite')
cur = conn.cursor()
cur.executescript('''
CREATE TABLE IF NOT EXISTS Words
(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
docs_id INTEGER,
word TEXT UNIQUE,
title TEXT);

CREATE TABLE IF NOT EXISTS Docs
(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
docname TEXT UNIQUE)
''')
#docs_id = id
import urllib.request, urllib.parse, urllib.error
import json
import re
#fn = input('Enter Filename:')
#if len(fn) < 1:
fn = 'The Anatomy of a Search Engine.html'
fh = open(fn)
##Translating text (Basic)
import os
from google.cloud import translate_v2
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/mnt/c/Users/1/Desktop/py4e/course_5/TranslationAPI_unfinished/GoogleCloudKey_MyServiceAcct.json'
translate_client = translate_v2.Client()
target_1 = 'ru'#RUSSIAN
target_2 = 'es'#SECOND LANGUAGE

import ssl
#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#1 will check if that document was already extracted for new words at least one time
cur.execute('''INSERT OR IGNORE INTO Docs (docname)
    VALUES ( ? )''', ( fn, ) )
cur.execute('SELECT id FROM Docs WHERE docname = ? ', (fn, ))
docs_id = cur.fetchone()[0]

#2 open file and put new words
count = 0
for line in fh:
    line = line.rstrip()
    word_lst = re.findall('`([\w-]+)',line)#words or complicated-words
    if len(word_lst) == 0 :
        continue#no matches at all
    else:#if 1 or multiple words on the line
        for wordin_line in range(len(word_lst)):# starts with first words
            text = word_lst[wordin_line]        # and end with last word of the line
            cur.execute('SELECT docs_id,word FROM Words WHERE word = ?', (text, ))
            row = cur.fetchone()
            #if row is None:
            if row is not None:
                #docs_id = row[0]
                #print('word',text,'already in the table and has',docs_id,'docs_id')
                continue
            else:
                print(text)#+if time SLEEP 5 seconds
                result_1 = translate_client.translate(
                    text,
                    target_language=target_1
                )
                result_2 = translate_client.translate(
                    text,
                    target_language=target_2
                )
                #
                print("[ru]",result_1["translatedText"])
                print("[sp]",result_2["translatedText"])
                #
                title = '[ru]' + str(result_1["translatedText"]) + '\n[sp]' + str(result_2["translatedText"])
                #print(title)
                cur.execute('INSERT OR IGNORE INTO Words (docs_id,word,title) VALUES ( ?,?,? )', (docs_id, text, title) )
                conn.commit()
            count += 1# will not work if mark 2 words and after execute script!Fix LATER
            #check if there is connection if not it might be Temporary failure in name resolution'
if count == 0:
    print('the last word was',text)#the last word
else:
    print(count,'new words was added to the database')#the last word
#print('there is',count,'words to update')#the last word
