from crads_data import StarRealmsCards
import pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CARD_NAME_FONT = pygame.font.SysFont('Gameplay,', 35)
CARD_abilities_FONT = pygame.font.SysFont('Gameplay,',25)

class Card:
    def __init__(self,**attributes):
        self.attributes = attributes
        self.name = attributes['attributes']['name']
        self.card_width = 24
        self.card_height = 34
        self.card_scale = 5
        self.rect = pygame.rect.Rect((100, 200),
                                     (self.card_width * self.card_scale, self.card_height * self.card_scale))
        self.card_surface = pygame.Surface((self.card_width * self.card_scale, self.card_height * self.card_scale))
        self.card_name_text = CARD_NAME_FONT.render(self.name, True, BLACK)

        self.change_x = 0
        self.change_y = 0


    def display_card(self,screen):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        self.card_surface.blit(self.card_name_text, (self.card_surface.get_width() // 2 - 35, 0))
        screen.blit(self.card_surface, (self.rect.x, self.rect.y))
        self.card_surface.fill(WHITE)

    def drag_card(self, position, is_mouse_pressed):
        self.change_x, self.change_y = 0, 0
        mouse_change = pygame.mouse.get_rel()
        if position[0] in range(self.rect.left, self.rect.right) and \
                position[1] in range(self.rect.top, self.rect.bottom):
            if is_mouse_pressed:
                self.change_x += mouse_change[0]
                self.change_y += mouse_change[1]

    def run(self,screen):
        self.display_card(screen)
        #self.drag_card()

    def print_all_attributes(self):
        print(self.attributes)


#all_cards = StarRealmsCards.ALL_STAR_REALMS_CARDS
#card_scout = Card(attributes=all_cards[0])
#card_scout.print_all_attributes()
