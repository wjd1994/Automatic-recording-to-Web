import sqlite3
db = sqlite3.connect('test.db')
cur = db.cursor()
cur.execute("create table text(id integer auto_increment,tx text,tm text,A text,B text,C text,D text,E text,F text,da text,nd integer,primary key(id))")
#cur.execute("drop table text")
print('ok')
cur.close()
db.close()
