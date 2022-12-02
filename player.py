import roomData

class Player:
    '''Sets starting location and empty inventory.
       Allows player to be moved from room to room.'''
    
    def __init__(self):
        self.location = roomData.rooms['Quarters']
        self.inventory = []
        self.num_turns = 0
        self.is_burned = False

    def move_player(self, direction):
        self.location.visited = True
        self.location = roomData.rooms[self.location.exits[direction.upper()]]
