import pygame
from crads_data import StarRealmsCards
from card import Card
from random import choice
from player import Player

pygame.init()
pygame.font.init()

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Star realms")
CARD_NAME_FONT = pygame.font.SysFont('Gameplay,',35)
CARD_abilities_FONT = pygame.font.SysFont('Gameplay,',25)

run = True
is_mouse_pressed = False


#Scout = Card(scout_pos, attributes=StarRealmsCards('Scout', False).pick_card()) example of a card (Scout)

cards_to_display = []

class Manage_Game:
    def __init__(self):
        self.deck_pile_dic = None
        self.deck_pile = None

    def initialize_deck(self):
        self.deck_pile_dic = \
            [cards for cards in StarRealmsCards.ALL_STAR_REALMS_CARDS if not cards['name'] == 'Scout']  # removing the Scouts from the deck pile
        self.deck_pile_dic.pop(0)  # removing the Vipers
        self.deck_pile_dic.pop(0)

        self.deck_pile = [card['name'] for card in self.deck_pile_dic for _ in range(card['quantity'])]
        self.deck_pile.sort()

    def display_trade(self):
        #print(self.deck_pile_dic)
        #print(self.deck_pile)

        for i in range(6):
            cards_to_display.append(Card((i * 300, SCREEN_HEIGHT // 2 - 50), attributes=StarRealmsCards(choice(self.deck_pile), False).pick_card()))

    def run(self):
        self.display_trade()


count_presses = 0
mouse_change = pygame.mouse.get_rel()
enter_preview_cards = False

deck = Manage_Game()
deck.initialize_deck()
deck.run()

player_1 = Player()
player_1.initialize()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            exit()
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                exit()
                break

            if event.key == pygame.K_SPACE:
                cards_to_display[0].change_card()

        if event.type == pygame.MOUSEBUTTONDOWN:
            is_mouse_pressed = True

        if event.type == pygame.MOUSEBUTTONUP:
            is_mouse_pressed = False

    mx, my = pygame.mouse.get_pos()
    mouse_change = pygame.mouse.get_rel()

    screen.fill(BLACK)
    for card in cards_to_display:
        card.run(screen, (mx, my), is_mouse_pressed, enter_preview_cards)
        if card.enter_preview:
            enter_preview_cards = True

        elif card.can_enter_global:
            enter_preview_cards = False

    pygame.display.update()