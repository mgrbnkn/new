#слово - последовательность символов, ограниченная пробельным символом

import os
import re

files = os.listdir()
directs = []

for file in files:
    path = file
    if os.path.exists(path):
        match = re.search('\s',path)
        if os.path.isdir(path) and match:
            directs.append(path)

print('Найдено папок, название которых состоит из более чем одного слова:',len(directs))
for direct in directs:
    print(direct)
