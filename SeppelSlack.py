#draft script for traveling salesman problem, wow edition
#coordinates used have been fetched from classicdb.ch

#Copyright Djseppelx of Nostalrius

#imports
import math
from turtle import Turtle, Screen #graphics
def init():
    #read inputs and try to open file
    while True:
        try:
            map_arg = str(input("What zone will you be farming in? "))
            map_arg = map_arg.title()

            node_arg = str(input("What will you be collecting? "))
            node_arg = node_arg.title()

            #fetch the data and setup graphical stuff
            file = open(map_arg + node_arg + ".txt", "r")
            screen = Screen()
            screen.onclick(lambda x, y: screen.update())
            screen.setworldcoordinates(0, 0, 100, 100)
            screen.bgpic(map_arg + node_arg + ".png")
            turtle.color("red")
            turtle.pensize(10)
            break

        except FileNotFoundError:
            print("Could not find any such combination. Try again. Ctrl+C to quit.")

    print("You have opted to farm " + node_arg + " in " + map_arg + ".")

    #Gather coordinates as tuples in an array.
    all_coords = [] #init as empty
    
    for row in file:
        coords = row.split()
        coords[0] = coords[0].strip(',')
        xy_tuple = (float(coords[0]), float(coords[1]))
        all_coords.append(xy_tuple)

    file.close()
    return all_coords

#all_coords now contains all coordinates from the file. Sorted on y-axis.

#attempt #1, nearest neighbour
def nearest_neighbour(all_coords):
    visited_coords = []
    #For every node visited, find nearest node and go there.
    start = all_coords.pop(0)
    visited_coords.append(start)
    current_coord = start
    while (len(all_coords) > 0): #true = still stuff left to visit
        shortest_distance = float("inf") #very BIG
        for i in range(len(all_coords)):
            coord = all_coords[i]
            distance = get_distance_between(current_coord, coord)
            if distance < shortest_distance:
                best_coord_index = i
                shortest_distance = distance
                #print(best_coord_index)
        current_coord = all_coords.pop(best_coord_index)
        visited_coords.append(current_coord)

    visited_coords.append(start) #reconnect to the start
    return visited_coords
    
def get_distance_between(coord1, coord2):
    delta_x = coord1[0] - coord2[0]
    delta_y = coord1[1] - coord2[1]
    distance = float(math.sqrt(delta_x * delta_x + delta_y * delta_y)) # logic here
    return distance

def draw_graph(path):
    #move the turtle
    turtle.setx(path[0][0])
    turtle.sety(path[0][1])
    for i in range(1, len(path)):
        #print("I am supposed to move turtle to: " + path[i])
        turtle.goto(path[i][0], path[i][1])
    return

turtle = Turtle()
all_coords = init()
path = nearest_neighbour(all_coords)
draw_graph(path)
