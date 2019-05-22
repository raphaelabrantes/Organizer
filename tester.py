from organizador import *

must = ['JPG', 'jpeg', 'MOV', 'png', 'm2ts', 'AVI', 'MTS', 'jpg', 'PNG', 'mov', 'mp4']
nots = ["(1)","(2)", "(3)","cópia","_face"," 2.jpg", " 3.jpg"," 4.jpg"," 5.jpg", "_2.jpg", ".bmp", '.css', '.doc', '.exe',
        '.gif', '.ini','.ncx', '.opf', '.pdf', '.pps', '.ppt', '.txt', '.wav', '.xls', '.xml', '.zip', 'bers','docx',
         'epub', 'fier', 'hive', 'html', 'list','pptx', 'tiff', 'type', 'xlsx', '._']

a = Organizer("Photos/", "organizado")
a.getFiles(nots, must)
a.moveEm()
