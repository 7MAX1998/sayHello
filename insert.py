#-*- coding:utf-8 –*-

# chinese.py

import sqlite3, sys

def insert(a, b, c, d, e ):
	conn = sqlite3.connect('sayHello.db')
	c = conn.cursor()
	c.execute("INSERT INTO COMPANY (姓名,学号,性别,年龄,学院) \
                 VALUES ('%s', '%s', '%s', '%s', '%s' )" % (a, b, c, d, e));
	conn.commit()
	c = conn.cursor()
	cursor = c.execute("SELECT 姓名,学号,性别,年龄,学院  from COMPANY")
	values= cursor.fetchall()
	for row in values:
		print ("姓名 = "+str(row[0]))
		print ("学号= "+str(row[1]))
		print ("性别= "+str(row[2]))
		print ("年龄= "+str(row[3]))
		print ("学院 = "+str(row[4])), "\n";
	return "Operation done successfully";
	
if '__main__' == __name__:
	if 6 == len(sys.argv):
		args = sys.argv
		insert(args[1], args[2], args[3], args[4], args[5])


