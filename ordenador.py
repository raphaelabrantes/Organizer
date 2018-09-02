import os
os.system("ls -R > nomescorretos.txt")
with open("nomescorretos.txt", "r") as filename:
	lines = filename.readlines()

files = []
path = ""
lines = [line.strip() for line in lines]
for line in lines:
	if line == ".:" or line == "":
		pass
	elif "./" in line:
		path = line[1:]
		path = path[: len(path) -1] + "/"
		pass
	else:
		if line[-1].lower() != 'g' and line[-1] != "4":
			pass
		elif (line[-1].lower() == 'g' or line[-1] == "4") and "." in line:
			files.append("%s%s"%(path,line))
for i in files:
	os.system("file %s"%(i))

os.system("rm nomescorretos.txt")


    
