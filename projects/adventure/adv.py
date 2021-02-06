from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
#map_file = "projects/adventure/maps/test_loop.txt"
#map_file = "projects/adventure/maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
reverse_direction = {"s": "n", "n": "s", "e": "w", "w":"e"}
backtrack = []
rooms = {}
# Initialize dictionaries and store current room and its exits

first_room = player.current_room.id
exits = player.current_room.get_exits()

#keep track of previous rooms
previous_room = None

print("graph", room_graph)

adjacent_rooms = [player.current_room.get_room_in_direction(direction) for direction in exits]
adjacent_room_IDs = [room.id for room in adjacent_rooms]

print("exits:", exits)
print("adjacent room IDs:", adjacent_room_IDs)
def format_exits(exits):
    dict_exit = {}
    for exit in exits:
        dict_exit[exit] = "?"
    return dict_exit

def travel(direction):
    prev_room_id = player.current_room.id
    player.travel(direction)
    traversal_path.append(direction)
    rooms[player.current_room.id] = format_exits(player.current_room.get_exits())
    rooms[prev_room_id][direction] = player.current_room.id
    rooms[player.current_room.id][reverse_direction[direction]] = prev_room_id
    backtrack.append(reverse_direction[direction])
def get_first_untravel_dir():
    # player.current_room.id 
    curr_room = rooms[player.current_room.id]
    for key, value in curr_room.items():
        print("value", value)
        print("key", key)
        if value == "?":
            return key
    return None
def untraveled(curr_room):
    untraveled_list = []
    for key, value in curr_room.items():
        if value == '?':
            untraveled_list.append(key)
    return untraveled_list

room_visit_path = []
visited = set()

print(len(rooms))
print(len(room_graph))
rooms[player.current_room.id] = format_exits(player.current_room.get_exits())


#print("first", player.current_room.id)

#find and stack first room

#Pop value and set it to current   --- keep track of current
#Visit it if it's not visited   
#Get exits
#Populate world with exits ---> current : {n:"?" ...}
#Choose an exit, first key with value == "?"
#Travel to next room through that exit -- "n"
#Create logic to discover the opposite of exit
#Update path with exit coordinate
#Update world ----> current: {n: 1}
#Create next entry for the "next room", where we are now
#world : {0:{n:1...}, 1:{s:0}}     n is the exit and s is the opposite

#append "next room" to stack
#begin loop again


# while len(rooms) < len(room_graph):
#     direction = get_first_untravel_dir()
#     while player.current_room.get_room_in_direction(direction) is not None:
#         travel(direction)
#     direction = get_first_untravel_dir()
#     print("backtack:", backtrack)
#     print("Traversal path:", traversal_path)
#     if direction == None:

#         for direction in rooms[player.current_room.id]:

#             if rooms[player.current_room.id][direction] == "?":
#                 travel(direction)
#             if len(room_graph) != len(rooms.keys()):
#                 travel(direction)

# get the room exits and mark as unvisited
def get_paths(room):
    paths = {}

    for i in room.get_exits():
        paths[i] = "?"

    return paths

# get the opposite direction
def reverse(direction):
    if direction == "n":
        return "s"
    elif direction == "s":
        return "n"
    elif direction == "e":
        return "w"
    elif direction == "w":
        return "e"

def explore(room, visited = None):
    # if no visited set, create one
    if visited is None:
        visited = set()

    # initialize the traversal path
    traversed_path = []

    # get the possible exits for the current room
    for direction in get_paths(room):
        # travel in available directions
        player.travel(direction)

        # check if room has been visited:
        if player.current_room.id not in visited:
            # add room to visited
            visited.add(player.current_room.id)
            # add the direction to the traversed path
            traversed_path.append(direction)
            # recursively call explore for the new current_room
            traversed_path += explore(player.current_room, visited)
            # travel in the opposite direction
            player.travel(reverse(direction))
            # append the opposite movement to the traversed path
            traversed_path.append((reverse(direction)))
        else:
            # room already visited, travel in opposite direction
            player.travel(reverse(direction))

    return traversed_path

traversal_path = explore(player.current_room)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

'''
# backtracking to go back to room with moves available
backtrack = []
backward_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# track visited rooms
visited = set()

while len(visited) < len(room_graph):
    next_move = None

    for exit in player.current_room.get_exits():
        if player.current_room.get_room_in_direction(exit) not in visited:

            next_move = exit


    if next_move is not None:
        traversal_path.append(next_move)
        backtrack.append(backward_directions[next_move])

        player.travel(next_move)
        visited.add(player.current_room)

    else:
        # backtrack
        next_move = backtrack.pop()

        traversal_path.append(next_move)
        player.travel(next_move)
'''

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
