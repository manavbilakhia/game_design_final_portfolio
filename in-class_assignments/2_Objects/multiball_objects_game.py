##
## Authors: Kristina Striegnitz, John Rieffel
##
## Version: Fall 2013 
##
## Testing your Ball class.
##cm

import pygame

from ball_2d_novector import *

def run_game():
    
    ## Initialize the pygame submodules and set up the display window.


    pygame.init()

    width = 1024
    height = 768
    my_win = pygame.display.set_mode((width,height))

    
    ballList = []

    b1 = Ball(500,300,10,0,pygame.color.Color('red')  )
    b1.setVelocity(0.1,0.1)
    b1.randomizePosition(width,height)
    b2 = Ball(100,200,20,0,pygame.color.Color('blue') )
    b2.setVelocity(0.1, -0.2)
    b2.randomizePosition(width,height)
    b3 = Ball(10,800,30,0,pygame.color.Color('blue') )
    b3.setVelocity(0.2, -0.1)
    b3.randomizePosition(width,height)
    b4 = Ball(800,800,40,0,pygame.color.Color('blue') )
    b4.setVelocity(-0.1, 0.2)
    b4.randomizePosition(width,height)

    ballList.append(b1)
    ballList.append(b2)
    ballList.append(b3)
    ballList.append(b4)

    ## setting up the clock
    clock = pygame.time.Clock()
    
    ## The game loop starts here.




    keepGoing = True    
    while (keepGoing):


        ## Handle events.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        ## Simulate game world
        for ball in ballList:
            ball.simulate(width,height)
            for otherBall in ballList:
                if ball != otherBall:
                    if ball.checkColision(otherBall):
                        ball.bounceOff(otherBall)





        ## Draw frame
        my_win.fill(pygame.color.Color("black"))

        ## update ball position with current velocity

        for ball in ballList:
            ball.updatePosition()

        ## draw ball in window
        for ball in ballList:
            ball.draw(my_win)
   

    

        ## Swap display

        pygame.display.update()

    ## The game loop ends here.

    pygame.quit()


## Start game
run_game()
