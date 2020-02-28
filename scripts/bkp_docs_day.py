import os
import time
import zipfile
import sys

# задание переменных
SRC_DIR = '/home/danya/python' 
#'x:\Docs'
DST_DIR = '/home/danya/archive/' 
#'Z:\Backups\Docs'
BKP_NAME = "Docs_day_"

now = time.strftime('%d-%m-%Y')

# прверяем есть ли каталог, который хотим бэкапить
if not os.path.exists(SRC_DIR):
    f = open('error.txt', 'w+')
    f.write('Не существует каталога для архивирования - ' + SRC_DIR)
    f.write('\nБэкап не сделан ...')
    f.close()
else:
    f = open('backup.txt', 'w+')
    f.write('Каталог ' + SRC_DIR + ' существет, начало создания бэкапа' + ' - ' 
            + str(time.asctime()))
#    sys.stdout = open('backup.txt', 'w')
    zipp=zipfile.ZipFile(DST_DIR + BKP_NAME + now + '.zip','w')
    for root, dirs, files in os.walk(SRC_DIR):
        for file in files:
           zipp.write(os.path.join(root, file))
    zipp.close()
    f.write('\nБэкап создан в' + ' - ' + str(time.asctime()))
    f.close()


