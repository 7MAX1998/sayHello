#-*- coding:utf-8 –*-

# chinese.py
import sqlite3,sys
def delete(x):
	conn = sqlite3.connect('sayHello.db')
	c = conn.cursor()
	print ("Opened database successfully")
	c.execute("DELETE from COMPANY where 学号 = '%s'"  %x)
	conn.commit()
	print (("Total number of rows deleted :"), conn.total_changes)
	cursor = conn.execute("SELECT 姓名,学号,性别,年龄,学院  from COMPANY")
	for row in cursor:
		print ("姓名 = "+str(row[0]))
		print ("学号= "+str(row[1]))
		print ("性别= "+str(row[2]))
		print ("年龄= "+str(row[3]))
		print ("学院 = "+str(row[4])),"\n"
	return "Operation done successfully"
if '__main__' == __name__:
	if 2 == len(sys.argv):
		args = sys.argv
		delete(args[1])

