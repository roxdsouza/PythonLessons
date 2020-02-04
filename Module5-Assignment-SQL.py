# More information on SQlite database at:
# https://www.tutorialspoint.com/sqlite/sqlite_python.htm
# https://docs.python.org/2/library/sqlite3.html

#import sqlite3

# # Solution 1
# con = sqlite3.connect('test.db')
# con.execute('''create table versions(APPNAME key NOT NULL, VERSION key NOT NULL);''')
# con.execute("insert into versions(APPNAME, VERSION) values ('SQlite3', '2.6.0')")
# with con:
#     cur = con.cursor()
#     cur.execute('SELECT VERSION from versions where APPNAME = "SQlite3"')
#     data = cur.fetchone()
#     print "SQLite version: %s" % data
#
# con.execute("drop table versions")
# con.close()
#
###########################################################################

# #Solution 2
# con = sqlite3.connect('new_db')
# with con:
#     cur = con.cursor()
#     cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
#     cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
#     cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
#     cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
#     cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")
#     con.commit()
#
# print "The last Id of the inserted row is %d" %cur.lastrowid
# con.execute("drop table Friends")
# con.close()
#
###########################################################################
# import os
#
# db_filename = 'todo.db'
# db_is_new = not os.path.exists(db_filename)
# conn = sqlite3.connect(db_filename)
# if db_is_new:
#     print 'Need to create schema'
#     print 'Creating database'
# else:
#     print 'Database exists, assume schema does, too.'
# conn.close()
#
###########################################################################

# import sqlite3 as lite
# import sys
# con = lite.connect('test.db')
# with con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM Cars")
#     for colinfo in cur.fetchall():
#         print colinfo
#
# con.close()
#
###########################################################################

# import sqlite3 as lite
#
# cars = (
#     (1, 'Audi', 52642),
#     (2, 'Mercedes', 57127),
#     (3, 'Skoda', 9000),
#     (4, 'Volvo', 29000),
#     (5, 'Bentley', 350000),
#     (6, 'Hummer', 41400),
#     (7, 'Volkswagen', 21600)
# )
#
# con = lite.connect('test.db')
# with con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE IF EXISTS Cars")
#     cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
#     for value in cars:
#         cur.execute("INSERT INTO Cars VALUES(?, ?, ?)", value)
#
###########################################################################

# import sqlite3 as lite
# con = lite.connect('test.db')
# with con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM Cars")
#     rows = cur.fetchall()
#     for row in rows:
#         print row
#
###########################################################################
#
# import sqlite3 as lite
# con = lite.connect('test.db')
# with con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM Cars")
#     rows = cur.fetchall()
#     for row in rows:
#         print "%s %s %s" %(row[0], row[1], row[2])
#
###########################################################################
#
# import sqlite3 as lite
# import sys
# uId = 1
# uPrice = 62300
# con = lite.connect('test.db')
# with con:
#     cur = con.cursor()
#     cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))
#     con.commit()
#     print "Number of rows updated: %d" %cur.rowcount
#
###########################################################################

# import sqlite3 as lite
# con = lite.connect('test.db')
# with con:
#     cur = con.cursor()
#     cur.execute('PRAGMA table_info(Cars);')
#     data = cur.fetchall()
#     for d in data:
#         print d[0], d[1], d[2]
#
###########################################################################

# import sqlite3 as lite
# con = lite.connect('test.db')
# with con:
#     cur = con.cursor()
#     cur.execute('SELECT * FROM Cars')
#     col_names = [cn[0] for cn in cur.description]
#     rows = cur.fetchall()
#     print "%s %-10s %s" % (col_names[0], col_names[1], col_names[2])
#     for row in rows:
#         print "%2s %-10s %s" %row
#
###########################################################################

import csv, sqlite3 as lite

con = lite.connect('store-info.db')
cur = con.cursor()
cur.execute("CREATE TABLE STORE(ID INTEGER PRIMARY KEY, NAME TEXT, CITY TEXT, STATE TEXT, COUNTRY TEXT);")

with open('sample-storedata.csv','rb') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['ID'], i['Store-Name'], i['Store-City'], i['Store-State'], i['Store-Country']) for i in dr]

cur.executemany("INSERT INTO STORE(ID, NAME, CITY, STATE, COUNTRY) VALUES (?, ?, ?, ?, ?);", to_db)
con.commit()
with con:
    cur = con.cursor()
    cur.execute('SELECT * FROM STORE')
    col_names = [cn[0] for cn in cur.description]
    rows = cur.fetchall()
    print "%s %-15s %-15s %-15s %-15s" %(col_names[0], col_names[1], col_names[2], col_names[3], col_names[4])
    for row in rows:
        print "%s %-15s %-15s %-15s %-15s" %row

con.close()
