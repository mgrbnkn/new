#вариант 5: Какой процент слов имеет длину больше 10 символов?

with open("text.txt", encoding="utf-8") as f:
    text = f.read()
words = text.split()
print(text)
print()
count = 0
for word in words:
    number = len(word)
    if number > 10:
        count = count + 1
print('Слов в тексте: ',len(words))
print('Слов длиннее 10 символов: ',count)
x = count * 100 // len(words)
print(x,'%')
