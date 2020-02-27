import os
import time
import zipfile

# задание переменных
SRC_DIR = '/home/danya/python' 
#'x:\Docs'
DST_DIR = '/home/danya/archive/' 
#'Z:\Backups\Docs'
BKP_NAME = "Docs_day_"

now = time.strftime('%d-%m-%Y')

# прверяем есть ли каталог, который хотим бэкапить
if not os.path.exists(SRC_DIR):
    print('Не существует каталога для архивирования - ' + SRC_DIR)
else:
    print('Каталог ' + SRC_DIR + ' существет, можем начинать')

zipp=zipfile.ZipFile(DST_DIR + now + '_new.zip','w')
for root, dirs, files in os.walk(SRC_DIR):
    for file in files:
        zipp.write(os.path.join(root, file))
zipp.close()




