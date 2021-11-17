import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

#executescript
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    #fname = 'roster_data_sample.json'
    fname = 'roster_data.json'
# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    #entry a row from many lists
    name = entry[0];# "Charley",
    title = entry[1];# "si110",
    role = entry[2];# "1" means INSTRUCTOR if it where "0" it will be STUDENT

    #print((name, title, role))
    #OR IGNORE - if we insert the name twice - nothing happens
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]
    #OR REPLACE if the combination is already there it will UPDATE
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ?)''',
        ( user_id, course_id, role) )

    conn.commit()

th_str = '''SELECT User.name, Member.role, Course.title
FROM User JOIN Member JOIN Course
ON Member.user_id = User.id AND Member.course_id = Course.id
ORDER BY Course.title, Member.role DESC, USER.name ASC
'''

ex_str = '''SELECT User.name,Course.title, Member.role FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2'''

for row in cur.execute(ex_str):
    print(row[0], row[1], row[2])#User.name, Member.role, Course.title

hex_str = '''SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1'''
cur.execute(hex_str)
row = cur.fetchone()[0]
print(row)

#In the following Python code sequence (assuming cur is a SQLite cursor object),
#cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
#row = cur.fetchone()
    #???None
    #an empty list
#What do we generally avoid in a many-to-many junction table?
