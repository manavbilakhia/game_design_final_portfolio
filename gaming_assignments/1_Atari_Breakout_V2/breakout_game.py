import pygame
from pygame.locals import *
from brick import brick
from paddle import paddle

pygame.init()
score = 0
screen_width = 800
screen_height = 1024
#define game variables
cols = 14
rows = 8
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Breakout')
clock = pygame.time.Clock()
FPS = 60
player_paddle = paddle(cols, screen_width, screen_height)


bricks = brick()
bricks.create_bricks(rows, cols)
class game_ball():
    def __init__(self, x, y):
        self.ball_rad = 5
        self.x = x - self.ball_rad
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = 1
        self.speed_y = -1
        self.game_over = 0
        self.speed_max = 5

    def move(self):

        # collision threshold
        collision_thresh = 5

        # start off with the assumption that the wall has been destroyed completely
        wall_destroyed = 1
        row_count = 0
        for row in bricks.blocks:
            item_count = 0
            for item in row:
                # check collision
                if self.rect.colliderect(item[0]):
                    # check if collision was from above
                    if abs(self.rect.bottom - item[0].top) < collision_thresh and self.speed_y > 0:
                        self.speed_y *= -1
                    # check if collision was from below
                    if abs(self.rect.top - item[0].bottom) < collision_thresh and self.speed_y < 0:
                        self.speed_y *= -1
                        # check if collision was from left
                    if abs(self.rect.right - item[0].left) < collision_thresh and self.speed_x > 0:
                        self.speed_x *= -1
                    # check if collision was from right
                    if abs(self.rect.left - item[0].right) < collision_thresh and self.speed_x < 0:
                        self.speed_x *= -1
                    # reduce the block's strength by doing damage to it
                    if bricks.blocks[row_count][item_count][1] > 1:
                        bricks.blocks[row_count][item_count][1] -= 1
                    else:
                        bricks.blocks[row_count][item_count][0] = (0, 0, 0, 0)

                # check if block still exists, in whcih case the wall is not destroyed
                if bricks.blocks[row_count][item_count][0] != (0, 0, 0, 0):
                    wall_destroyed = 0
                # increase item counter
                item_count += 1
            # increase row counter
            row_count += 1
        # after iterating through all the blocks, check if the wall is destroyed
        if wall_destroyed == 1:
            self.game_over = 1

        # check for collision with walls
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1

        # check for collision with top and bottom of the screen
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.bottom > screen_height:
            self.game_over = -1

        # look for collision with paddle
        if self.rect.colliderect(player_paddle):
            # check if colliding from the top
            if abs(self.rect.bottom - player_paddle.rect.top) < collision_thresh and self.speed_y > 0:
                self.speed_y *= -1
                self.speed_x += player_paddle.direction
                if self.speed_x > self.speed_max:
                    self.speed_x = self.speed_max
                elif self.speed_x < 0 and self.speed_x < -self.speed_max:
                    self.speed_x = -self.speed_max
            else:
                self.speed_x *= -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.game_over


    def draw(self,screen):
        pygame.draw.circle(screen, pygame.color.Color("white"), (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)

ball = game_ball(player_paddle.x + (player_paddle.width // 2), player_paddle.y - player_paddle.height)

def end_screen(txt):
    font = pygame.font.Font('BlackOpsOne-Regular.ttf', 70)
    text = font.render(txt, 1, pygame.color.Color("white"))
    text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(text, text_rect)
    pygame.display.update()

run = True
while run:

    screen.fill(pygame.color.Color('black'))

    #draw wall
    bricks.draw_bricks(screen)
    bricks.draw_walls(screen, screen_width, screen_height)
    #draw paddle
    player_paddle.draw(screen, pygame.color.Color('blue'))
    player_paddle.move(screen_width)
    #draw ball
    ball.draw(screen)
    ball.move()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if ball.game_over == -1:
            end_screen("Game Over")
            pygame.time.delay(3000)
            run = False

    font = pygame.font.Font('BlackOpsOne-Regular.ttf', 50)
    text = font.render("Score: " + str(f"{score:03}"), 1, pygame.color.Color("white"))
    screen.blit(text, (80, 120))
    pygame.display.update()
pygame.quit()