#encoding=utf-8
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')
conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='211599100yxz',
        db ='jwc2',
        charset='utf8'
		)
cur = conn.cursor()
try:
#	cur.execute("select count(*) from cjcx_course where Cname='会计学原理'")
#	Cname = cur.fetchall()
#	for cname in Cname:
#		cname = cname[0]
#		print cname
#		conn.commit()
#	name = '123'
#	Credit =  "3.5"
#	sql = ("select count(*) from cjcx_course where Cname=%s and Credit=%s")
#	course = (name,Credit)
#	cur.execute(sql,course)
#	Cname = cur.fetchall()
#	for cname in Cname:
#		cname = cname[0]
#		print cname
#	if cname == 0: 
#		sql = "insert into cjcx_course values(%s,%s)"
#		Course = (name, Credit)
#		cur.execute(sql,Course)
	cur.execute("select * from cjcx_course")
	Course = cur.fetchall()
	for course in Course:
		print course[0]
		conn.commit()
except Exception,ex:
	print ex
finally:
	cur.close()
	conn.close()
