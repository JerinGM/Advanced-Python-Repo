import sqlite3

# create a connection to a new database (if the database does not exist then it will be created).
db = sqlite3.connect("books-collection.db")
# Now running will create books-collection.db


# creating cursor
cursor = db.cursor()

# creating a db table
#
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) "
#                "NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# our db will have id, title, author and rating fields

# Downloaded db browser


# creating entry
cursor.execute("INSERT OR IGNORE INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
# NOW commenting previous line of code where I created DB and also close the db browser



