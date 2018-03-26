#формы глагола «съесть»
import re

def name():
    filename = input('Введите имя файла: ')
    return filename

def open_(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    text = text.replace(',', '').replace('.', '').replace(':','').replace('?','').replace('!','').replace('"','').replace(';','').replace(')','').replace('(','').replace('\t',' ').replace('\n',' ')
    text = text.lower()
    return text

def find(text):
    list1 = re.findall('съел.?с?я?ь?\s',text)
    list3 = re.findall('съешь.?.?\s',text)
    list2 = re.findall('съед.?.?.?\s',text)
    list4 = re.findall('съев.?.?.?.?с?я?ь?\s',text)
    list5 = re.findall('съеден.?.?.?.?\s',text)
    list6 = re.findall('съесть?с?я?\s',text)
    list7 = re.findall('съем\s',text)
    biglist = list1 + list2 + list3 + list4 + list5 + list6 + list7
    return biglist

def nice_result(biglist):
    if len(biglist) == 0:
        print('Ничего не найдено')
    else:
        result = set(biglist)
        print('В вашем тексте встретились формы:')
        for word in result:
            word = word.strip()
            print(word)
    
def main():
    filename = name()
    text = open_(filename)
    biglist = find(text)
    nice_result(biglist)
    
main()
