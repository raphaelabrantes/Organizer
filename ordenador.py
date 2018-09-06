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
			if (line[-3:].lower() == 'jpg' or line[-3:] == "mp4" or line[-3:] == "png") and "." in line:
				files.append("%s%s"%(path,line))
	
	os.system("rm nomescorretos.txt")
	return files


def save_name(name, file_n):
	with open(file_n, "a") as filename:
		filename.write("%s\n" %(name))


def check_and_save(files):
	saves = 0
	rejected = 0
	totais = 0
	for name in files:
		totais +=1
		name_l = name.lower()
		if ("(1)" not in name_l) and ("(2)" not in name_l) and ("(3)" not in name_l) and ("cópia" not in name_l) and ("_face" not in name_l):
			if (" 2.jpg" not in name_l) and (" 3.jpg" not in name_l) and (" 4.jpg" not in name_l) and (" 5.jpg" not in name_l) and ("_2.jpg" not in name_l):
				save_name(name,"nomes.txt")
				saves += 1
			else: 
				rejected +=1
				save_name(name, "rejected.txt")
		elif ("(1)" in name_l) or ("(2)" in name_l) or ("(3)" in name_l):
			if ("amiga" in name_l or "madri" in name_l):
				save_name(name,"nomes.txt")
				saves+= 1
			else:
				rejected += 1
				save_name(name, "rejected.txt")
		else:
			rejected += 1
			save_name(name, "rejected.txt")

	print("Salvadas : %d" %(saves))
	print("Rejeitadas: %d" %(rejected))
	print("Totais: %d" %(totais))


files = get_paths()
files.sort()
check_and_save(files)