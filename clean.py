from organizador import *

#list of things the file must have in the name THIS IS OBLIGATORY
must = ['JPG', 'jpeg', 'MOV', 'png', 'm2ts', 'AVI', 'MTS', 'jpg', 'PNG', 'mov', 'mp4']

#list of things that will discart the file from being copied
nots = ['.css', '.doc', '.exe']

#path of files you want to organize
orginals = "PATH/TO/FILES"

#path to where they gonna be copied to if they pass the filters
new_path = "NEW/PATH/"

#path to where they gonna be copied if they pass the filters but dont have a taken day
no_taken = "PATH/PHOTOS/WITHOUT/TAKEN/DAY"

#generates folder in memory
folder = Organizer(orginals, new_path, no_taken)

#pass all files truth the filter
folder.getFiles(nots, must)

#move photos to new place
folder.moveEm()

