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

def display_card(card_movement):
    card_surface = pygame.Surface((card_width * card_scale, card_height * card_scale))
    card_surface.fill(WHITE)

    card_name_text = CARD_NAME_FONT.render(card_scout['name'], True, BLACK)
    card_surface.blit(card_name_text, (card_surface.get_width() // 2 - 35 ,0))
    card_surface.blit(CARD_abilities_FONT.render("Trade: " + str(card_scout['trade']), True, BLACK), (card_surface.get_width() // 2 - 23, 30))

    card_rect.x += card_movement[0]
    card_rect.y += card_movement[1]

    screen.blit(card_surface, (card_rect.x, card_rect.y))
    return card_rect

def drag_card(position,card_rect, is_mouse_pressed):
    change_x, change_y = 0, 0
    mouse_change = pygame.mouse.get_rel()
    if position[0] in range(card_rect.left, card_rect.right) and position[1] in range(card_rect.top, card_rect.bottom):
        if is_mouse_pressed:
            change_x += mouse_change[0]
            change_y += mouse_change[1]

    return change_x, change_y

run = True
is_mouse_pressed = False
card_movement = (0,0)

Scout = Card(attributes=card_scout)

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

    #card_rect = display_card(card_movement)
    #card_movement = drag_card((mx, my) ,card_rect, is_mouse_pressed)

    Scout.display_card(screen)
    Scout.drag_card((mx, my), is_mouse_pressed)

    #print(pygame.mouse.get_rel())

    pygame.display.update()