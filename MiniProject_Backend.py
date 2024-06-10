import sqlite3

def connect():
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY, 
        Movie_ID TEXT, 
        Movie_Name TEXT, 
        Release_Date TEXT, 
        Director TEXT, 
        Cast TEXT, 
        Budget TEXT, 
        Duration TEXT, 
        Rating TEXT
    )
    """)
    conn.commit()
    conn.close()

def AddMovieRec(Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating):
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?,?,?,?,?)", 
                (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating))
    conn.commit()
    conn.close()

def ViewMovieData():
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def DeleteMovieRec(id):
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE Movie_ID=?", (id,))
    conn.commit()
    conn.close()
