from random import shuffle

class Card:
    suits = ["пики", "черви", "буби", "трефы"]#переменная класса, представляющая спсиок всех мастей, которые есть у карт 
    values = [None, None, "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10 ", "вальта ", "даму ", "короля ", "туза "]#переменная класса, представляющая список номиналы карт. Элементы под 2-мя первыми индексами являются None, чтобы строки в списке совпадали с индексами, которые представляют строки
    def __init__(self, v, s):
        """suit и value - целые числа"""
        self.value = v #пременные экземпляра класса, представленные целым числом представляют вид карты объекста Card.
        self.suit = s #пременные экземп�from random import shuffle

class Card:
    suits = ["пики", "черви", "буби", "трефы"]#переменная класса, представляющая спсиок всех мастей, которые есть у карт 
    values = [None, None, "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10 ", "вальта ", "даму ", "короля ", "туза "]#переменная класса, представляющая список номиналы карт. Элементы под 2-мя первыми индексами являются None, чтобы строки в списке совпадали с индексами, которые представляют строки
    def __init__(self, v, s):
        """suit и value - целые числа"""
        self.value = v #пременные экземпляра класса, представленные целым числом представляют вид карты объекста Card.
        self.suit = s #пременные экземпляра класса, представленные целым числом представляют вид карты объекста Card.

    def __lt__(self, c2):#магический метод, позволяющий вам сравнивать два объекта Card в вырвжении при помощи операторов больше меньше
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):#магический метод, позволяющий вам сравнивать два объекта Card в вырвжении при помощи операторов больше меньше
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):#магический метод, использует переменные экземпляра values и suit для нахождения значения и масти карты в списках values и suits и возвращает их, чтобы можно было вывести карту, которую представляет объект Card.
        v=self.values[self.value] + "" \
        + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):# создают объекты, представляющие все карты в 52-карточной колоде и добавляют их в спсиок cards
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)


    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:#представляет каждого игрока и отслеживает их карты и кол-во выигранных ими раундов
    def __init__(self, name):
        self.wins=0 #отслеживает кол-во раундов, выигранных игроко
        self.card=None#представляет карты, которую в данный момент держит игрок
        self.name=name#отслеживает имя игрока

class Game:
    def __init__(self):
        name1=input("имя игрока 1: ")
        name2=input("имя игрока 2: ")
        self.deck=Deck()
        self.p1=Player(name1)
        self.p2=Player(name2)



    def wins(self, winner):
        w="{} забирает карты"
        w=w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n,  p2c):
        d="{} кладет {}, a {} кладет {}"
        d=d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards=self.deck.cards
        print("Поехали!")
        while len(cards) >= 2:
            m="Нажмите х для выхода. Нажмите любую лругую клавишу для начала игры."
            response=input(m)
            if response=="x":
                break
            p1c=self.deck.rm_card()
            p2c=self.deck.rm_card()
            p1n=self.p1.name
            p2n=self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("Игра окончена. {} выиграл!".format(win))


    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Ничья!"

print("Приветсвую вас в игре пьяница!\n Данная игра предлагает вам проверить свою удачу и выяснить кто сегодня из вас более везучий.\n Правила очень просты каждый игрок берёт из колоды по карте.\n Побеждает тот, у которого карта старше")
game = Game()
game.play_game()











            











        













        






















        
