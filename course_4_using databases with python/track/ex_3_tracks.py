import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):#d = entry
    found = False
    for child in d:
    #<key>Track ID</key><integer>369</integer>
        if found :
            return child.text#369
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)#<xml.etree.ElementTree.ElementTree object at 0x7f4be34648e0>
all = stuff.findall('dict/dict/dict')#the list with the dictionaries
#print('Dict count:', len(all))
for entry in all:#the first elemet <Element 'dict' at 0x7fbe1f6f5a40>
    if ( lookup(entry, 'Track ID') is None ) :
        continue
    name = lookup(entry, 'Name')#1
    artist = lookup(entry, 'Artist')#2
    album = lookup(entry, 'Album')#3
    genre = lookup(entry, 'Genre')#4
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None or genre is None:
        continue

    #print(name, artist, album, count, rating, length)
    #INSERT OR IGNORE
    #id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        #if an 'id' exists inside SQL it will be AUTOINCREMENTed but not added
    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
        #if ( artist )
            #sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 5 supplied.
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?, ?)''',
        ( name, album_id, genre_id, length, rating, count, ) )
###MAKE THE ORDER
sqlcursor = cur.execute('''SELECT * FROM Track ORDER BY "title" ASC''')
track_list = list()
for tup_line in sqlcursor:
    track_list.append(tup_line[1:])
cur.executescript('''
DROP TABLE IF EXISTS Track;
CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER);
    ''')
sql = ('''INSERT OR REPLACE INTO Track
    (title, album_id, genre_id, len, rating, count)
    VALUES ( ?, ?, ?, ?, ?, ?)''')
cur.executemany(sql, track_list)

print(track_list[0][0])
#print(track_list)
    #cur.execute('''
    #UPDATE Track
    #SET (title, album_id, genre_id, len, rating, count)
    #VALUES ( ?, ?, ?, ?, ?, ?)''',
    #( name, album_id, genre_id, length, rating, count, ) )
conn.commit()
cur.close()
#cur.execute('''
#SELECT Track.title, Artist.name, Album.title, Genre.name
#FROM Track JOIN Genre JOIN Album JOIN Artist ON Track.genre_id = Genre.ID and Track.album_id = Album.id AND Album.artist_id = Artist.id
#ORDER BY Artist.name LIMIT 3''')
#print(cur.fetchone()[0])
