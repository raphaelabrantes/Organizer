import os
os.system("ls -R > nomescorretos.txt")
with open("nomescorretos.txt", "w") as filename:
    lines = filename.readlines()

files = []

lines = [line.strip() for line in lines]
for line in lines:
    if line == ".:" or line == "":
        pass
    elif line[:1] == "./":
        path = line
    else:
        if line[-1].lower != "g" or "." not in line:
            pass
        else:
            file.append("%s%s"%(path,line))
for i in file:
    print(i)

    
