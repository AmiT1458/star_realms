from card import Card
from random import shuffle
from cards_data import *
from turn import Round
from client import send_msg, message


# class for the players actions in a turn
class Player:
    def __init__(self):
        self.health = 50
        self.combat = 0
        self.trade = 0
        self.draw_deck = None
        self.discard_pile = None
        self.in_play = None
        self.in_play_obj = []
        self.bases_in_play = []
        self.outposts_in_play = []
        self.playing = False
        self.dict_info = {'health': self.health,
                          'trade': self.trade,
                          'combat': self.combat,
                          'trade row': cards_to_display}

        self.starRealmsObj = StarRealmsCards

    def initialize_deck(self):
        shuffle(self.draw_deck)

    def get_hand(self):
        deck_5 = []
        n = 5
        while True:
            try:
                for i in range(n):
                    deck_5.append(self.draw_deck[4 - i])
                    self.draw_deck.pop(4 - i)
                    n -= 1
            except Exception as e:
                self.draw_deck += self.discard_pile
                self.initialize_deck()

                self.discard_pile = []
                continue
            break
        return deck_5

    def initialize_start(self):  # being called at the start of every game
        Scouts = ['Scout']
        Vipers = ['Viper']
        self.draw_deck = Scouts * 8 + Vipers * 2
        self.initialize_deck()
        self.discard_pile = []

    # displaying the player's hand at the start of the turn
    def get_cards_obj(self):
        self.in_play_obj = []
        i = 1
        for card in self.in_play:
            obj_card = Card((75 * i * 4 - 48, screen.get_height() - 220), attributes=StarRealmsCards(card, False).pick_card())
            self.in_play_obj.append(obj_card)

            # checking if the card is either a base or an outpost
            if obj_card.type == 'base':
                self.bases_in_play.append(card)
            elif obj_card.type == 'outpost':
                self.outposts_in_play.append(card)

            i += 1

    def display_cards_obj(self, is_mouse_pressed, enter_preview_cards):
        if self.playing:
            for card in self.in_play_obj:
                card.run((0, 0), is_mouse_pressed, enter_preview_cards)

    def set_info(self):  # setting the info as a dict to be sent to the other client (player)
        self.dict_info = {'health': self.health,
                          'trade': self.trade,
                          'combat': self.combat,
                          'trade row': cards_to_display
                          }

    def send_info(self):  # sending the info to the server
        send_msg(self.dict_info)

    def read_player_info(self, info):  # reading the info from the sever and changing stats accordingly
        self.get_damage(info['damage'])

    def get_damage(self, damage):
        self.health -= damage

    def buy_card(self, card):
        self.trade -= card.cost
        self.discard_pile.append(card.name)

    def end_turn_hand(self):  # ending the current turn and preparing to the next one
        self.set_info()
        # self.send_info()
        self.discard_pile += self.in_play

        self.playing = False
        self.combat = 0
        self.trade = 0

    def start_turn(self):  # starts a new turn
        # self.read_player_info(message)
        self.in_play = self.get_hand()
        self.get_cards_obj()
        self.combat = 0
        self.trade = 0
        self.playing = True
        Round().player_turn(self)

    def pursue_turn(self, status):
        if not status:
            self.end_turn_hand()

        else:
            self.start_turn()

    def end_turn_start(self):  # a method for unit test Player
        self.start_turn()
        self.end_turn_hand()
