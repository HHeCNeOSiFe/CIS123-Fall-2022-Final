from functions import *
import roomData

# for room in roomData.rooms:
#     print(room)

def check_room(player, room):
    # get_room_name(player.location) = 'Quarters'

    # Puzzle 1
    if room == 'Energy Storage':
        if 'EJ7 Interlock' in player.inventory:
            player.location.puzzle_solved = True
    
    elif room == 'Operations':
        if roomData.rooms['Energy Storage'].puzzle_solved == True:
            player.location.puzzle_solved = True

    # Puzzle 2
    elif room == 'Engine Room - Starboard':
        if  'Flux Coupler' in player.inventory and \
            'Thermal Regulator' in player.inventory and \
            'Phase Modulator' in player.inventory:

            player.location.puzzle_solved = True
    
    # Puzzle 3
    elif room == 'Engine Room - Port':
        if player.num_turns < 100:
            if 'Small Extinguisher' in player.inventory:
                player.location.puzzle_solved = True
        elif player.num_turns < 200:
            if 'Large Extinguisher' in player.inventory:
                player.is_burned = True
                player.location.puzzle_solved = True
        elif player.num_turns >= 200:
            #FIXME Game over, man! Game over!
            pass

    # Puzzle 4
    elif room == 'Recreation':
        if roomData.rooms['Communications'].examined == True:
            if roomData.rooms['Recreation'].examined == True:
                player.location.puzzle_solved = True

    elif room == 'Comm. Satellites':
        if roomData.rooms['Recreation'].puzzle_solved == True:
            player.location.puzzle_solved = True
    
    elif room == 'Communications':
        if roomData.rooms['Comm. Satellites'].puzzle_solved == True:
            player.locaiton.puzzle_solved = True
    
    # Puzzle 5  --  I'd love for this one to be far more complex but I have neither the time nor the expertise, I think.
    elif room == 'A.I. Interface':
        if 'Code Binder' in player.inventory:
            player.location.puzzle_solved = True
    
    elif room == 'Control':
        if roomData.rooms['A.I. Interface'].puzzle_solved == True:
            player.location.puzzle_solved = True

    # Puzzle 0?  --  This was the one I was using for debugging because it was 'simple'. Ha. I'm still learning..
    elif room == 'Storage - Starboard':
        player.location.puzzle_solved = True
    
    elif room == 'Quarters':
        if roomData.rooms['Storage - Starboard'].puzzle_solved == True:
            player.location.puzzle_solved = True