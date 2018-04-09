import re

def name():
    filename = input('Введите имя файла: ')
    return filename

def open_(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    return text

def find(text):
    res = re.sub('Диноза.?вр','Кот',text)
    res = re.sub('динозавр','кот',res)
    return res

def main():
    filename = name()
    text = open_(filename)
    result = find(text)
    with open("Коты.html", "w", encoding="utf-8") as f:
        f.write(result)
  
main()
