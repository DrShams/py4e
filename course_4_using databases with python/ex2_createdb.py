import sqlite3

conn = sqlite3.connect('ex_ages_db.sqlite')
    #create emaildb.sqlite here on the folder
cur = conn.cursor()
    #
cur.execute('''
DROP TABLE IF EXISTS Ages''')
    #delete whole table if exists
cur.execute('''
CREATE TABLE Ages (name VARCHAR(128), age INTEGER)''')
cur.execute('DELETE FROM Ages')
    #erase all info insife table
row = cur.fetchone()#information that we get from database
val = [
    ('Madisyn', 40),
    ('Kevyn', 35),
    ('Jackson', 15),
    ('Kean', 30),
    ('Lorena', 13)
]
if row is None:
    sql = ('INSERT INTO Ages (name, age) VALUES (?, ?)')
    cur.executemany(sql, val)
    #add '?' - is a placeholder, we do not allow SQL injection by putting this question mark
        # INSERT INTO Counts (email, count) VALUES (?, 1)''', (email,))
else:
    #cur.executemany('UPDATE Ages SET age = age WHERE name = ?', (val,))
    print("There is no data")
conn.commit()#write all of the stuff to disk

sqlstr = 'SELECT hex(name || age) AS X FROM Ages ORDER BY X'
for row in cur.execute(sqlstr):#<class 'sqlite3.Cursor'> #<sqlite3.Cursor object at 0x7f6786ab8b90>
    #<class 'tuple'>
    print(row[0])#4A61636B736F6E3135
    break
cur.close()
