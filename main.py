
def dictToStr():
    global dictionary
    dictContent = ''
    for i in dictionary:
        dictContent += f'{i}:{dictionary[i]}\n'
    return dictContent

def translateWord(word):
    isInLine = False
    file = open('words.txt', 'r', encoding='utf-8')
    for line in file:
        if word in line:
            isInLine = True
            print(line + "\n")
    if isInLine == False:
        print('Nie ma takiego słowa\n')
    file.close()

def printDict():
    file = open('words.txt', 'r', encoding='utf-8')
    wordsArr = file.readlines()
    wordStr = "".join(wordsArr)
    print(wordStr + "\n")
    file.close()

def appendWord(plWord, enWord):
    exists = False
    fileAdd = open('words.txt', 'a', encoding='utf-8')
    file = open('words.txt', 'r', encoding='utf-8')
    for line in file:
        if plWord in line:
            exists = True
            print('Takie słowo już istnieje\n')
    if exists == False:
        fileAdd.write(f"\n{plWord}:{enWord}")
        print(f"Pomyślnie dodano słowo '{plWord}'\n")
    fileAdd.close()
    file.close()

dictionary = {}
file = open('words.txt', 'r', encoding="utf_8")
for i in file.readlines():
    line = str.split(i, ':')
    dictionary[line[0]] = line[1].replace('\n', '')
file.close()

def deleteWord(word):
    global dictionary
    if word in dictionary:
        dictionary.pop(word)
        file = open('words.txt', 'w', encoding="utf-8")
        file.writelines(dictToStr())
        file.close()
        print(f"Słowo {word} zostało pomyślnie usunięte\n")
    else:
        print('Takie słowo nie istnieje\n')

while(True):
    print('Dictionary v2.0\n[T] - Tłumacz\n[P] - Wypisz słownik\n[+] - Dodaj słowo\n[-] - Usuń słowo\n\n[x] - Wyjdź')
    choice = input()

    if(choice.lower() == 't'):
        word = input('Podaj słowo: ')
        translateWord(word)
    elif(choice.lower() == 'p'):
        printDict()
    elif(choice == '+'):
        plWord = input('Podaj polskie słowo: ')
        enWord = input('Podaj jego tłumaczenie: ')
        appendWord(plWord, enWord)
    elif(choice == '-'):
        plWord = input('Podaj słowo do usunięcia: ')
        deleteWord(plWord)
    elif(choice.lower() == 'x'):
        exit('Zakończono program')