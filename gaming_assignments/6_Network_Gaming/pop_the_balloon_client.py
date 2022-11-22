##
## Author: Kristina Striegnitz
## Author:  John Rieffel
##
## Version: Fall 2022
##
## An incomplete implementation of a client for the multiplayer
## networked balloon popping game.

import pygame, select
import socket

def you_have_a_message (a_socket):
    """
    This function checks whether there is a message waiting to be
    received.
    """

    [in_msgs, out, err] = select.select([a_socket], [], [], 0)
    if len(in_msgs) > 0:
        return True
    else:
        return False


def run_game():

    ## Initialize the pygame submodules and set up the display window.

    pygame.init()

    width = 800
    height = 600
    my_win = pygame.display.set_mode((width,height))

    UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_host = "localhost"
    server_port = 7000
    server_addr = (server_host, server_port)

    mouse_x, mouse_y = 0,0
    ## Load resources

    balloon = pygame.image.load("red_balloon.gif")
    balloon = balloon.convert()

    pop_sound = pygame.mixer.Sound("pop.wav")

    myFont = pygame.font.Font(None,30)

    ## Initialize game objects

    # balloon positions
    b_x = 100
    b_y = 100
    b_xv = 0
    b_yv = 0


    score = 0
    scorelist = []

    name = ""

    clock = pygame.time.Clock()

    ## Initialize loop variables
    intro = True
    keepGoing = True

    #########
    ## The intro screen: lets the player input a name
    #########
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                keepGoing = False

            elif event.type==pygame.KEYDOWN:

                if event.key >= 65 and event.key <= 122:
                    name += chr(event.key)

                if event.key == 13:
                    intro = False

        ## Draw picture and update display
        my_win.fill(pygame.color.Color("darkblue"))

        label = myFont.render("Please enter your name: "+name, True, pygame.color.Color("magenta"))
        my_win.blit(label, (50,height/2-100))

        label = myFont.render("Then hit 'Enter' to start.", True, pygame.color.Color("magenta"))
        my_win.blit(label, (50,height/2-50))

        pygame.display.update()



    ###########
    ## The main game loop: We are using a time based game loop so that
    ## it doesn't matter if the framerate on the server and on the
    ## client computers aren't the same.
    ###########

    ## connect to the server
    msg = "connect "+name
    UDP_sock.sendto(msg.encode('utf-8'), server_addr)

    dt = clock.tick()
    while (keepGoing):

        dt = clock.tick()
        
        ## Handle events.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                message = 'click ' + str(int(mouse_x)) + ' ' + str(int(mouse_y))
                UDP_sock.sendto(message.encode('utf-8'), server_addr)
                print("i clicked at position ", mouse_x, mouse_y)


        ## Update game objects

        b_x = b_x + b_xv * dt
        b_y = b_y + b_yv * dt

        # handle messages from the server

        # Uncomment the following lines of code. They check whether
        # there is a message from the server waiting and if so,
        # extract the message string and the address of the sender
        # (which should be the server
        if you_have_a_message(UDP_sock):
           received_string, sender = UDP_sock.recvfrom(1024)
           received_string = received_string.decode('utf-8')


           # Write code to handle "position" messages
           #print("sending message")

           received_string = received_string.split()
           if received_string[0] == 'position':
               b_x = float(received_string[1])
               b_y = float(received_string[2])
               b_xv = float(received_string[3])
               b_yv = float(received_string[4])

           # Write code to handle "scores" messages
           elif received_string[0]=='scores':
               for score in received_string[1:]:
                   scorelist = score.split(':')


           # Write code to handle "hit" messages
           elif received_string[0] =='hit':
               print(received_string[1:])
               pop_sound.play()
 

        ## Draw picture and update display

        my_win.fill(pygame.color.Color("darkblue"))


        # score
        x = 10
        y = 10
        label = myFont.render("Your score: "+str(score), True, pygame.color.Color("magenta"))
        my_win.blit(label, (x,y))

        # Write code to display other player's scores
        x = 10
        y = 50
        for i in range(3,len(scorelist)-1):
            label = myFont.render(scorelist[i] + ":" +scorelist[i+1], True, pygame.color.Color("magenta"))
            my_win.blit(label, (x,y))
            y = y + 40
            i+=1

        # balloon images
        my_win.blit(balloon,(int(b_x), int(b_y)))

        pygame.display.update()

    ## The game loop ends here.
    #disconnect should tell the server you have disconnected when the game loop ends
    msg = "disconnect"
    UDP_sock.sendto(msg.encode('utf-8'), server_addr)


    pygame.quit()


## Call the function run_game.

run_game()
