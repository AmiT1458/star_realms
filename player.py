from random import choice
from card import Card
from crads_data import StarRealmsCards


class Player:
    def  __init__(self):
        self.health = 50
        self.combat = 0
        self.trade = 0
        self.deck = None
        self.discard_pile = None
        self.in_play = None

    def initialize(self):
        Scouts = ['Scout']
        Vipers = ['Viper']
        self.deck = Scouts * 8 + Vipers * 2
        self.discard_pile = []
        self.in_play = [choice(self.deck) for _ in range(5)]

        print(self.in_play)