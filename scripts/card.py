from cards_data import *
import pygame
#from main_screen import SCREEN_WIDTH
pygame.init()


class Card:
    def __init__(self, starting_pos, **attributes):
        self.starting_pos = starting_pos
        self.attributes = attributes['attributes']
        self.not_card_attributes = ['set', 'flavor', 'quantity', 'name']
        self.name = self.attributes['name']
        self.card_width = 48
        self.card_height = 10
        self.card_scale = 5
        self.font = CARD_abilities_FONT

        self.card_vector = pygame.Vector2((starting_pos[0], starting_pos[1]))
        self.rect = pygame.rect.Rect((self.card_vector[0], self.card_vector[1]),
                                     (self.card_width * self.card_scale, self.card_height * self.card_scale))
        self.card_surface = pygame.Surface((self.card_width * self.card_scale, self.card_height * self.card_scale))
        self.yellow_mask = pygame.mask.from_surface(self.card_surface)
        self.lines = self.yellow_mask.outline()

        self.card_name_text = CARD_NAME_FONT.render(self.name, False, BLACK)
        self.display_abilities = False
        self.enter_preview = False
        self.prop_pos_dic = self.get_properties_pos()

        self.starting_time = 0
        self.preview_cooldown = 450
        self.can_enter_global = True

        # game settings
        self.cost = self.attributes['cost']
        self.faction = self.attributes['faction']
        self.faction_color = self.faction_color_picker()

    def __len__(self):
        return sum(map(len, self.name.split()))

    def get_properties_pos(self):
        properties_dict = {}
        property_index = 1
        large_properties = ['ally-abilities', 'scrap-abilities', 'abilities']

        if not self.display_abilities:
            for key, value in self.attributes.items():
                if key not in self.not_card_attributes:
                    if key in large_properties:
                        for key2, value2 in value.items():
                            if key == 'ally-abilities':
                                if not self.display_abilities:
                                    property_index += 1
                                    properties_dict.update({'Faction abilities: ': (5, 24 * property_index)})
                                    property_index += 1
                                    if len(self.attributes[key]) >= 2:
                                        for fac_ability, fact_value in self.attributes[key].items():
                                            properties_dict.update({fac_ability: (5, 24 * property_index)})
                                            property_index += 1
                                        self.display_abilities = True
                                        continue

                                    if key2 == 'other-ability':
                                        properties_dict.update({value2: (5, 24 * property_index)})
                                    else:
                                        properties_dict.update({f"{key2}: {value2}": (5, 24 * property_index)})

                                    self.display_abilities = True
                            else:
                                if key2 == 'other-ability':
                                    property_index += 1
                                    properties_dict.update({value2: (5, 24 * property_index)})
                                elif key == 'scrap-abilities':
                                    property_index += 1
                                    properties_dict.update({f"scrap: {key2} {value2}": (5, 24 * property_index)})

                                else:
                                    properties_dict.update({f"{key2}: {value2}": (5, 24 * property_index)})
                                    property_index += 1

                    else:
                        properties_dict.update({f"{key}: {value}": (5, 24 * property_index)})
                        property_index += 1

        return properties_dict

    def faction_color_picker(self):
        color = WHITE

        if self.faction == MACHINE_CULT:
            color = RED

        if self.faction == BLOB:
            color = GREEN

        if self.faction == TRADE_FEDERATION:
            color = BLUE

        if self.faction == STAR_EMPIRE:
            color = YELLOW

        return color

    def display_card(self):
        self.card_surface.blit(self.card_name_text, (5, 2))
        for context, pos in self.prop_pos_dic.items():
            self.card_surface.blit(self.font.render(context, False, BLACK), pos)
        screen.blit(self.card_surface, (self.card_vector[0], self.card_vector[1]))
        self.card_surface.fill(self.faction_color)

    def make_yellow(self):
        for point in self.lines:
            x = point[0] + self.card_vector[0]
            y = point[1] + self.card_vector[1]
            pygame.draw.circle(screen, 'yellow', (x, y), 2.5)

    def preview_card(self, is_mouse_pressed=False):
        if not self.enter_preview and self.can_enter_global:
            #print("Entered preview")
            self.card_width *= 2
            self.card_height = 60
            self.card_surface = None
            self.card_surface = pygame.Surface((self.card_width * self.card_scale, self.card_height * self.card_scale))
            #self.rect.x = 900 - self.rect.width
            #self.rect.y = 400 - self.card_height
            self.enter_preview = True
            self.can_enter_global = False

        elif self.enter_preview:
            #print("closed preview")
            self.enter_preview = False
            self.card_width = 48
            self.card_height = 10
            self.card_surface = pygame.Surface((self.card_width * self.card_scale, self.card_height * self.card_scale))
            self.rect.x = self.starting_pos[0]
            self.rect.y = self.starting_pos[1]
            self.can_enter_global = True

    def drag_card(self, position, is_mouse_pressed, enter_preview_cards):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            if is_mouse_pressed and pygame.time.get_ticks() - self.starting_time > self.preview_cooldown:
                if not enter_preview_cards or self.enter_preview:
                    self.starting_time = pygame.time.get_ticks()
                    self.preview_card(is_mouse_pressed)

    def check_buy_button(self, is_mouse_pressed_right, position) -> bool:
        if position[0] in range(self.rect.left, self.rect.right) and \
                position[1] in range(self.rect.top, self.rect.bottom) and is_mouse_pressed_right:
            return True

        else:
            return False

    def run(self, position, is_mouse_pressed, enter_preview_cards, is_mouse_pressed_right=False):
        self.drag_card(position, is_mouse_pressed, enter_preview_cards)
        self.display_card()
        if self.check_buy_button(is_mouse_pressed_right, position):
            print(True)

    def print_all_attributes(self):
        print(self.attributes)

    def change_card(self, name, random=False):
        self.__init__(starting_pos=(self.rect.x, self.rect.y), attributes=StarRealmsCards(name, random).pick_card())


# scout_card = Card((100, 10),attributes=StarRealmsCards.ALL_STAR_REALMS_CARDS[3])
# scout_card.print_all_attributes()