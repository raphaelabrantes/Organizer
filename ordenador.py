import os
def get_paths():
	os.system("ls -R > nomescorretos.txt")
	with open("nomescorretos.txt", "r") as filename:
		lines = filename.readlines()
	files = []
	path = os.getcwd() + "/"
	lines = [line.strip() for line in lines]
	for line in lines:
		if line == ".:" or line == "":
			pass
		elif "./" in line:
			path = os.getcwd()
			path += line[1:]
			path = path[: len(path) -1] + "/"
		else:
			if line[-1].lower() != 'g' and line[-1] != "4":
				pass
			elif (line[-1].lower() == 'g' or line[-1] == "4") and "." in line:
				files.append("%s%s"%(path,line))
	os.system("rm nomescorretos.txt")
	return files


	
files = get_paths()
for i in files:
	with open("nomes.txt", "a") as filename:
		filename.write("%s\n" %(i))

	
	