#5
#Программа показывает число попыток, которое
#пользователь уже сделал, чтобы угадать слово

import random

def opening(filename):
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def puzzle_making(lines):
    dict = {}
    for line in lines:
        line = line.strip()
        line = line.split(',')
        puzzle = {line[0]:line[1]}
        dict.update(puzzle)
    return(dict)

def game(dict):
    print('Добро пожаловать в игру "Звезда по имени ...".\n\nПопробуйте угадать слово, которое мы заменили тремя точками:')
    keys = list(dict.keys())
    word = random.choice(keys)
    print(dict[word])
    print('\nВведите свой вариант ответа:')
    answer = input().lower()
    counter = 2
    if answer == word:
        print('Великолепно! Вы угадали!')
    else:
        print('Увы! Неудача. Попробуйте угадать ещё раз или остановите игру словом "стоп".')
        while answer != word:
            print('\nПопытка №',counter,'. Введите слово:', sep = '')
            answer = input().lower()
            counter += 1
            if answer == 'стоп':
                print('Спасибо за игру! Было загадано слово:',word)
                break
            elif answer != word:
                print('Увы! Неудача. Попробуйте угадать ещё раз или остановите игру словом "стоп":')
            else:
                print('Великолепно! Вы угадали!')

def main():
    lines = opening('puzzle.csv')
    puzzles = puzzle_making(lines)
    game(puzzles)

main()

