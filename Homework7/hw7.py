#5
#сколько в тексте прилагательных с суффиксом -ous,
#и какая средняя длина такого прилагательного.

def name():
    filename = input('Введите имя файла: ')
    return filename

def open_tokenize(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    text = text.replace(',', '').replace('.', '').replace(':','').replace('?','').replace('!','').replace('"','').replace(';','').replace(')','').replace('(','')
    text = text.lower()
    words = text.split()
    return words

def find_ous(words):
    dict_ous = {}
    for word in words:
       if word[-3:] == 'ous':
           new_word = {word: len(word)}
           dict_ous.update(new_word)
    return dict_ous

def main():
    filename = name()
    average = 0
    number = 0
    tokens = open_tokenize(filename)
    dictionary = find_ous(tokens)
    for value in dictionary.values():
        number = number + 1
        average = average + value
    average = average / number
    print('В тексте',number,'прилагательных с суффиксом -ous и средняя длина такого прилагательного',round(average),'букв.')

main()
