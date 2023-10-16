import pygame
from crads_data import StarRealmsCards
from card import Card

pygame.init()
pygame.font.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Star realms")
card_height = 34
card_width = 24
card_scale = 5
CARD_NAME_FONT = pygame.font.SysFont('Gameplay,',35)
CARD_abilities_FONT = pygame.font.SysFont('Gameplay,',25)

card_rect = pygame.rect.Rect((100, 200), (card_width * card_scale, card_height * card_scale))

card_scout = StarRealmsCards.ALL_STAR_REALMS_CARDS[0]

run = True
is_mouse_pressed = False
card_movement = (0,0)

Scout = Card(attributes=card_scout) # example of a card (Scout)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            exit()
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_mouse_pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            is_mouse_pressed = False

    mx, my = pygame.mouse.get_pos()

    screen.fill(BLACK)
    Scout.run(screen, (mx, my), is_mouse_pressed)

    pygame.display.update()