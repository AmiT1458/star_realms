from crads_data import StarRealmsCards
import pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CARD_NAME_FONT = pygame.font.SysFont('Gameplay,', 32)
CARD_abilities_FONT = pygame.font.SysFont('Gameplay,',25)


class Card:
    def __init__(self,starting_pos, **attributes):
        self.attributes = attributes['attributes']
        self.not_card_attributes = ['set', 'flavor', 'quantity', 'name']
        self.name = self.attributes['name']
        self.card_width = 43
        self.card_height = 57
        self.card_scale = 5
        self.rect = pygame.rect.Rect((starting_pos[0], starting_pos[1]),
                                     (self.card_width * self.card_scale, self.card_height * self.card_scale))
        self.card_surface = pygame.Surface((self.card_width * self.card_scale, self.card_height * self.card_scale))
        self.card_name_text = CARD_NAME_FONT.render(self.name, True, BLACK)
        self.display_abilities = False
        self.prop_pos_dic = self.get_properties_pos()
        self.change_x = 0
        self.change_y = 0

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

                                    else:
                                        properties_dict.update({key2: (5, 24 * property_index)})

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

    def display_card(self, screen):
        self.card_surface.blit(self.card_name_text, (self.card_surface.get_width() // 2 - 70, 2))
        for context, pos in self.prop_pos_dic.items():
            self.card_surface.blit(CARD_abilities_FONT.render(context, True, BLACK), pos)
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


scout_card = Card((100, 10),attributes=StarRealmsCards.ALL_STAR_REALMS_CARDS[3])
#scout_card.print_all_attributes()