#2

import re

def open_():
    with open('new.xml', encoding='utf-8') as f:
        text = f.read()
    return text

def morph(text):
    k = 0
    match = re.search('<w lemma=".+" type=".+">.+</w>\s',text)
    if match:
        k = k + 1
    else:
        print('oyo')
    x = match.group()
    newd = {x:k}
    return (newd)

        
def main():
    dicty = {}

    corpus = open_()
    
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write('')

    text = open_()
    res = morph(text)
    dicty.update(res)

    for key, value in dicty.items():
        print(key, value)


main()
