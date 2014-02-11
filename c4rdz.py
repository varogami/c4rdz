#!/usr/bin/env python


class Character:
    def __init__(self, id, type, name):
        self.id = id
        self.type = type
        self.name = name
        self.moves = []
    def hello(self):
        print "Hi, I am " + self.name + ", type " + self.type + " number " + str(self.id)
    def get_yx(self):
        return self.yx

class Game:
    def __init__(self, id):
        self.id = id
        self.cards = []
        self.matrix = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        ]
    def list(self):
        for c in self.cards:
            print c.name

    def put(self, card, x, y):
        self.cards.append(card)
        self.matrix[y][x] = card.id
        card.yx = y, x
    def move(self, card, move_id):
        card_id = card.id
        yy, xx = card.get_yx()
        self.matrix[yy][xx] = 0
        yy = yy + card.moves[move_id][0]
        xx = xx + card.moves[move_id][1]
        captured_id = self.matrix[yy][xx]
        self.matrix[yy][xx] = card_id
        card.yx = yy, xx
    def screen(self):
        stringa = "gioco\n"
        for i in range(4):
            for j in range(4):
                stringa = stringa + " " + str(self.matrix[i][j]) + " "
            stringa = stringa + "\n"
        print stringa

gioco = Game(1)
guer1 = Character(2, "warrior", "Conan")
guer1.moves.append((0, 1))
guer1.moves.append((0, -1))
guer2 = Character(1, "cleric", "Giulio")
guer2.moves.append((1, 0))
guer2.moves.append((-1, 0))

gioco.list()

gioco.screen()
gioco.put(guer1, 0, 0)
gioco.screen()
gioco.put(guer2, 3, 3)
gioco.screen()

gioco.move(guer1, 0)
gioco.screen()

gioco.move(guer2, 1)
gioco.screen()

