import pygame
from brick import Brick
from paddle import Paddle
from ball import Ball

# Initialize the pygame submodules and set up the display window.

pygame.init()

WIDTH = 800
HEIGHT = 1024
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()
FPS = 60

# defining all the atari breakout colors for the screen
BLACK = pygame.color.Color("black")
WHITE = pygame.color.Color("white")
GREY = pygame.color.Color("grey")
BLUE = pygame.color.Color("blue")
score = 0
balls =3
# defining colors for the bricks

RED = pygame.color.Color("red")
GREEN = pygame.color.Color("green")
ORANGE = pygame.color.Color("orange")
YELLOW = pygame.color.Color("yellow")

# defining the paddle
paddle_width = 120
paddle_height = 20

all_sprites_list = pygame.sprite.Group()

# defining the bricks
brick_width = 65
brick_height = 16
brick_gap_x = 7
brick_gap_y = 5
brick_rows = 8
brick_columns = 14


all_bricks = pygame.sprite.Group()

# defining the wall
wall_width = 16

paddle = Paddle(BLUE, paddle_width, paddle_height)
paddle.rect.x = WIDTH // 2 - paddle_width // 2
paddle.rect.y = HEIGHT - 65

ball = Ball(WHITE, 10, 10)
ball.rect.x = WIDTH // 2 - 5
ball.rect.y = HEIGHT // 2 - 5

def draw_lines():
    pygame.draw.line(screen, GREY, [0, 19], [WIDTH, 19], 40)
    pygame.draw.line(screen, GREY, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, HEIGHT], wall_width)
    pygame.draw.line(screen, GREY, [(WIDTH - wall_width / 2) - 1, 0], [(WIDTH - wall_width / 2) - 1, HEIGHT],
                     wall_width)

    pygame.draw.line(screen, BLUE, [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2],
                     [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)
    pygame.draw.line(screen, BLUE, [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2],
                     [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)

    pygame.draw.line(screen, RED, [(wall_width / 2) - 1, 212.5],
                     [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * brick_gap_y], wall_width)
    pygame.draw.line(screen, RED, [(WIDTH - wall_width / 2) - 1, 212.5],
                     [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * brick_gap_y], wall_width)

    pygame.draw.line(screen, ORANGE, [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * brick_gap_y],
                     [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * brick_gap_y], wall_width)
    pygame.draw.line(screen, ORANGE, [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * brick_gap_y],
                     [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * brick_gap_y], wall_width)

    pygame.draw.line(screen, GREEN, [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * brick_gap_y],
                     [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * brick_gap_y], wall_width)
    pygame.draw.line(screen, GREEN, [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * brick_gap_y],
                     [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * brick_gap_y], wall_width)

    pygame.draw.line(screen, YELLOW, [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * brick_gap_y],
                     [(wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * brick_gap_y], wall_width)
    pygame.draw.line(screen, YELLOW, [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * brick_gap_y],
                     [(WIDTH - wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * brick_gap_y], wall_width)


def generate_bricks():
    for j in range(brick_rows):
        for i in range(brick_columns):
            if j < 2:
                if i == 0:
                    brick = Brick(RED, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (brick_gap_y + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(RED, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + brick_gap_x + (i - 1) * (brick_width + brick_gap_x)
                    brick.rect.y = 215 + j * (brick_gap_y + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 1 < j < 4:
                if i == 0:
                    brick = Brick(ORANGE, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (brick_gap_y + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(ORANGE, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + brick_gap_x + (i - 1) * (brick_width + brick_gap_x)
                    brick.rect.y = 215 + j * (brick_gap_y + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 3 < j < 6:
                if i == 0:
                    brick = Brick(GREEN, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (brick_gap_y + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(GREEN, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + brick_gap_x + (i - 1) * (brick_width + brick_gap_x)
                    brick.rect.y = 215 + j * (brick_gap_y + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 5 < j < 8:
                if i == 0:
                    brick = Brick(YELLOW, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (brick_gap_y + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(YELLOW, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + brick_gap_x + (i - 1) * (brick_width + brick_gap_x)
                    brick.rect.y = 215 + j * (brick_gap_y + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)


brick_wall = generate_bricks()
all_sprites_list.add(paddle)
all_sprites_list.add(ball)


def end_screen(txt):
    font = pygame.font.Font('BlackOpsOne-Regular.ttf', 70)
    text = font.render(txt, 1, WHITE)
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.blit(text, text_rect)
    pygame.display.update()


def run_game(balls,score):
    # -------- Main Program Loop -----------
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move_left(10)
        if keys[pygame.K_RIGHT]:
            paddle.move_right(10)

        all_sprites_list.update()
        if ball.rect.y < 40:
            ball.velocity[1] = -ball.velocity[1]

        if ball.rect.x >= WIDTH - wall_width - 10:
            ball.velocity[0] = -ball.velocity[0]

        if ball.rect.x <= wall_width:
            ball.velocity[0] = -ball.velocity[0]

        if ball.rect.y > HEIGHT:
            ball.rect.x = WIDTH // 2 - 5
            ball.rect.y = HEIGHT // 2 - 5
            ball.velocity[0] = ball.velocity[1]
            balls -= 1
            if balls == -1:
                end_screen("GAME OVER")
                pygame.time.wait(2000)
                run = False

        if pygame.sprite.collide_mask(ball, paddle):
            ball.rect.x -= ball.velocity[0]
            ball.rect.y -= ball.velocity[1]
            ball.bounce()

        brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
        for brick in brick_collision_list:
            ball.bounce()
            score += 1
            brick.kill()
        if score ==88:

            end_screen("You Win!")
            pygame.time.wait(2000)

            run = False



        screen.fill(BLACK)

        draw_lines()

        all_sprites_list.draw(screen)
        font = pygame.font.Font('BlackOpsOne-Regular.ttf', 50)
        text = font.render("Score: "+str(f"{score:03}"), 1, WHITE)
        screen.blit(text, (80, 120))
        text = font.render("Lives: "+str(balls), 1, WHITE)
        screen.blit(text, (500, 120))
        text = font.render('', 1, WHITE)
        screen.blit(text, (580, 120))
        text = font.render('', 1, WHITE)
        screen.blit(text, (20, 40))
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    run_game(balls,score)
