#encoding=utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import MySQLdb
import time
import urllib
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf8')

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='********',
        db ='jwc2',
		charset='utf8'
        )   
cur = conn.cursor()
username = raw_input("账号")
password = raw_input("密码")
driver = webdriver.PhantomJS();
driver.get("http://jwc2.yangtzeu.edu.cn:8080/login.aspx")
driver.find_element_by_name('txtUid').send_keys(username)
driver.find_element_by_name('txtPwd').send_keys(password)
driver.find_element_by_id('btLogin').click()
cookie=driver.get_cookies()
driver.get("http://jwc2.yangtzeu.edu.cn:8080/cjcx.aspx")
js = "document.getElementById('btAllcj').removeAttribute('onclick');document.getElementById('btAllcj').setAttribute('type', 'submit');"
driver.execute_script(js)
driver.find_element_by_name("btAllcj").click()
html=driver.page_source
#html = open("btAllcj.html","r")
soup = BeautifulSoup(html,"lxml")
Sno = str(soup.find(id="lbXH").getText())
Sname = str(soup.find(id="lbXm").getText())
Sdept =  str(soup.find(id="lbBj").getText())
Student = (Sno,Sname,Sdept,'12345678')
sql = "insert into cjcx_student values(%s,%s,%s,%s)" 
cur.execute(sql,Student)
#id = 0
tables = soup.findAll("table")
for tab in tables[1:2]:
    for tr in tab.findAll("tr")[1:]:
		count = 0
		for td in tr.findAll("td"):
			count += 1
			if count==1:
				Cname = td.getText()
			if count==2:
				Grade = td.getText()
				num = cur.execute("select * from cjcx_sc")
				id = num + 1
				sql = "insert into cjcx_sc values(%s,%s,%s,%s)"
				SC = (id,Sno,Cname,Grade)
				cur.execute(sql,SC)
			if count==3:
				Credit = td.getText()
				sql = "select count(*) from cjcx_course where Cname=%s and Credit=%s"
				Course = (Cname,Credit)
				cur.execute(sql,Course)
				Cn = cur.fetchall()
				for cname in Cn:
					cname  = cname[0]
				if cname == 0:
					sql = "insert into cjcx_course values(%s,%s)"
					Course = (Cname,Credit)
					cur.execute(sql,Course)
				else:
					continue
conn.commit()
cur.close()
conn.close()
