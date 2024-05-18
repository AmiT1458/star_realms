from star_realms.scripts.cards_data import *
from star_realms.scripts.card import Card
from random import choice
from Button import Button
from pygame import time

class Manage_Game:
    def __init__(self):
        self.deck_pile_dic = None
        self.deck_pile = None
        self.in_play = []

    def initialize_trade_deck(self):
        self.deck_pile_dic = \
            [cards for cards in StarRealmsCards.ALL_STAR_REALMS_CARDS if not cards['name'] == 'Scout']  # removing the Scouts from the deck pile
        self.deck_pile_dic.pop(0)  # removing the Vipers
        self.deck_pile_dic.pop(0)

        self.deck_pile = [card['name'] for card in self.deck_pile_dic for _ in range(card['quantity'])]

    def display_trade(self):
        for i in range(6):
            card_name = choice(self.deck_pile)
            cards_to_display.append(Card((i * 300, screen.get_height() // 2 - 175), attributes=StarRealmsCards(card_name, False).pick_card()))
            self.deck_pile.remove(card_name)

    def replace_card(self, card):
        try:
            self.deck_pile.remove(card.name)
            print(len(self.deck_pile))
        except Exception:
            pass
        card.change_card(choice(self.deck_pile))

    def run(self):
        self.display_trade()


# class for changing the players' stats according to their turns
# TODO: make this class the communication tool for the players
class Round:
    def __init__(self):
        pass

    def player_turn(self, player):
        stats_dict = {'combat': 0, 'trade': 0, 'authority': 0, 'draw': 0}

        for stat in stats_dict.keys():
            for card in player.in_play_obj:
                if card.attributes.get(stat) is not None:
                    stats_dict[stat] += card.attributes[stat]

                if card.name != 'Scout' and card.name != 'Viper':
                    if card.attributes['abilities'].get(stat) is not None:
                        stats_dict[stat] += card.attributes['abilities'][stat]

        player.trade += stats_dict['trade']
        player.combat += stats_dict['combat']
        player.health += stats_dict['authority']


class UI:
    def __init__(self, player):
        self.font = UI_FONT
        self.turn_button = Button(screen.get_width() - 300, screen.get_height() - 50, "hello", 250)
        self.player = player
        self.player_status = ["Start", "End"]
        self.current_time = time.get_ticks()
        self.countdown = 250
        self.timer_point = 0
        self.turn_button.change_text_input(self.player_status[int(self.player.playing)])

    def draw_stats(self):
        if self.player.playing:
            screen.blit(self.font.render(f"trade: {self.player.trade}", False, YELLOW),
                        (5, screen.get_height() - 3 * self.font.get_height()))
            screen.blit(self.font.render(f"combat: {self.player.combat}", False, RED),
                        (5, screen.get_height() - 2 * self.font.get_height()))
            screen.blit(self.font.render(f"health: {self.player.health}", False, GREEN),
                        (5, screen.get_height() - self.font.get_height()))
        else:
            screen.blit(self.font.render(f"trade: {0}", False, YELLOW),
                        (5, screen.get_height() - 3 * self.font.get_height()))
            screen.blit(self.font.render(f"combat: {0}", False, RED),
                        (5, screen.get_height() - 2 * self.font.get_height()))
            screen.blit(self.font.render(f"health: {self.player.health}", False, GREEN),
                        (5, screen.get_height() - self.font.get_height()))

    def draw_buy_outline(self):
        for card in cards_to_display:
            if self.player.trade >= card.cost:
                card.make_yellow()

    def end_start_button(self, position, is_mouse_pressed):
        if self.turn_button.check_for_input(position, is_mouse_pressed) and self.current_time - self.timer_point >= self.countdown:
            self.timer_point = time.get_ticks()
            self.player.playing = not self.player.playing
            self.turn_button.change_text_input(self.player_status[int(self.player.playing)])

        self.turn_button.change_color(position)
        self.turn_button.update()

    def run(self, position, is_mouse_pressed):
        self.end_start_button(position, is_mouse_pressed)
        self.draw_stats()
        self.draw_buy_outline()
        self.current_time = time.get_ticks()