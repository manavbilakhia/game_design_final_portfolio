"""

Author: John Rieffel
Manav Bilakhia

Based off of 

Simpson College Computer Science Material

Game art from Kenney.nl:
http://opengameart.org/content/platformer-art-deluxe

"""

import pygame

from player import Player
from platform_generator import Platform_Generator

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    HEIGHT = 768
    WIDTH = 1024
    size = [WIDTH,HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Simple Platformer")

    # Create the player
    player = Player()
    current_world = Platform_Generator(player)

    active_sprite_list = pygame.sprite.Group()
    player.world = current_world
    player.rect.x = 100 
    player.rect.y = HEIGHT - player.rect.height
    active_sprite_list.add(player)

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump(size)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.v.x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.v.x > 0:
                    player.stop()



        # Update the player.
        active_sprite_list.update(size)

        current_world.update()

        #handle right edge
        if player.rect.right > WIDTH:
            player.rect.right = WIDTH

            # handle left edge
        if player.rect.left < 0:
            player.rect.left = 0

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_world.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
