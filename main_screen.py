import pygame
from crads_data import StarRealmsCards

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Star realms")
card_height = 34
card_width = 24
card_scale = 5

card_rect = pygame.rect.Rect((100, 200), (card_width * card_scale, card_height * card_scale))
def display_card(card_movement):
    card_surface = pygame.Surface((card_width  * card_scale, card_height * card_scale))
    card_surface.fill(WHITE)

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
    card_rect = display_card(card_movement)
    card_movement = drag_card((mx, my) ,card_rect, is_mouse_pressed)
    #print(pygame.mouse.get_rel())

    pygame.display.update()