import os, time, shutil


class Organizer:
    def __init__(self,base, new_path= ""):
        self.path = base
        self.new_path = new_path
        self.directory = self.getDictories()
        self.files = []

    def __len__(self):
        return len(self.files)

    def getDictories(self):
        directory = []
        list_all = [self.path]
        for elemento in list_all:
            if os.path.isdir(elemento):
                directory.append(elemento)
                for inside in os.listdir(elemento):
                    list_all.append(elemento + inside + "/")
        return directory

    def getFiles(self, nots= None, musts=None):
        files = [str + file for str in self.directory for file in os.listdir(str) if os.path.isfile(str + file)]
        for file in files:
            if self.verifyPatern(file,nots, musts):
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
        dict_compare = {}
        for i in self.files:
            x = os.stat(i)
            tempo = time.localtime(x.st_mtime)
            month = str(tempo.tm_mon)
            year = str(tempo.tm_year)
            hour = str(tempo.tm_hour)
            minute = str(tempo.tm_min)
            second = str(tempo.tm_sec)
            repartition = i.rpartition("/")[-1]
            path = "%s/%s-%s/%s" %(self.new_path, year, month, repartition)
            if path in dict_compare.keys():
                if hour < dict_compare[path][1]:
                    dict_compare[path] = [i, hour, minute, second]
                elif hour == dict_compare[path][1] and minute < dict_compare[path][2]:
                    dict_compare[path] = [i, hour, minute, second]
                elif hour == dict_compare[path][1] and minute == dict_compare[path][2] and second < dict_compare[path][3]:
                    dict_compare[path] = [i, hour, minute, second]
            else:
                dict_compare[path] = [i, hour, minute, second]

        return dict_compare

    # copia os arquivos os arquivos para o path novo
    def moveEm(self):
        new_paths = self.organize()
        self.generateDirectories(new_paths)
        for key, value in new_paths.items():
            print("Moving %s"%(value[0]))
            shutil.copy2(value[0], key)

    def generateDirectories(self, path):
        for new in path.keys():
            direct = new[:new.find("/", new.find("/") + 1) + 1]
            os.makedirs(direct, exist_ok=True)






# argumentos que ajudam:
# os.listdir(path)
# os.path.isfile(path)
# os.path.isdir(path)
# isinstance(obj, type)
