import sqlite3
import os


def connect():
    ''' Create a database if not existed and make a connection to it.
    
    '''
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data1 (id Integer PRIMARY KEY, book TEXT, author TEXT, price INTEGER, rating REAL)")
    conn.commit()
    conn.close()

def insert(book,author,price,rating):
    ''' insertion function to insert a new book to the database.
    
        Arguments
        ---------
        book: str, Book Name.
        author: str, Author Name.
        price: int, Price of Book.
        rating: float, Rating of the book.
    '''
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO data1 Values (NULL,?,?,?,?)",(book,author,price,rating))
    conn.commit()
    conn.close()

def view():
    ''' view function to show the content of the database 
        which is the books data.
        returns the content of the database.
    '''
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data1")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(book="",author="",price="",rating=""):
    ''' search function to search for a specific book in the database.
        returns the content of the database.
    
        Arguments
        ---------
        book: str, Book Name.
        author: str, Author Name.
        price: int, Price of Book.
        rating: float, Rating of the book.
    '''
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("Select * FROM data1 WHERE book=? or author=? or price=? or rating=?",(book,author,price,rating))
    rows = cur.fetchall()
    conn.close()
    return(rows)

def delete(id):
    ''' delete function to delete a specific book from the database.
    
        Arguments
        ---------
        id: int, id of the book in the database.
    '''
    conn = sqlite3.connect("Books.db")
    cur  = conn.cursor()
    cur.execute("DELETE FROM data1 WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,book,author,price,rating):
    ''' update function to update the data of a specific book in the database
        by their id.
    
        Arguments
        ---------
        id: int, id of the book in the database.
        book: str, Book Name.
        author: str, Author Name.
        price: int, Price of Book.
        rating: float, Rating of the book.
    '''
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("UPDATE data1 SET book=?, author=?, price=?, rating=? WHERE id=?",(book,author,price,rating,id))
    conn.commit()
    conn.close()

def delete_data():
    ''' delete_data function is to delete the database.
    
    '''
    if os.path.exists("Books.db"):
        os.remove("Books.db")
    connect()

connect()
