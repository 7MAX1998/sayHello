#-*- coding:utf-8 –*-

# chinese.py
import sqlite3
conn = sqlite3.connect('sayHello.db')
c = conn.cursor()
c.execute('''CREATE TABLE COMPANY
       (姓名  TEXT      NOT NULL,
	学号  STRING PRIMARY KEY     NOT NULL,
	性别  TEXT     NOT NULL,	
        年龄  INT     NOT NULL,
        学院  TEXT     NOT NULL
    );''')
print ("Table created successfully")
conn.commit()
conn.close()
