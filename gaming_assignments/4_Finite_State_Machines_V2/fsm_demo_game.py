##
## Author: Kristina Striegnitz
##
## Version: Fall 2011 
##
## A finite state controlled character wanders around the
## screen. While it is on the green part it wanders slowing; when it
## is on the red it starts running.
##

import pygame
import random

from vector import Vector
from fsm_character import FSMBeakBall
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

    #x = random.randint(0,width)
    #y = random.randint(0,height)
    #c = FSMBeakBall (x, y, 10, 1, pygame.color.Color("darkorange"), 0, 0)

    char_list = []
    objects_in_swarm = 20
    # objects_in_swarm = 100
    x_cords = [random.randint(0, width) for _ in range(objects_in_swarm)]
    y_cords = [random.randint(0, height) for _ in range(objects_in_swarm)]
    [char_list.append(FSMBeakBall(x, y, 10, 1, pygame.color.Color("darkorange"), 0, 0)) for x, y in
     zip(x_cords, y_cords)]

    ## a dictionary to remember which keys are pressed
    keymap = {}

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


        ## Simulate game world



        for character in char_list:
            character.execute_actions()
            character.move(dt, world)
            character.collide_edge (world)
            character.fsm.update(world)

        
        ## Rendering
        # Draw frame
        pygame.draw.rect (my_win, pygame.color.Color("green"), (0,0,width/2,height))
        pygame.draw.rect (my_win, pygame.color.Color("white"), (width/2,0,width/2,height))
        for character in char_list:
            character.draw (my_win)
        #c.draw(my_win)

        # Swap display
        pygame.display.update()

    ## The game loop ends here.

    pygame.quit()


## Start game
run_game()
