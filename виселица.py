import random

list1=["вирус", "программа", "компьютер", "хакер", "взлом"]

word=random.choice(list1)

wrong = 0
stages=[" ", "________   ", "|        ", "|    |    ", "|    0    ", "|   /|\    ", "|   / \    ", "|        "]
rletters = list(word)
board = ["_"]*len(word)
win=False
print("Добро пожало�import random

list1=["вирус", "программа", "компьютер", "хакер", "взлом"]

word=random.choice(list1)

wrong = 0
stages=[" ", "________   ", "|        ", "|    |    ", "|    0    ", "|   /|\    ", "|   / \    ", "|        "]
rletters = list(word)
board = ["_"]*len(word)
win=False
print("Добро пожаловать на казнь!")
while wrong<len(stages)-1:
    print("\n")
    msg="Введите букву:"
    char=str(input(msg))
    if char in rletters:
        cind = rletters.index(char)
        board[cind]=char
        rletters[cind]='$'
    else:
        wrong+=1
    print((" ".join(board)))
    e = wrong + 1
    print("\n".join(stages[:e]))
    if "_" not in board:
        print("Вы выиграли! Быдо загадано слово: ")
        print(" ".join(board))
        win=True
        break
if not win:
    print("\n".join(stages[:wrong]))
    print("Вы проиграли! Было загадано слово: {}.".format(word))


        
