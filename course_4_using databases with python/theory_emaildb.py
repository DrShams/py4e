import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
    #create emaildb.sqlite here on the folder
cur = conn.cursor()
    #
cur.execute('''
DROP TABLE IF EXISTS Counts''')
    #
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')
    #
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]#grab emails from te file

#dictionary part
    cur.execute('''
SELECT count FROM Counts WHERE email = ? ''', (email,))
    # cur.execute is not retrieving the data
    # '?' - is a placeholder, we do not allow SQL injection by putting this question mark
    # (email,) -it's a tupple
    row = cur.fetchone()
    # row - information that we get from database
    if row is None:
        cur.execute('''
INSERT INTO Counts (email, count) VALUES (?, 1)''', (email,))
    #INSERT INTO Counts (email, count) VALUES (?)''', (email,1))
    #why we couldn't do that?
    else:
        cur.execute('''
UPDATE Counts SET count = count + 1 WHERE email = ?''', (email,))
    conn.commit()#write all of the stuff to disk

#https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
            #<class 'sqlite3.Cursor'>
            #<sqlite3.Cursor object at 0x7f6786ab8b90>
    #('cwen@iupui.edu', 5)
    #<class 'tuple'>
    print(str(row[0]), row[1])
#"emaildb.py" 34, 942C
cur.close()

#In a typical online production environment, who has direct access to the production database?
    #Database Administrator
#What happens if a DELETE command is run on a table without a WHERE clause?
    #All the rows in the table are deleted
    #DELETE FROM "main"."Counts" WHERE _rowid_ IN ('11');
    #DELETE FROM "main"."Counts"
