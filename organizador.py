import os, time, shutil


class Organizer:
    def __init__(self, base, new_path=""):
        self.path = base
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
                #print("Matching pattern: ", file)
                self.files.append(file)

    def verifyPatern(self, file, nots =None, musts=None):
        """
                Verifica se o arquivo esta de acordo com as regras ditadas pelo usuario
                A variavel nots é uma lista de coisas que o arquivo nao pode conter no nome,
                A variavel musts é uma lista de coisas que o arquivo pode conter (deve conter pelo menos uma)
                retorna True ou False dependendo das comparacoes

        """
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
        print("Organizando Arquivos")
        contador = 0
        dict_compare = {}
        for i in self.files:
            contador += 1
            x = os.stat(i)
            size = x.st_size
            tempo = time.localtime(x.st_mtime)
            month = str(tempo.tm_mon)
            year = str(tempo.tm_year)
            #hour = str(tempo.tm_hour)
            #minute = str(tempo.tm_min)
            #second = str(tempo.tm_sec)
            repartition = i.rpartition("/")[-1]
            path = "%s/%s-%s/%s" % (self.new_path, year, month, repartition)
            if path in dict_compare.keys():
                if size > dict_compare[path][1]:
                    dict_compare[path] = [i, size]
            else:
                dict_compare[path] = [i, size]

        return dict_compare

    # copia os arquivos os arquivos para o path novo
    def moveEm(self):
        new_paths = self.organize()
        self.generateDirectories(new_paths)
        contador = 0
        size = len(new_paths)
        for key, value in new_paths.items():
            print("Moving %s" % (value[0]))
            shutil.copy2(value[0], key)
            contador += 1
            print("%.2f Done" % ((contador/size) * 100))

    def generateDirectories(self, path):
        print("Criando diretorios")
        for new in path.keys():
            direct = new[:new.find("/", new.find("/") + 1) + 1]
            os.makedirs(direct, exist_ok=True)






# argumentos que ajudam:
# os.listdir(path)
# os.path.isfile(path)
# os.path.isdir(path)
# isinstance(obj, type)
