import os, time, shutil
from PIL import Image


class Organizer:
    def __init__(self, base, new_path="", mod_path=""):
        self.path = base
        self.mod_path = mod_path
        self.new_path = new_path
        self.directory = self.getDictories()
        self.files = []

    def __len__(self):
        return len(self.files)

    def getDictories(self):
        print("Getting all diretorys")
        directory = []
        list_all = [self.path]
        for elemento in list_all:
            if os.path.isdir(elemento):
                directory.append(elemento)
                for inside in os.listdir(elemento):
                    list_all.append(elemento + inside + "/")
        print("Done")
        return directory

    def getFiles(self, nots= None, musts=None):
        print("Getting all Files")
        files = [string + file for string in self.directory for file in os.listdir(string) if os.path.isfile(string + file)]
        print("Done")
        for file in files:
            if self.verifyPatern(file, nots, musts):
                self.files.append(file)

    def verifyPatern(self, file, nots =None, musts=None):
        if nots is None and musts is None:
            return True

        elif nots is not None and musts is not None:
            for negative in nots:
                if negative in file:
                    return False

            flag = False
            for positive in musts:
                if positive in file:
                    flag = True
            return flag

        elif nots is None:
            flag = False
            for positive in musts:
                if positive in file:
                    flag = True
            return flag

        elif musts is None:
            for negative in nots:
                if negative in file:
                    return False
            return True

    # organiza paths
    def organize(self):
        print("Organizing Files")
        contador = 100
        dict_compare = {}
        for i in self.files:
            try:
                image = Image.open(i)._getexif()[36867]
                split = image.split(":")
                year = split[0]
                month = split[1]
                new_path = self.new_path
                print("NEW TAKEN", end="-\t\t")
            except(KeyError, OSError, TypeError, IndexError):
                print("NO TAKEN DATE", end="-\t\t")
                x = os.stat(i)
                tempo = time.localtime(x.st_mtime)
                month = str(tempo.tm_mon)
                year = str(tempo.tm_year)
                new_path = self.mod_path
            repartition = i.rpartition("/")[-1]
            path = "%s/%s-%s/%s" % (new_path, year, month, repartition)
            print(path)
            if path in dict_compare.keys():
                ponto = path.find(".")
                path = path[:ponto] + str(contador) + path[ponto:]
                contador += 1

            dict_compare[path] = i

        return dict_compare

    # copia os arquivos os arquivos para o path novo
    def moveEm(self):
        new_paths = self.organize()
        self.generateDirectories(new_paths)
        contador = 0
        size = len(new_paths)
        for key, value in new_paths.items():
            print("Moving %s" % (value))
            shutil.copy2(value, key)
            contador += 1
            print("%.2f Done" % ((contador/size) * 100))                                                                                                                                                

    def generateDirectories(self, path):
        print("Creating Directories")
        for new in path.keys():
            direct = new[:new.find("/", new.find("/") + 1) + 1]
            os.makedirs(direct, exist_ok=True)
            print("%s created" % direct)





# argumentos que ajudam:
# os.listdir(path)
# os.path.isfile(path)
# os.path.isdir(path)
# isinstance(obj, type)
