#-*- coding:utf-8 –*-

# chinese.py
import sqlite3,sys
def update(a,b):

	conn = sqlite3.connect('sayHello.db')
	c = conn.cursor()
	c.execute("UPDATE COMPANY set 学院 = '%s' where 学号='%s'" %(b,a))
	conn.commit()
	
	cursor = conn.execute("SELECT 姓名,学号,性别,年龄,学院  from COMPANY")
	for row in cursor:
		print ("姓名 = "+str(row[0]))
		print ("学号= "+str(row[1]))
		print ("性别= "+str(row[2]))
		print ("年龄= "+str(row[3]))
		print ("学院 = "+str(row[4])),"\n"
	return "Operation done successfully"
	conn.close()
if '__main__' == __name__:
	if 3 == len(sys.argv):
		args = sys.argv
		update(args[1], args[2])


