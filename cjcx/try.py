#encoding=utf-8
import MySQLdb

conn = MySQLdb.connect(
		host='localhost',
		port='3306',
		user='root',
		passwd='211599100yxz',
		db='jwc2',
		charset='utf8'
		) 
cur = conn.cursor()
try:
	sql = "insert into cjcx_course values(%s,%s)"
	Course = ('会学原理','3.5')
	cur.execute(sql,Course)
except Exception,ex:
	print ex
finally:
	conn.commit()
	cur.close()
	conn.close()
