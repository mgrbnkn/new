#world → orldway

print('Введите слово:')
phrase = input()

print('На Pig Latin это будет:')
word = ''
k = -1
for i in phrase:
    k = k + 1
    if phrase[k] != ' ':
        word = word + phrase[k]
        pig = word[1:] + word[0] + 'ay'
    else:
        word = ''
        print(pig)
print(pig)
