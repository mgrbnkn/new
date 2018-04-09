#1
import re

def open_():
    with open('new.xml', encoding='utf-8') as f:
        text = f.readlines()
    return text

def find(lines):
    k = 0
    for line in lines:
        k = k + 1
        match = re.search('</teiHeader>\s',line)
        if match:
            break
    return k

def main():
    corpus = open_()
    
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write('')

    text = open_()
    number = find(text)
    if number:
        with open("result.txt", "a", encoding="utf-8") as f:
            f.write('Cтрок заголовка XML (то есть от начала файла до строки, которая содержит "</teiHeader>": '+str(number))
    else:
        with open("result.txt", "a", encoding="utf-8") as f:
            f.write('Ничего не обнаружено')
            
    print('Результат обновлен. Проверьте файл.')

main()
