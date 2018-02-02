#world → orldway

print('Введите слово:')
phrase = input()

print('На Pig Latin это будет:')
word = ''
pig_phrase = ''
k = -1
for i in phrase:
    k = k + 1
    if phrase[k] != ' ':
        word = word + phrase[k]
        pig = word[1:] + word[0] + 'ay'
    else:
        word = ''
        pig_phrase = pig_phrase + pig + ' '
pig_phrase = pig_phrase + pig + ' '
print(pig_phrase)
