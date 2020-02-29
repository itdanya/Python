import os
import time
import zipfile
import sys
import smtplib
import codecs


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
    f.write('Not found folder - ' + SRC_DIR)
    f.write('\nBackup is fail ...')
    f.close()
else:
    f = codecs.open('backup.txt', 'w+', 'utf-8')
    f.write('Folder ' + SRC_DIR + ' OK, starting backup ... ' + ' - ' 
            + str(time.asctime()))
#    sys.stdout = open('backup.txt', 'w')
    zipp=zipfile.ZipFile(DST_DIR + BKP_NAME + now + '.zip','w')
    for root, dirs, files in os.walk(SRC_DIR):
        for file in files:
           zipp.write(os.path.join(root, file))
    zipp.close()
    f.write('\nBackup already exist at' + ' - ' + str(time.asctime()))
    f.close()


