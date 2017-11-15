word = input('Введи слово: ')
print(word)
k = len(word)
for i in word:
    print(word[k-1:])
    k = k-1
