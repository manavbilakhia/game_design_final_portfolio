# I affirm that I have carried out my academic endeavors with full academic honesty.
# @MB (Manav Bilakhia)
# read the readme file for more information on how to run this script
import pygame
import random
from time import sleep

def nightsky():
    # Initialize pygame and set up the display window.
    pygame.init()
    width = 800
    height = 600
    radius = 4
    color = pygame.color.Color("Yellow")
    num_stars = random.randint(50,100)
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Nightsky")
    # initialize variables for the stars
    x = [random.randint(0,width) for _ in range(num_stars)] # x coordinates of the stars
    y = [random.randint(0,height) for _ in range(num_stars)] # y coordinates of the stars
    r = [random.randint(1,radius) for _ in range(num_stars)] # radius of the stars
    done = False
    # The game loop starts here.
    while not done:
        # 1. Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # 2. Draw ball
        for i in range(num_stars):
            pygame.draw.circle(screen, color, (x[i],y[i]),r[i])
        pygame.display.update()
    pygame.quit()

def failed_nightsky():
    pygame.init()
    width = 800
    height = 600
    radius = 4
    max_length = 100
    min_length = 10
    color = pygame.color.Color("Yellow")
    num_stars = random.randint(50,100)
    num_shooting_stars = random.randint(0,15)
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Nightsky")

    x = [random.randint(0,width) for _ in range(num_stars)]
    y = [random.randint(0,height) for _ in range(num_stars)]
    r = [random.randint(1,radius) for _ in range(num_stars)]


    shooting_star_x = [random.randint(0,width) for _ in range(num_shooting_stars)]
    shooting_star_y = [random.randint(0,height) for _ in range(num_shooting_stars)]
    shooting_star_length = [random.randint(min_length,max_length) for _ in range(num_shooting_stars)]

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        for i in range(num_stars):
            pygame.draw.circle(screen, color, (x[i],y[i]),r[i])
        for j in range(num_shooting_stars):
            pygame.draw.circle(screen, color, (shooting_star_x[j],shooting_star_y[j]),r[j])
            pygame.draw.line(screen, color, (shooting_star_x[j],shooting_star_y[j]),(shooting_star_x[j]+shooting_star_length[j], shooting_star_y[j]+shooting_star_length[j]),1)
            pygame.draw.circle(screen, color, (shooting_star_x[j] + shooting_star_length[j], shooting_star_y[j] + shooting_star_length[j]), r[j])
        pygame.display.update()
    pygame.quit()

