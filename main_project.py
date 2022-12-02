from os import system
from player import Player
from game import Game
from functions import *
from translator_API_req import intro_translator_API_call

def intro():
    lines = [
        'You find yourself awake, but only partially aware of that fact.',
        'You sit yourself up and try to look around.',
        'You\'re surrounded by smoke and lights.',
        'Your hearing seems to return suddenly, filling your head with the',
        'loud blaring of an alarm.',
        f'{fg.RED + style.BRIGHT + " !WARNING!" + style.RESET_ALL}',
        f'{fg.RED + style.BRIGHT + "   !WARNING!" + style.RESET_ALL}',
        f'{fg.RED + style.BRIGHT + "     !WARNING!" + style.RESET_ALL}',
        intro_translator_API_call('"You are finally awake? That is good. There are things that need attending immediately."'),
        'That was NOT in any language you know. And the voice seemed very robotic.',
        'Could it be that you just don\'t remember... etc.',
        intro_translator_API_call('"You look confused, Astronaut. Is there something wrong?"')
    ]
    
    for line in lines:
        output_text(line + '\n')
        sleep(0.5)
    
    input('Press Enter to continue..')
    system('cls')

# ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- #

if __name__ == '__main__':
    system('cls')
    player = Player()
    game = Game(player)
    intro()
    output_text(current_map(player), 0.005)

    while 'the player has not opted to quit': # I've said this elsewhere, but I love Truthiness
        player_choice = game.get_player_input()
        if player_choice.upper() == 'Q':
            break
        game.process_choice(player_choice)
        player.num_turns += 1

    system('cls')
