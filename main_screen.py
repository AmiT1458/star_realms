import pygame
from crads_data import StarRealmsCards
from card import Card
import random
pygame.init()
pygame.font.init()

SCREEN_WIDTH = 1700
SCREEN_HEIGHT = 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Star realms")
CARD_NAME_FONT = pygame.font.SysFont('Gameplay,',35)
CARD_abilities_FONT = pygame.font.SysFont('Gameplay,',25)

run = True
is_mouse_pressed = False
card_movement = (0, 0)
scout_pos = (600, 200)
viper_pos = (250, 500)

Scout = Card(scout_pos, attributes=StarRealmsCards('Scout', False).pick_card()) # example of a card (Scout)
Viper = Card(viper_pos, attributes=StarRealmsCards('Viper', False).pick_card())
other_ship = Card((500, 500), attributes=StarRealmsCards('Blob Carrier', False).pick_card())

cards_to_display = [other_ship]

mouse_change = pygame.mouse.get_rel()

#other_ship.print_all_attributes()

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

        if event.type == pygame.MOUSEBUTTONDOWN:
            is_mouse_pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            is_mouse_pressed = False

    mx, my = pygame.mouse.get_pos()
    mouse_change = pygame.mouse.get_rel()

    screen.fill(BLACK)
    for card in cards_to_display:
        card.run(screen, (mx, my), is_mouse_pressed, mouse_change)

    #Viper.run(screen, (mx, my), is_mouse_pressed, mouse_change)
    #Scout.run(screen, (mx, my), is_mouse_pressed, mouse_change)
    #other_ship.run(screen, (mx, my), is_mouse_pressed, mouse_change)

    pygame.display.update()