def failed_nightsky2():
    #initialize pygame and setup display window
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Nightsky")


    # initialize variables for the stars
    num_stars = random.randint(50, 100)
    num_shooting_stars = random.randint(0, 30)
    radius = 4
    color = pygame.color.Color("Yellow")
    static_color = pygame.color.Color("Yellow")

    x = [random.randint(0, width) for _ in range(num_stars)]
    y = [random.randint(0, height) for _ in range(num_stars)]
    r = [random.randint(1, radius) for _ in range(num_stars)]

    shooting_star_x = random.randint(0, width)
    shooting_star_y = random.randint(0, height)
    copy_shooting_star_y = shooting_star_y
    shooting_star_length = random.randint(20, 100)
    speed = 5
    done = False
    # game loop starts here
    while not done:
        # 1. Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # 2. Apply rules of the world

        # 3. Simulate the World



        shooting_star_y += speed
        shooting_star_x += speed
        if shooting_star_y > copy_shooting_star_y + shooting_star_length:
            color = pygame.color.Color("Black")

        #4. Draw Frame

        # Draw Background
        screen.fill((0, 0, 0)) # black background

        # Draw Stars
        for i in range(num_stars):
            pygame.draw.circle(screen, static_color, (x[i], y[i]), r[i])
        for j in range(num_shooting_stars):
            pygame.draw.circle(screen, color, (shooting_star_x, shooting_star_y), r[j])
            sleep(0.00005)
            pygame.draw.circle(screen, color, (shooting_star_x+j, shooting_star_y+j), r[j])
            sleep(0.00005)
            pygame.draw.circle(screen, color, (shooting_star_x+j, shooting_star_y+j), r[j])
            sleep(0.00005)
            pygame.draw.circle(screen, color, (shooting_star_x+j, shooting_star_y+j), r[j])
            sleep(0.00005)
            pygame.draw.circle(screen, color, (shooting_star_x+j, shooting_star_y+j), r[j])
            sleep(0.00005)
            pygame.draw.circle(screen, color, (shooting_star_x + j, shooting_star_y + j), r[j])
            sleep(0.000005)
            pygame.draw.circle(screen, color, (shooting_star_x + j, shooting_star_y + j), r[j])
            sleep(0.00005)
            pygame.draw.circle(screen, color, (shooting_star_x + j, shooting_star_y + j), r[j])
            sleep(0.00005)
            pygame.draw.circle(screen, color, (shooting_star_x + j, shooting_star_y + j), r[j])
            sleep(0.00005)
            pygame.draw.circle(screen, color, (shooting_star_x + j, shooting_star_y + j), r[j])
            sleep(0.00005)
            pygame.draw.circle(screen, color, (shooting_star_x + j, shooting_star_y + j), r[j])
            sleep(0.00005)
            pygame.draw.circle(screen, color, (shooting_star_x + j, shooting_star_y + j), r[j])
            sleep(0.00005)
            pygame.draw.circle(screen, color, (shooting_star_x + j, shooting_star_y + j), r[j])

        #  swap display
        pygame.display.update()
    # end game loop
    pygame.quit()

def failed_nightsky3():
    #initialize pygame and setup display window
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Nightsky")


    # initialize variables for the stars
    num_stars = random.randint(50, 100)
    num_shooting_stars = random.randint(0, 15)
    radius = 4
    color = pygame.color.Color("Yellow")

    x = [random.randint(0, width) for _ in range(num_stars)]
    y = [random.randint(0, height) for _ in range(num_stars)]
    r = [random.randint(1, radius) for _ in range(num_stars)]

    shooting_star_x = [random.randint(0, width) for _ in range(num_shooting_stars)]
    shooting_star_y = [random.randint(0, height) for _ in range(num_shooting_stars)]
    copy_shooting_star_y = shooting_star_y
    shooting_star_length = random.randint(20, 100)
    speed = 0.1
    done = False
    # game loop starts here
    while not done:
        # 1. Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # 2. Apply rules of the world

        # 3. Simulate the World

        for i in range(num_shooting_stars):
            shooting_star_y[i] += speed
            shooting_star_x[i] += speed
            if shooting_star_y[i] > copy_shooting_star_y[i] + shooting_star_length:
                color = pygame.color.Color("Black")

        #4. Draw Frame

        # Draw Background
        screen.fill((0, 0, 0)) # black background

        # Draw Stars
        for i in range(num_stars):
            pygame.draw.circle(screen, (255, 255, 255), (x[i], y[i]), r[i])
        for j in range(num_shooting_stars):
            pygame.draw.circle(screen, color, (shooting_star_x[j], shooting_star_y[j]), r[j])
        #  swap display
        pygame.display.update()
    # end game loop
    pygame.quit()

if __name__ == '__main__':

    user_input = int(input("Enter '1' to see a static night sky. Enter '2' picture of a night sky with a couple of shooting "
                           "stars. Enter '3' to see one shooting star withh a stary background. Enter 4 for a cool multistar animation: "))
    if user_input == 1:
        nightsky()
    elif user_input == 2:
        failed_nightsky()
    elif user_input == 3:
        failed_nightsky2()
    elif user_input == 4:
        failed_nightsky3()
    else:
        print("Invalid input. Please run the file again as instructed in the readme and give a correct choice")