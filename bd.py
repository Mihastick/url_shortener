import sqlite3 as sql

con = sql.connect('url.db')
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS 'users' ('name' VARCHAR, 'password' BLOB, 'email' VARCHAR PRIMARY KEY)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS 'urls' ('id' INTEGER PRIMARY KEY, 'url_name' VARCHAR, 'short_url' VARCHAR, 'user_email' INTEGER, 'count' INTEGER)")
    con.commit()