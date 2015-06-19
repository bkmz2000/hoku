from random import choice, randint
from pickle import dump, load
from os import listdir


def countSyll(string, pat = ""):
    '''
        возвращает кол-во слогов
        или -1 (для сокращений)
    '''
                                 
    counter = 0
    
    if pat == "":
        pat = "аоэиуыеёюяьъй"

    for i in string:
        if i in pat:
            counter+=1

    if counter == 0 and len(string) > 1:
        counter = -1

    return counter

def nextWord(length, arr):
    '''
       возвращает слово с заданным кол-вом слогов
       
       length - "длинна" слова в слогах
       arr    - массив возможных слов
    '''
    
    av = []

    for i in arr:
        if countSyll(i) == length:
            av.append(i)

    return choice(av)

def nextLine(length, arr):
    '''
       возвращает строку с заданным кол-вом слогов
       
       length - "длинна" слова в слогах
       arr    - массив возможных слов   
    '''
    
    line = ""
    prev = 0
    while not length == 0:
        l = randint(0, length)

        if l == prev:
            continue
        
        prev = l
        line = line+nextWord(l, arr)+' '
        length -= l

    return line

def readAndPickle(name):
    '''
       чтение и разбор файла с именем  name,
       создание файла с разобранным текстом
    '''

    print('Чтение и разбор файла...')
    text = open(name+'.txt', 'r')
    text = text.read()

    text = text.lower()

    for i in text:
        if i in ",.?1234567890():[]»\"\'qwertyuiopasdfghjklzxcvbnm":
            text = text.replace(i, '')

    text = text.split()

    for i in text:
        while text.count(i) > 1:
            del text[text.index(i)]

    text.sort(key = countSyll)

    dump(text, open(name+'.data', 'wb'))
    return text

def readOrPickle(name):
    '''
       загружает разобранный файл с именем name
       или разбирает его заново
    '''
    
    if name+'.data' in listdir():
        print('Загрузка...')
        return load(open(name+'.data', 'rb'))

    else:
        return readAndPickle(name)

name = input('Введите имя файла без расширения (\'in\' по умолчанию) :')

if name == '':
    name = 'in'
text = readOrPickle(name)
    
for i in range(10):
    print(nextLine(5, text))
    print(nextLine(7, text))
    print(nextLine(6, text))
    print()

input()
