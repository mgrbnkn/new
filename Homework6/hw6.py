import random

def loc():
    with open('words/loc.txt', encoding = 'utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words.append(line)
        return random.choice(words)

def ling():
    with open('words/ling.txt', encoding = 'utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words.append(line)
        return random.choice(words)

#action
def predv():
    with open('words/predv.txt', encoding = 'utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words.append(line)
        return random.choice(words)

#state
def preda():
    with open('words/preda.txt', encoding = 'utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words.append(line)
        return random.choice(words)

#coordinate    
def conjco():
    with open('words/conjco.txt', encoding = 'utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words.append(line)
        return random.choice(words)

#subordinate
def conjsu():
    with open('words/conjsu.txt', encoding = 'utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words.append(line)
        return random.choice(words)

def conj():
    number = random.choice([1,2])
    if number == 1:
        return conjco()
    else:
        return conjsu()
    
def subj():
    with open('words/subj.txt', encoding = 'utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words.append(line)
        return random.choice(words)
        
def advs():
    with open('words/advs.txt', encoding = 'utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words.append(line)
        return random.choice(words)

def advd():
    with open('words/advd.txt', encoding = 'utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words.append(line)
        return random.choice(words)
        
def verb():
    with open('words/verb.txt', encoding = 'utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words.append(line)
        return random.choice(words)

def obj():
    with open('words/obj.txt', encoding = 'utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words.append(line)
        return random.choice(words)

def modal():
    with open('words/modal.txt', encoding = 'utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words.append(line)
        return random.choice(words)

def inf():
    with open('words/inf.txt', encoding = 'utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words.append(line)
        return random.choice(words)
    
def ind():
    with open('words/ind.txt', encoding = 'utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words.append(line)
        return random.choice(words)

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
