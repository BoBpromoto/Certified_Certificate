import os
#coding:utf8
#coding:cp949
import codecs
import pymysql

f = open("ip_zip_date.txt", "r") #ip address, date, time data
ip_str = f.readlines()

conn = pymysql.connect(host='localhost', user='root', password='root', db='victim_db', charset='utf8'); # Connect for use DataBase & set charset
																										# Because name written by Korean

curs = conn.cursor()
sql = "insert into victim_list(id, date, time, name, bank, account_no, ip_addr, location_nation) values (%s, %s, %s, %s, %s, %s, %s, %s)" #Create Query for transfer

for i in range (0, len(ip_str)) :
		ip_addr = ip_str[i].split(" ")[0]
		date = ip_str[i].split(" ")[1]
		div = ip_str[i].split(" ")[2].find("\n")
		time = ip_str[i].split(" ")[2][:div]
		#print "\n" + ip_addr + "\n" + date + "\n" + time
		s = codecs.open("cw0_un/"+ip_addr+"/signCert.cert", encoding="euc-kr") #Open unziped file, Parsing for name, account_number, bank, nation_info
		data = s.readlines()
		for j in range (0, 5) :
				if j==0 :
					div = data[0].split(",")[j].find("()")
					name = data[0].split(",")[j][3:div]
					account_no = data[0].split(",")[j][div+2:]
					#print name +" " +  account_no

				elif (j == 1) :
					div = data[0].split(",")[j].find("=")
					bank = data[0].split(",")[j][div+1:]			

				elif (j == 2) or (j == 3) :
					continue

				else:
					div = data[0].split(",")[j].find("=")
					location_nation = data[0].split(",")[j][div+1:]
					#print location_nation
#		print i+1
		curs.execute(sql,(i+1, date, time, name, bank, account_no, ip_addr, location_nation)) #Transfer Query
		conn.commit()
		s.close()
conn.close()
f.close()


