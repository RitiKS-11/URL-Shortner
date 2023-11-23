import random
import string
import sqlite3

def shorten_url(length=6):
    letters = string.ascii_lowercase + string.digits
    short_url = ""
    
    for _ in range(length):
        short_url += "".join(random.choice(letters))

    return short_url

def connect_database():
    db = sqlite3.connect("database.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS shortner( \
                   url varchar, \
                   short_url varchar)")
    
    cursor.close()
    return db


def insert_data(url, short_url):
    
    db = connect_database()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM link_table WHERE link_table.url = ?;", (str(url), ))
    result = cursor.fetchone()

    if result:
        url, short_url = result
    else:
        cursor.execute("INSERT INTO link_table (url, short_url) VALUES (?, ?)", (url, short_url))
        db.commit()

    cursor.close()
    db.close()

    return short_url
    
def get_data(shorten_url):
    db = connect_database()
    cursor = db.cursor()
    cursor.execute("SELECT url FROM link_table WHERE link_table.short_url = ?;", (str(shorten_url), ))

    result =  cursor.fetchone()
    print(result)


    return result[0]
    
if __name__ == "__main__":
    shorten_url()