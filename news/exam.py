'''
В общем, оно должно было работать как надо, но так не получилось.
Потратив множество времени на попытки заставить это работать со всеми файлами,
я так ни к чему и не пришла.
Что есть то есть.
'''


import os
import re

'''
def file_list():
    files = os.listdir()
    #print(files)
    return files
'''
def get_data(file_name):
    with open(file_name, encoding='cp1251') as f:
        raw_text = f.read()
    return raw_text

def info(text):
    ghj = []
    ghj.append('"_itartass1.xhtml"')
    pos = re.search(r'".+"(?= name="author")', text)
    ghj.append(pos.group(0))
    created = re.search(r'".+"(?= name="created")', text)
    ghj.append(created.group(0))
    header = re.search(r'".+"(?= name="header")', text)
    ghj.append(header.group(0))
    ghjstr = ';'.join(ghj)
    return(ghjstr)


def new_file(p):
    with open('res.csv', 'w') as f:
        f.write('"Название файла";"Автор";"Дата создания текста";"Заголовок"\n'+p)
        
    print('Проверьте файл')


if __name__ == '__main__':
    raw = get_data('_itartass1.xhtml')
    print(raw)
    ghjstr = info(raw)
    new_file(ghjstr)
