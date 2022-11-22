import pygame
class paddle():
    def __init__(self,cols,screen_width,screen_height):
        #define paddle variables
        self.height = 20
        self.width = 700#int(screen_width / cols)
        self.x = int((screen_width / 2) - (self.width / 2))
        self.y = screen_height - (self.height * 2)
        self.speed = 1
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = 0


    def move(self,screen_width):
        #reset movement direction
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
            self.direction = 1

    def draw(self,screen,paddle_col):
        pygame.draw.rect(screen, paddle_col, self.rect)
        #pygame.draw.rect(screen, paddle_outline, self.rect, 3)