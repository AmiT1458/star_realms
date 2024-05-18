import pygame

from player import Player
from turn import *
from client import disconnect


class Game:
    def __init__(self):
        self.current_time = pygame.time.get_ticks()
        self.run = True
        self.is_mouse_pressed = False
        self.is_mouse_pressed_right = False

        self.mouse_change = pygame.mouse.get_rel()
        self.position = (0, 0)
        self.enter_preview_cards = False

        pygame.init()
        # pygame.font.init()

        self.deck = Manage_Game()
        self.deck.initialize_trade_deck()
        self.deck.run()

        self.player_1 = Player()
        self.player_1.initialize_start()

        self.UI = UI(self.player_1)

        self.screen_settings = [pygame.FULLSCREEN, pygame.RESIZABLE]

    def run_display_cards(self):
        for card in cards_to_display:
            card.run(self.position, self.is_mouse_pressed, self.enter_preview_cards, self.is_mouse_pressed_right)
            if card.enter_preview:
                self.enter_preview_cards = True

            elif card.can_enter_global:
                self.enter_preview_cards = False

    def main(self):

        while self.run:
            current_time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    disconnect()
                    exit()
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run = False
                        disconnect()
                        exit()
                        break

                    if event.key == pygame.K_SPACE:
                        #cards_to_display[0].change_card()
                        self.deck.replace_card(cards_to_display[1])
                        # print(cards_to_display[1].name)

                    if event.key == pygame.K_F11:
                        pygame.display.set_mode((0,0), pygame.FULLSCREEN)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        self.is_mouse_pressed = True

                    if pygame.mouse.get_pressed()[2]:
                        self.is_mouse_pressed_right = True

                if event.type == pygame.MOUSEBUTTONUP:
                    self.is_mouse_pressed = False

            self.position = pygame.mouse.get_pos()

            screen.fill(BLACK)

            self.run_display_cards()
            self.UI.run(self.position, self.is_mouse_pressed)

            self.player_1.display_cards_obj(self.is_mouse_pressed, True)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.main()