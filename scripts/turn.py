from star_realms_game.scripts.cards_data import *
from star_realms_game.scripts.card import Card
from random import choice
from Button import Button
from pygame import time


class Manage_Game:
    def __init__(self):
        self.deck_pile_dic = None
        self.deck_pile = None
        self.explorer_pile = ['Explorer' * StarRealmsCards.ALL_STAR_REALMS_CARDS[2]['quantity']]
        self.in_play = []
        self.current_time = pygame.time.get_ticks()
        self.timer_point = 0
        self.buy_cooldown = 500

    def initialize_trade_deck(self):
        self.deck_pile_dic = \
            [cards for cards in StarRealmsCards.ALL_STAR_REALMS_CARDS if not cards['name'] == 'Scout' and
             not cards['name'] == 'Viper'
             and not cards['name'] == 'Explorer']  # removing the Scouts, Vipers and Explorers from the deck pile

        self.deck_pile = [card['name'] for card in self.deck_pile_dic for _ in range(card['quantity'])]
        self.deck_pile.sort()

    def display_trade(self):
        for i in range(5):
            card_name = choice(self.deck_pile)
            cards_to_display.append(Card((i * 300 + 50, trade_row_pos_y),
                                         attributes=StarRealmsCards(card_name).pick_card()))
            self.deck_pile.remove(card_name)

        #cards_to_display.append(Card((1550, screen.get_height() // 2 - 100)),
                                #attributes=StarRealmsCards("Explorer").pick_card())

    def replace_card(self, card):
        try:
            self.deck_pile.remove(card.name)
        except Exception:
            pass
        card.change_card(choice(self.deck_pile))

    def buy_card(self, player):
        if player.playing:
            for card in cards_to_display:
                if card.check_buy_button() and player.trade >= card.cost and self.current_time - self.timer_point >= self.buy_cooldown:
                    self.timer_point = pygame.time.get_ticks()
                    player.buy_card(card)
                    self.replace_card(card)

        self.current_time = pygame.time.get_ticks()

    def run(self):
        self.display_trade()


class UI:
    def __init__(self, player):
        self.font = UI_FONT
        self.turn_button = Button(screen.get_width() - 300, screen.get_height() - 50, "hello", 251)
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
            self.player.pursue_turn(self.player.playing)

        self.turn_button.change_color(position)
        self.turn_button.update()

    def run(self, position, is_mouse_pressed):
        self.end_start_button(position, is_mouse_pressed)
        self.draw_stats()
        self.draw_buy_outline()
        self.current_time = time.get_ticks()
        self.turn_button.update_rect_position(screen.get_width() - 300, screen.get_height() - 50)
