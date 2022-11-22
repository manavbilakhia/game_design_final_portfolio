##
## Author: Kristina Striegnitz
## Author: John Rieffel
## Author: Manav Bilakhia
##
## Version: Fall 2022 
##
## A character shows a simple seek behavior that makes it move towards
## a target.
##

import pygame
import random

from vector import Vector
from steering_ball import SteeringBall
from moving_ball_2d import MovingBall
from world import World

def run_game():
    
    ## Initialize the pygame submodules and set up the display window.
    pygame.init()

    width = 1024
    height = 768
    my_win = pygame.display.set_mode((width,height))

    ## setting up the game world
    world = World (width, height)

    ## our character
    char_list = []
    objects_in_swarm = 5
    # objects_in_swarm = 100
    x_cords = [random.randint(0,width) for _ in range(objects_in_swarm)]
    y_cords = [random.randint(0,height) for _ in range(objects_in_swarm)]
    [char_list.append(SteeringBall (x, y, 10, 1, pygame.color.Color("darkorange"), 0, 0)) for x,y in zip(x_cords,y_cords)]


    ## the target
    target = MovingBall (150, 175, 20, float('inf'), pygame.color.Color("red"), 0, 0)
    
    ## setting up the clock
    clock = pygame.time.Clock()
    dt = 0
    
    ## The game loop starts here.

    keepGoing = True    
    while (keepGoing):

        dt = clock.tick()
        if dt > 500:
            continue

        ## Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                


        mousepos = pygame.mouse.get_pos()
        mousepos = Vector(mousepos[0],mousepos[1])
        target.p = mousepos
        
        ## Simulate game world
        target.move (dt, world)
        target.collide_edge (world)

        center_of_mass = Vector(0, 0)
        for character in char_list:
            center_of_mass += character.p
        center_of_mass = center_of_mass / len(char_list)
        centroid_ball = MovingBall(center_of_mass.x, center_of_mass.y, 20, float('inf'),
                                   pygame.color.Color("darkgreen"), 0, 0)
        for character in char_list:
            character.steering = []
            character.flee(target, 1.0/30)
            character.cohesion(centroid_ball, 1.0/30)
            character.separation(char_list, 3.0)
            character.align(char_list, 1.0/30)
            character.apply_steering()
            character.move(dt, world)
            character.collide_edge (world)



        ## Rendering
        # Draw frame
        my_win.fill(pygame.color.Color("gray14"))

        target.draw(my_win)
        for character in char_list:
            character.draw(my_win)
        centroid_ball.draw(my_win)

        # Swap display
        pygame.display.update()

    ## The game loop ends here.

    pygame.quit()


## Start game
run_game()
