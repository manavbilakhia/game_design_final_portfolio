import pygame
from simple_platform import Box


class Platform_Generator(object):


    def __init__(self, player):

        self.platform_list = pygame.sprite.Group()
        self.player = player


        self.background = None
        # platforms
        # height, weight, x, y
        platforms = [[35, 210, 500, 700],
                 [35, 210, 200, 600],
                 [35, 210, 550, 550],
                 [35, 210, 700, 400],]

        for platform in platforms:
            block = Box(pygame.color.Color('yellow'), platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

    def update(self):
        self.platform_list.update()

    def draw(self, screen):
        screen.fill(pygame.color.Color("gray14"))
        self.platform_list.draw(screen)


