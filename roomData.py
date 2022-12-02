from dataclasses import dataclass


with open('maps.txt', 'r', encoding='utf-8') as map_data:
    map_lines = map_data.read().split('\n')
    maps = []
    for i in [0, 12, 24, 36]:
        maps.append(''.join([line + '\n' for line in map_lines[i:i+11]]))
    map1, map2, map3, map4 = maps

@dataclass
class Room:
    short_desc: str
    long_desc: str
    puzzle_desc: str
    puzzle_solved: bool
    exits: dict
    items: list
    _map: str
    map_marker_index: int
    visited: bool          # <-- this one may be deprecated
    examined: bool

rooms = {
    'Communications':           Room('''There is a large panel in front of you, covered in knobs, screens, and lights.''',
                  '''''',
                  '''''',
                  None,
                  {'E': 'Control', 'S': 'A.I. Interface'}, [],
                  map1, 25, False, False),

    'Control':                  Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'W': 'Communications', 'E': 'Operations', 'S': 'Hall - Bow'}, [],
                  map1, 33, False, False),

    'Operations':               Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'W': 'Control', 'S': 'Medbay'}, [],
                  map1, 41, False, False),

    'A.I. Interface':           Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'N': 'Communications'}, [],
                  map1, 113, False, False),

    'Hall - Bow':               Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'N': 'Control', 'E': 'Medbay', 'S': 'Ladder/Airlock - Bow'}, ['Flux Coupler'],
                  map1, 121, False, False),

    'Medbay':                   Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'N': 'Operations', 'W': 'Hall - Bow'}, [],
                  map1, 173, False, False),

    'A.I. Mainframe':           Room('''''',     # There's really no point in having this room coded, but I'm keeping it...
                  '''''',                        # ...for posterity!
                  '''''',
                  None,
                  {}, [],
                  map1, 201, False, False),

    'Ladder/Airlock - Bow':     Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'D': 'Ladder - Bow', 'N': 'Hall - Bow', 'S': 'Airlock Landing'}, [],
                  map1, 209, False, False),

    'Recreation':               Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'E': 'Hall - Midship', 'S': 'Mess Hall'}, [],
                  map2, 69, False, False),

    'Ladder - Bow':             Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'U': 'Ladder/Airlock - Bow', 'S': 'Hall - Midship'}, [],
                  map2, 33, False, False),

    'Hygeine':                  Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'S': 'Quarters'}, ['EJ7 Interlock'],
                  map2, 41, False, False),

    'Hall - Midship':           Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'N': 'Ladder - Bow', 'W': 'Recreation', 'E': 'Quarters', 'S': 'Ladder - Stern'}, ['Thermal Regulator'],
                  map2, 121, False, False),

    'Quarters':                 Room('''There are two bunkbeds recessed into the wall and two cryo-beds nearby.
                                        It looks like the bathroom is to the north and the door to the west leads to the central chamber
                                        of this floor of the ship.''',
                  '''You solved the puzzle!''',
                  '''As you look around you notice that on the cryo-bed next to the one you were just in there is a light flashing red.
                    You follow the prompts on the cryo-bed interface and see that the power source has become disconnected.
                    Hopefully that doesn't mean 'damaged' as you're pretty sure you're running low on backups.
                    You should go check the connection. If you remember correctly, it is located in the floor of the room above.''',
                  False,
                  {'N': 'Hygeine', 'W': 'Hall - Midship'}, [],
                  map2, 173, False, False),

    'Mess Hall':                Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'N': 'Recreation'}, [],
                  map2, 201, False, False),

    'Ladder - Stern':           Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'U': 'Ladder/Airlock - Stern', 'N': 'Hall - Midship'}, [],
                  map2, 209, False, False),

    'Storage - Port':           Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'S': 'Engine Room - Port'}, [],
                  map3, 25, False, False),

    'Ladder/Airlock - Stern':   Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'D': 'Ladder - Stern', 'N': 'Airlock Landing', 'S': 'Hall - Stern'}, [],
                  map3, 33, False, False),

    'Storage - Starboard':      Room('''This storage room is filled with boxes with various labels.
                                        There seems to be a removeable panel in the floor.
                                        The engine room you came from is to the south.''',
                  '''''',
                  '''You open the panel in the floor to reveal the inner workings of a complex power system.
                     One of the cables seems to have obviously come loose.''',
                  False,
                  {'S': 'Engine Room - Starboard'}, [],
                  map3, 41, False, False),

    'Engine Room - Port':       Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'N': 'Storage - Port', 'E': 'Hall - Stern'}, ['Small Extinguisher'],
                  map3, 157, False, False),

    'Hall - Stern':             Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'N': 'Ladder/Airlock - Stern', 'W': 'Engine Room - Port', 'E': 'Engine Room - Starboard', 'S': 'Warp Core'}, ['Phase Modulator'],
                  map3, 121, False, False),

    'Engine Room - Starboard':  Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'N': 'Storage - Starboard', 'W': 'Hall - Stern'}, ['Large Extinguisher'],
                  map3, 173, False, False),

    'Warp Core':                Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'N': 'Hall - Stern'}, ['Code Binder'],
                  map3, 209, False, False),

    'Comm. Satellites':         Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'E': 'Airlock Landing'}, [],
                  map4, 113, False, False),

    'Airlock Landing':          Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'N': 'Ladder/Airlock - Bow', 'W': 'Comm. Satellites', 'E': 'Energy Storage', 'S': 'Ladder/Airlock - Stern'}, [],
                  map4, 121, False, False),

    'Energy Storage':           Room('''''',
                  '''''',
                  '''''',
                  None,
                  {'W': 'Airlock Landing'}, [],
                  map4, 129, False, False)
}
