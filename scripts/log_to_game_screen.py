import pygame
#import client
from cards_data import UI_FONT, screen
from main_screen import Game
from Input_box import InputBox
import client


class Login:
    def __init__(self):
        self.text_box = InputBox(600, 150, 400, 32, 'Enter you IP here: ')
        self.name_text = InputBox(600, 330, 400, 32, 'Name: ')
        self.events_handles = [self.text_box, self.name_text]
        self.enter_server = False
        self.running = True

    def enter_name(self):
        self.enter_server = True
        text = UI_FONT.render('Connection Successful!', True, (255, 0, 0))
        text2 = UI_FONT.render('Enter your name: ', True, (255, 0, 0))
        screen.blit(text, (600, 210))
        screen.blit(text2, (600, 270))

        self.name_text.update()
        self.name_text.draw(screen)

    def main(self):
        welcome_text = UI_FONT.render('Star Realms!', True, (255, 0, 0))
        to_play = UI_FONT.render('to play...', True, (255, 0, 0))
        game: Game = Game()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    exit()
                    break

                for box in self.events_handles:
                    box.handle_event(event)

            if self.text_box.pressed_enter and not self.enter_server:
                print(self.text_box.text_input)
                try:
                    client.connect(self.text_box.text_input)
                except Exception:
                    print("Connection failed")

                self.text_box.pressed_enter = False

            if self.name_text.pressed_enter:
                if client.send_name(self.name_text.text_input):
                    client.start_receive()
                    game.main()
                self.name_text.pressed_enter = False

            screen.fill('black')

            self.text_box.update()
            self.text_box.draw(screen)

            screen.blit(welcome_text, (600, 50))
            screen.blit(to_play, (600, 100))

            if client.is_connection:
                self.enter_name()

            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    game = Login()
    game.main()
