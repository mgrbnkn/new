#5
#я не смогла придумать, куда применить форматирование строк

import re
import collections

def name():
    filename = input('Введите имя файла: ')
    #filename = 'pik.txt'
    return filename

def open_(filename):
    with open(filename, encoding='utf-8') as f:
        lines = f.read(1000)
    lines = re.split(r'\.|\?|\!|\n', lines)
    return lines
    
def replacing(sentences):
    sentences = [sentence for sentence in sentences if sentence]
    sentences = [sentence.lower() for sentence in sentences]
    sentences = [re.sub(r'[^\w\s]','',sentence) for sentence in sentences]
    sentences = [sentence.strip() for sentence in sentences]
    for sentence in sentences:
        words = sentence.split()
        sentence2 = []
        for word in words:
            cbf = collections.Counter()
            for letter in word:
                cbf[letter] += 1
            word = [letter * cbf[key] for letter in word for key in cbf if letter == key]
            word = ''.join(word)
            sentence2.append(word)
        sentence2 = ' '.join(sentence2)
        print(sentence2)

def main():
    filename = name()
    text = open_(filename)
    replacing(text)
    
main()
