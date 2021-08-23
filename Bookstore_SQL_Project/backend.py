import sqlite3

def connect():
   #Opens a connection to a local .db file
   conn = sqlite3.connect("books.db")
   #Creates a cursor object to interact w/ the .db
   cur=conn.cursor()

   #Creates a 'book' table that will hold the columns "id", "title", "author", "year", "isbn"
   cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")

   #Commits changes to the .db and closes the connection
   conn.commit()
   conn.close()

#Creates a new row in the table with the parameters given
def insert(title, author, year, isbn):
   #Opens a connection to a local .db file
   conn = sqlite3.connect("books.db")

   #Creates a cursor object to interact w/ the .db
   cur=conn.cursor() 
   cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title,author,year,isbn))

   #Commits changes to the .db and closes the connection
   conn.commit()
   conn.close()

#Returns a list with all rows in the .db
def view():
   #Opens a connection to a local .db file
   conn = sqlite3.connect("books.db")

   #Creates a cursor object to interact w/ the .db
   cur=conn.cursor() 
   cur.execute("SELECT * FROM book")

   #fetches all rows held in the cursor object as a list
   rows = cur.fetchall()
   conn.close()
   return rows

#Searches the .db for rows matching given parameters and returns found rows as a list
def search(title = "", author = "", year = "", isbn = ""):
   #Opens a connection to a local .db file
   conn = sqlite3.connect("books.db")
   #Creates a cursor object to interact w/ the .db
   cur=conn.cursor() 
   cur.execute("SELECT * FROM book WHERE title = ? OR autor = ?, or year = ?, or isbn = ?", (title,author,year,isbn))

   #fetches all rows held in the cursor object as a list, closes connection to .db
   rows=cur.fetchall()
   conn.close()
   return rows

#Deletes a row in the .db by the unique id parameter
def delete(id):
   #Opens a connection to a local .db file
   conn = sqlite3.connect("books.db")

   #Creates a cursor object to interact w/ the .db
   cur=conn.cursor() 
   cur.execute("DELETE FROM book WHERE id = ?", (id,))

   #Commits changes to the .db and closes the connection
   conn.commit()
   conn.close()

#Updates a unique row in the .db identfied with the id parameter
def update(id, title, author, year, isbn):
   #Opens a connection to a local .db file
   conn = sqlite3.connect("books.db")

   #Creates a cursor object to interact w/ the .db
   cur=conn.cursor()
   cur.execute("UPDATE book SET title=?, author =?, year=?, isbn=? WHERE id=?", (title,author,year,isbn, id))

   #Commits changes to the .db and closes the connection
   conn.commit()
   conn.close()