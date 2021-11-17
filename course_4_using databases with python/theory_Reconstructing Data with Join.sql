select Track.title, Genre.name from Track join Genre on Track.genre_id = Genre.id

#what we want to see
#the tables which hold the data
#how the tables are linked
select Track.title,	Artist.name, Album.title, Genre.name FROM
Track join Genre join Album join Artist on
Track.genre_id = Genre.id and
Track.album_id = Album.id and
Album.artist_id = Artist.id

#What is the purpose pf a primary key?
  #To look up a particular row in a table very quicky
  #?To point to a particular row in another table

#Which of the following is NOT a good rule to follow when developing a database model?
 #Use a person's email address as their primary key
 #?Model each "object" in the application as one or more tables

#If our user interface (i.e., like iTunes) has repeated strings on one column of the user interface, how should we model this properly in a database?
  #Make a table that maps the strings in the column to numbers and then use those numbers in the column
  #Put the string in the first row where it occurs and then put that row number in the column of all of the rest of the rows where the string occurs

#Which of the following is the label we give a column that the "outside world" uses to look up a particular row?
  #Logical key
  #?Primary key

#What is the label we give to a column that is an integer and used to point to a row in a different table?
  #Foreign key
  #?Logical key
  #?Primary key
  #Remote key
  #Local key

#What is the SQL keyword that reconnects rows that have foreign keys with the corresponding data in the table that the foreign key points to?
  #join
  #count

#What happens when you JOIN two tables together without an ON clause?
  #The number of rows you get is the number of rpws in the first table times the number of rows in the second table
  #You get all of the rows of the left table in the JOIN and NULLS in all of the columns of the right table
