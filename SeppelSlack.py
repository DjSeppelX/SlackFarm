#draft script for traveling salesman problem, wow edition
#coordinates used have been fetched from classicdb.ch

#Copyright Djseppelx and 'Niggma of Nostalrius

#imports for calculation
import math

#imports for graphics
from tkinter import *
from tkinter.ttk import *
from turtle import Turtle, Screen

# TODO: Fix a helper function for importing the graphics,
# the blob in the init() function is ugly.

# TODO: Align the used background image with the canvas better

# TODO: Menu with a few buttons (toggle the removal of nodes on/off).

# TODO: Implement functionality for on-click events.
# Used for "skipping" nodes in the pathing algorithm.

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
            screen.bgpic(map_arg + node_arg + ".png")
            canvas = screen.getcanvas()
            canvas.itemconfig(screen._bgpic, anchor="nw")
            screen.setup(1000, 670)
            screen.setworldcoordinates(0, 100, 100, 0)
            #filename = PhotoImage(file = map_arg + node_arg + ".png")
            #image = canvas.create_image(50, 50, anchor=NW, image=filename)
            turtle.color("red")
            turtle.pensize(5)
            turtle.penup()
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
    turtle.pendown()
    #print(turtle.position())
    for i in range(0, len(path)):
        #print("Moving to x: " + str(path[i][0]) + ", y: " + str(path[i][1]))
        turtle.goto(path[i][0], (path[i][1]))
    return

turtle = Turtle()
all_coords = init()
path = nearest_neighbour(all_coords)
draw_graph(path)
