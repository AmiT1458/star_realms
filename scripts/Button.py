import pygame
from cards_data import screen, UI_FONT, UI_SIZE, WHITE


class Button():
    def __init__(self, x_pos,y_pos,text_input, size):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size
        self.text_input = text_input
        self.rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.size, UI_SIZE))
        self.font = UI_FONT
        self.text = self.font.render(self.text_input , True , 'black')
        self.text_rect = self.text.get_rect(topleft=(self.x_pos,self.y_pos))
        self.color = 'black'

    def check_for_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top , self.rect.bottom):
            return True
        return False

    def change_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.color = 'green'

        else:
            self.color = 'black'

        self.text = self.font.render(self.text_input, True, self.color)

    def change_text_input(self, text_input):
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.color)

    def update(self):
        pygame.draw.rect(screen, WHITE, self.rect)
        screen.blit(self.text, self.text_rect)
