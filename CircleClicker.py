# -*- coding: utf-8 -*-
"""
Alexander Harshman
10/29/2021
"""

from graphics import *
from random import choice, random, randint
from math import sqrt

##################################################################################################################################################
"""
This function does the distance formula
    
inputs: x1: The x from the first point
        x2: The x from the second point
        y1: The y from the first point
        y2: The y from the second point
            
outputs: dist: The final distance between the two points
"""
def distance(x1, y1, x2, y2):
    dist = sqrt((((x2 - x1)**2) + (y2 - y1)**2))
    return dist

#####################################################################################################################################################
"""
This function keeps a circle
    
inputs: x: The x from the first point
        y: The y from the first point
        color: What color the circle should be
            
outputs: c: The circle
"""
def circle(x, y, color):
    c = Circle(Point(x, y), 25)
    c.setFill(color)
    return c

#####################################################################################################################################################
"""
This function moves the circle based on a number ramdonly selected from the lists
    
inputs: x: the x from the center of the circle
        y: The y from the center of the circle
        window: The y from the second point
        color: What color the circle should be
            
outputs: x: The new x for the center of the circle
         y: The new y for the center of the circle
"""

def movement (x, y, window, color):
    dx = choice([15, 20, 25, 30, 35])
    dx = choice([1, -1]) * dx
    x += dx
    dy = choice([15, 20, 25, 30, 35])
    dy = choice([1, -1]) * dy
    y += dy
    c = circle(x, y, color).draw(window)
    time.sleep(0.2)
    c.undraw()
    return x, y

########################################################################################################################################################
def main():
    
#Making Graphics Window
    win = GraphWin('Circle Game', 400, 400)

#Introduction
    Intro = Text(Point(200, 100,),'The object of the game is to destroy the circle.  \nThe cicle will move ramdomly around the screen.\nClick the circle twice to destroy it.\nClick to begin').draw(win)
    c = circle(200, 200, 'Green').draw(win)
    win.getMouse()
    
#CountDown
    Intro.undraw()
    c.undraw()
    numberT = Text(Point(200, 200,),'3').draw(win)
    time.sleep(1)
    numberT.undraw()
    numberT = Text(Point(200, 200,),'2').draw(win)
    time.sleep(1)
    numberT.undraw()
    numberT = Text(Point(200, 200,),'1').draw(win)
    time.sleep(1)
    numberT.undraw()
    
#Game

    #Random Starting Spot
    x = randint(100, 300)
    y = randint(100, 300)
    c = circle(x, y, 'Green').draw(win)
    d = 100
    time.sleep(0.2)
    c.undraw()
    
#Counter
    n = 0
    
    #Loops
    while n <= 1:
        
        if n == 0:
            color = 'Green'
        else:
            color = 'Red'
        
        while d > 25:
            
        # Movement function
            x, y = movement(x, y, win, color)
            
        #If the circle hits the border
            if 25 >= x or x >= 375 or 25 >= y or y >= 375:
                n = 20000
                break
            else:
                pass
        
        #Distance between where the player clicks and the center of the circle
            
            #Getting the points where the user clicked
            click = win.checkMouse()
            
            if click == None:
                x2 = 700
                y2 = 700
            else:
                x2 = click.getX()
                y2 = click.getY()
    
            #Actually getting distance
                d = distance(x, y, x2, y2)
        
        
        #Resetting Variables
        d = 100
        n += 1    
        
# Closing screen
    if n > 10:
        t = Text(Point(200, 200,),'YOU LOSE!!')
        t.setSize(36)
        t.draw(win)
        time.sleep(2)
    else:
        t = Text(Point(200, 200,),'You Win')
        t.setSize(12)
        t.draw(win)
        time.sleep(2)

    win.close()
    
main()