#5
#сколько в этих папках встречается разных названий файлов без учёта расширений;

import os

def main():
    directs = []
    start_path = '.'

    for file in os.walk(start_path):
        names = file[2]
        for name in names:
            name = name.split('.')[:-1]
            directs.extend(name)
    directs = set(directs)
    print('Сколько в этих папках разных названий файлов без учёта расширений?',len(directs))

main()

