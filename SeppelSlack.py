#draft script for traveling salesman problem, wow edition
#coordinates used have been fetched from classicdb.ch

#Copyright Djseppelx and 'Niggma of Nostalrius

#imports for calculation
import math

#imports for graphics
from tkinter import *
from tkinter.ttk import *
from turtle import Turtle, Screen

# TODO: Align the used background image with the canvas better

# TODO: Menu with a few buttons (toggle the removal of nodes on/off).

# TODO: Add functionality for un-toggling of nodes... how do we do this?
# Would need to save a graphics window temporarily or smth.
# This could be tricky.

# TODO: Figure out why all_coords are zero after the nearest_neighbour call,
# even with the temp variables.

# TODO: Proper wait-state functionality, not a constant looping (tkinter mainloop)

def init():
    #read inputs and try to open file
    while True:
        try:
            #fetch the data and setup graphical stuff
            map_arg = str(input("What zone will you be farming in? "))
            map_arg = map_arg.title()

            node_arg = str(input("What will you be collecting? "))
            node_arg = node_arg.title()

            file = open(map_arg + node_arg + ".txt", "r")
            screenloader_helper(map_arg, node_arg);
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

def screenloader_helper(map_arg, node_arg):
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
    return

#attempt #1, nearest neighbour
def nearest_neighbour(all_coords):
    temp = all_coords #store all_coords if we need it later.
    visited_coords = []
    start = all_coords.pop(0)
    visited_coords.append(start)
    current_coord = start
    while (len(all_coords) > 0): #true = still stuff left to visit
        shortest_distance = float("inf") #very BIG
        #For every node visited, find nearest other node and go there.
        for i in range(len(all_coords)):
            coord = all_coords[i]
            distance = get_distance_between(current_coord, coord)
            if distance < shortest_distance:
                best_coord_index = i
                shortest_distance = distance
        current_coord = all_coords.pop(best_coord_index)
        visited_coords.append(current_coord)

    visited_coords.append(start) #reconnect to the start
    all_coords = temp #give back the coords, used in other functions
    #above line currently not working?
    return visited_coords

def get_distance_between(coord1, coord2):
    delta_x = coord1[0] - coord2[0]
    delta_y = coord1[1] - coord2[1]
    distance = float(math.sqrt(delta_x * delta_x + delta_y * delta_y))
    return distance

def draw_graph(path):
    #move the turtle
    turtle.setx(path[0][0])
    turtle.sety(path[0][1])
    turtle.pendown()
    for i in range(0, len(path)):
        turtle.goto(path[i][0], (path[i][1]))
    return

def toggle_node(xCoord, yCoord):
    toggled_coord = (xCoord, yCoord)
    print("xCoord :" + str(xCoord) + " yCoord: " + str(yCoord))
    radius = 1 #parameter for node toggling
    for i in range(len(path)):
        distance = get_distance_between(toggled_coord, path[i])
        if distance < 1: #very close
            turtle.penup() #don't paint when we move
            turtle.goto(xCoord, yCoord - radius/2)
            turtle.pendown() #paint the circle
            turtle.circle(radius, 360) #small circle
            disabled_coords.append(path[i])
    return
        
turtle = Turtle()
screen = Screen()
all_coords = init()
disabled_coords = [] #initially empty
path = nearest_neighbour(all_coords)
draw_graph(path)
screen.onscreenclick(toggle_node)
turtle.getscreen()._root.mainloop()
