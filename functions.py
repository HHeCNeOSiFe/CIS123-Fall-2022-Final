from time import sleep
from roomData import rooms

# Terminal color definitions.
# Stolen from GitHub -
# credit to Josh Bothun (minism)

class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

class bg:
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'

class style:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET_ALL = '\033[0m'

# ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- #

def output_text(text, speed=0.04):
    '''Prints text one character at a time. As if a computer were talking to you a la 90s cyberpunk.
       The 'join' statement is there to allow better formatting of multi-line strings elsewhere in the program.
       (by splitting the text by newline, removing all line-leading whitespace, and then rejoining with newlines)'''
    for char in '\n'.join([l.lstrip() for l in text.split('\n')]):
        print(char, end='')
        sleep(speed)

def get_room_name(value):
    '''Returns room name for printing elsewhere.'''
    for key, val in rooms.items():
        if value == val:
            return key

# ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- #

def current_map(player_obj):
    '''Returns a string of the current map with a red @ where the player is located.
       Makes choosing which direction to go far simpler.'''
    output = ''
    for ind, char in enumerate(player_obj.location._map):
        if ind == player_obj.location.map_marker_index - 1:
            output += fg.RED        \
                    + style.BRIGHT  \
                    + '@'           \
                    + style.RESET_ALL
        elif char in ['|', '—', '≡', '═']:
            output += fg.CYAN \
                    + style.BRIGHT \
                    + char \
                    + style.RESET_ALL
        else:
            output += char
    output += '\n'
    return output

def get_options(player_obj):
    '''Checks for all exits and outputs all choices in a (#)### format to inform
    the user as to which button to press.  (and interaction options soon?) '''

    directions = {              'U': 'Up',   'D': 'Down',
                'N': 'North', 'W': 'West', 'E': 'East', 'S': 'South'}
                
    options = ', '.join('(' + k + ')' + directions[k][1:] for k in player_obj.location.exits.keys()) + '\n(X)amine surroundings'

    if player_obj.location.examined == True:
        options += ', (G)et an item, (I)nteract'

    options += '\n(V)iew inventory, (Q)uit'

    return options
