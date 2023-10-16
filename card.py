import pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CARD_NAME_FONT = pygame.font.SysFont('Gameplay,', 32)
CARD_abilities_FONT = pygame.font.SysFont('Gameplay,',25)


class Card:
    def __init__(self,starting_pos, **attributes):
        self.attributes = attributes['attributes']
        self.name = self.attributes['name']
        self.card_width = 35
        self.card_height = 34
        self.card_scale = 5
        self.rect = pygame.rect.Rect((starting_pos[0], starting_pos[1]),
                                     (self.card_width * self.card_scale, self.card_height * self.card_scale))
        self.card_surface = pygame.Surface((self.card_width * self.card_scale, self.card_height * self.card_scale))
        self.card_name_text = CARD_NAME_FONT.render(self.name, True, BLACK)

        self.change_x = 0
        self.change_y = 0

    def __len__(self):
        return sum(map(len, self.name.split()))

    def display_card(self,screen):
        self.card_surface.blit(self.card_name_text, (self.card_surface.get_width() // 2 - 70, 2))
        screen.blit(self.card_surface, (self.rect.x, self.rect.y))
        self.card_surface.fill(WHITE)

    def drag_card(self, position, is_mouse_pressed, mouse_change):
        self.change_x, self.change_y = 0, 0
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            if is_mouse_pressed:
                self.rect.x += mouse_change[0]
                self.rect.y += mouse_change[1]

    def run(self, screen, position, is_mouse_pressed, mouse_change):
        self.display_card(screen)
        self.drag_card(position, is_mouse_pressed, mouse_change)

    def print_all_attributes(self):
        print(self.attributes)
