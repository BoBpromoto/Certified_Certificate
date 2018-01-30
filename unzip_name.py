import os
import zipfile

f = open("ip_zip_date.txt", "r")
filename = f.readlines()

for i in range (0, len(filename)) :
		name = filename[i].split(" ")[0]
		os.system("unzip ./cw0/"+ name + " -d ./cw0_un/"+name);
		print name
	
f.close()
