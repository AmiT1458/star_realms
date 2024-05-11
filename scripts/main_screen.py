from player import Player
from turn import *

pygame.init()
#pygame.font.init()

pygame.display.set_caption("Star realms")

run = True
is_mouse_pressed = False

count_presses = 0
mouse_change = pygame.mouse.get_rel()
enter_preview_cards = False

deck = Manage_Game()
deck.initialize_trade_deck()
deck.run()

player_1 = Player()
player_1.initialize_start()
#player_1.initialize_start()
#player_1.display_hand()

UI = UI()


def unittest_cards():
    print("Starts a turn")
    player_1.start_turn()
    print(player_1.draw_deck)

    print("Ending a turn")
    player_1.end_turn_hand()


current_time = pygame.time.get_ticks()
while run:
    current_time = pygame.time.get_ticks()
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

            if event.key == pygame.K_SPACE:
                cards_to_display[0].change_card()
                # deck.remove_card(cards_to_display[1])
                # print(cards_to_display[1].name)

            if event.key == pygame.K_r:
                player_1.end_turn_start()

            if event.key == pygame.K_w:
                player_1.start_turn()

            if event.key == pygame.K_s:
                player_1.end_turn_hand()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                is_mouse_pressed = True

        if event.type == pygame.MOUSEBUTTONUP:
            is_mouse_pressed = False

    mx, my = pygame.mouse.get_pos()
    mouse_change = pygame.mouse.get_rel()

    screen.fill(BLACK)
    for card in cards_to_display:
        card.run((mx, my), is_mouse_pressed, enter_preview_cards)
        if card.enter_preview:
            enter_preview_cards = True

        elif card.can_enter_global:
            enter_preview_cards = False

    UI.run(player_1)
    player_1.display_cards_obj(is_mouse_pressed, True)
    pygame.display.update()
