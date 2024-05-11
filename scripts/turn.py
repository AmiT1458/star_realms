from star_realms.scripts.cards_data import *
from star_realms.scripts.card import Card
from random import choice
from Button import Button


class Manage_Game:
    def __init__(self):
        self.deck_pile_dic = None
        self.deck_pile = None

    def initialize_trade_deck(self):
        self.deck_pile_dic = \
            [cards for cards in StarRealmsCards.ALL_STAR_REALMS_CARDS if not cards['name'] == 'Scout']  # removing the Scouts from the deck pile
        self.deck_pile_dic.pop(0)  # removing the Vipers
        self.deck_pile_dic.pop(0)

        self.deck_pile = [card['name'] for card in self.deck_pile_dic for _ in range(card['quantity'])]
        self.deck_pile.sort()

    def display_trade(self):
        for i in range(6):
            cards_to_display.append(Card((i * 300, SCREEN_HEIGHT // 2 - 175), attributes=StarRealmsCards(choice(self.deck_pile), False).pick_card()))

    def remove_card(self, card):
        cards_to_display.remove(card)
        #cards_to_display.append(StarRealmsCards.pick_card())

    def run(self):
        self.display_trade()


# class for changing the players' stats according to their turns
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
    def __init__(self):
        self.font = UI_FONT
        self.button = Button(SCREEN_WIDTH - 300, SCREEN_HEIGHT - 50, "hello", 250)

    def draw_stats(self, player):
        if player.playing:
            screen.blit(self.font.render(f"trade: {player.trade}", False, YELLOW),
                        (5, SCREEN_HEIGHT - 3 * self.font.get_height()))
            screen.blit(self.font.render(f"combat: {player.combat}", False, RED),
                        (5, SCREEN_HEIGHT - 2 * self.font.get_height()))
            screen.blit(self.font.render(f"health: {player.health}", False, GREEN),
                        (5, SCREEN_HEIGHT - self.font.get_height()))
        else:
            screen.blit(self.font.render(f"trade: {0}", False, YELLOW),
                        (5, SCREEN_HEIGHT - 3 * self.font.get_height()))
            screen.blit(self.font.render(f"combat: {0}", False, RED),
                        (5, SCREEN_HEIGHT - 2 * self.font.get_height()))
            screen.blit(self.font.render(f"health: {player.health}", False, GREEN),
                        (5, SCREEN_HEIGHT - self.font.get_height()))

    def end_start_button(self, player):
        if player.playing:
            self.button.change_text_input("End")

        if not player.playing:
            self.button.change_text_input("Start")

        self.button.update()

    def run(self, player):
        self.end_start_button(player)
        self.draw_stats(player)
