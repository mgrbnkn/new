#вариант 5
#Программа должна спрашивать у пользователя латинские слова до тех пор, пока он не введёт пустое слово.
#После этого программа должна записать построчно в файл те из введённых слов, которые с большой вероятностью
#являются формой 3-го лица пассива настоящего времени (каждое слово на отдельной строчке).

with open("text.txt", "w", encoding="utf-8") as f:
    f.write('')
a = 1
while a > 0:
    word = input()
    if bool(word) == False:
        break    
    if word[-3:] == 'tur':
        with open("text.txt", "a", encoding="utf-8") as f:
            f.write(word+"\n")
        with open("text.txt", "r", encoding="utf-8") as f:
            text = f.read()
print(text)


