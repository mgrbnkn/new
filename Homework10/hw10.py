#5 статьи о растениях (напр., томат) — семейство
#в ботанике к основе названия типового рода добавляется стандартное окончание -aceae

import re

def open_(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    return text

def find(text):
    raw = str(re.search('aceae</span>"&gt;</span>[А-Яа-яё]+',text))
    fam = re.search('[А-Яа-яё]+',raw)
    return fam

def main():
    #список страниц - в отдельном файле
    with open("list_of_pages.txt", encoding="utf-8") as f:
        pages = f.read()
    pages = pages.splitlines()
    
    with open("familia.txt", "w", encoding="utf-8") as f:
        f.write('')
    
    for page in pages:
        text = open_(page)
        result = find(text)
        if result:
            with open("familia.txt", "a", encoding="utf-8") as f:
                f.write('Страница: '+page+'\nСемейство: '+result.group()+'\n\n')
        else:
            with open("familia.txt", "a", encoding="utf-8") as f:
                f.write('Страница: '+page+'\nСемейство: не обнаружено\n\n')
    print('Результат обновлен. Проверьте файл.')
        
main()
