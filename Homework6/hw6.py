import random

def get_text(filename):
    with open(filename, encoding = 'utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words.append(line)
        return random.choice(words)

def loc():
    return get_text('words/loc.txt')

def ling():
    return get_text('words/ling.txt')

#action
def predv():
    return get_text('words/predv.txt')

#state
def preda():
    return get_text('words/preda.txt')

#coordinate    
def conjco():
    return get_text('words/conjco.txt')

#subordinate
def conjsu():
    return get_text('words/conjsu.txt')

def conj():
    number = random.choice([1,2])
    if number == 1:
        return conjco()
    else:
        return conjsu()
    
def subj():
    return get_text('words/subj.txt')
        
def advs():
    return get_text('words/advs.txt')

def advd():
    return get_text('words/advd.txt')
        
def verb():
    return get_text('words/verb.txt')

def obj():
    return get_text('words/obj.txt')

def modal():
    return get_text('words/modal.txt')

def inf():
    return get_text('words/inf.txt')
    
def ind():
    return get_text('words/ind.txt')

def punct():
    return random.choice(['.', '!', '...'])

def sentence1():
    part1 = loc() + ' ' + ling() + ' ' + preda()
    part2 = subj() + ' ' + advs() + ' ' + verb()
    order = random.choice([1,2])
    if order == 1:
        sentence = part1 + ', ' + conj() + ' ' + part2 + punct()
    else:
        sentence = part2 + ', ' + conj() + ' ' + part1 + punct()
    return sentence[0].upper() + sentence[1:]

def sentence2():
    choose = random.choice([1,2])
    if choose == 1:
        part1 = conjsu() + ' ' + subj() + ' ' + ind() + ' ' + obj()
    else:
        part1 = conjsu() + ' ' + subj() + ' ' + modal() + ' ' + inf() + ' ' + obj()
    part2 = ling() + ' ' + advd() + ' ' + predv()
    order = random.choice([1,2])
    if order == 1:
        sentence = part1 + ', ' + part2 + punct()
    else:
        sentence = part2 + ', ' + part1 + punct()
    return sentence.capitalize()

def sentence():
    choose = random.choice([1,2])
    if choose == 1:
        return sentence1()
    else:
        return sentence2()

for i in range(5):
    print(sentence(), end = ' ')

