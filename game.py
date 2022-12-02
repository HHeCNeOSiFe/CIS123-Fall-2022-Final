from functions import *
from puzzles import check_room
from os import system

class Game:
    def __init__(self, player_obj):
        self.player_obj = player_obj

    def get_player_input(self):
        options = get_options(self.player_obj)
        choice = input(f'Choose one of the following:\n{options}\n> ')

        system('cls')

        while choice.upper() not in list(map(str, self.player_obj.location.exits.keys())) + ['I', 'G', 'Q', 'X']:
            system('cls')
            output_text('Sorry, that was an invalid input.\n')
            choice = input(f'Choose one of the following:\n{options}\n> ')

        return choice

    def process_choice(self, input_choice):
        if input_choice.upper() == 'X':
            system('cls')
            self.player_obj.location.examined = True
            if self.player_obj.location.puzzle_solved:
                output_text(self.player_obj.location.long_desc)
            else:
                output_text(self.player_obj.location.puzzle_desc)

        elif input_choice.upper() == 'G':
            system('cls')
            if self.player_obj.location.items:
                thing_to_get = input(f'> What you you like to pick up?\n + {", ".join(i for i in self.player_obj.location.items)}\n> ').title()

                while thing_to_get not in self.player_obj.location.items:
                    system('cls')
                    output_text(f'You can\'t seem to find "{thing_to_get}." Please try again.')
                    thing_to_get = input(f'> What would you like to pick up?\n + {", ".join(i for i in self.player_obj.location.items)}\n> ').title()

                system('cls')
                output_text(f'> You pick up {thing_to_get}.')
                self.player_obj.location.items.remove(thing_to_get)
                self.player_obj.inventory.append(thing_to_get)
            else:
                output_text('There is nothing here relevant to fixing the current damage to the ship.')

        elif input_choice.upper() == 'I':
            check_room(self.player_obj, get_room_name(self.player_obj.location))

        elif input_choice.upper() == 'V':
            system('cls')
            output_text(', '.join([i for i in self.player_obj.inventory]))

        else: #elif choice.upper() not in ['Q', 'X', 'G', 'I']:
            self.player_obj.move_player(input_choice)

            location_name = get_room_name(self.player_obj.location)
            system('cls')
            print(f'You arrive at {location_name}\n')
            sleep(1.0)
            output_text(self.player_obj.location.short_desc + '\n')
            sleep(1.0)

        print('\n' + current_map(self.player_obj))
