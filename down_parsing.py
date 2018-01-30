from bs4 import BeautifulSoup
import urllib2
import os

url = "http://fl0ckfl0ck.info"
str_r = urllib2.urlopen(url).readlines()
temp_list = str_r
f=open("1st_parsing.txt", "w")

for i in range (10, len(temp_list)-4) :
		data = temp_list[i][temp_list[i].find("zip"):temp_list[i].find("</a>")] +" "+ temp_list[i][temp_list[i].find("2017"):temp_list[i].find("</>")] + "\n"
		f.write(data)
f.close()

s = open("1st_parsing.txt", "r")
t = open("ip_zip_date4down.txt", "w")
p = open("ip_zip_date.txt", "w")
line = s.readlines()
for i in range(0, len(line)) :
		data_1 = line[i][5:line[i].find(" ")+17] + "\n"
		t.write(data_1)
		p.write(data_1)
p.close()
t.close()
s.close()

os.system("find . -name \"ip_zip_date.txt\" -exec perl -pi -e\'s/.zip//g\' {} \;")

x = open("ip_zip_date4down.txt", "r")
zipline = x.readlines()
for i in range(0,len(zipline)) :
		href = zipline[i].split(" ")[0]
		os.system("wget -P ./cw0 http://fl0ckfl0ck.info/" + href)
x.close()

