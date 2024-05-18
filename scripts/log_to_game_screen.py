import pygame
#import client
from cards_data import UI_FONT, screen
from main_screen import Game
from Input_box import InputBox
import client

events_handles = []


def enter_name():
    text = UI_FONT.render('Connection Successful!', True, (255, 0, 0))
    text2 = UI_FONT.render('Enter your name: ', True, (255, 0, 0))
    screen.blit(text, (600, 210))
    screen.blit(text2, (600, 270))

    name_text.update()
    name_text.draw(screen)


def main():
    welcome_text = UI_FONT.render('Star Realms!', True, (255, 0, 0))
    to_play = UI_FONT.render('to play...', True, (255, 0, 0))

    global events_handles, name_text
    text_box = InputBox(600, 150, 400, 32, 'Enter you IP here: ')
    name_text = InputBox(600, 330, 400, 32, 'Name: ')
    running = True
    events_handles = [text_box, name_text]

    game: Game = Game()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
                break

            for box in events_handles:
                box.handle_event(event)

        if text_box.pressed_enter:
            print(text_box.text_input)
            try:
                client.connect(text_box.text_input)
            except Exception:
                print("Connection failed")

            text_box.pressed_enter = False

        if name_text.pressed_enter:
            if client.send_name(name_text.text_input):
                client.start_receive()
                game.main()
            name_text.pressed_enter = False

        screen.fill('black')

        text_box.update()
        text_box.draw(screen)

        screen.blit(welcome_text, (600, 50))
        screen.blit(to_play, (600, 100))

        if client.is_connection:
            enter_name()

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()