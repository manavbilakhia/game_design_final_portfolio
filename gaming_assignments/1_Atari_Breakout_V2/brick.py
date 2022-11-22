import pygame
class brick():
    def __init__(self):
        self.width = 60
        self.height = 16

    def create_bricks(self, rows, cols):
        self.blocks = []
        #define an empty list for an individual block
        block_individual = []
        for row in range(rows):
            #reset the block row list
            block_row = []
            #iterate through each column in that row
            for col in range(cols):
                #generate x and y positions for each block and create a rectangle from that
                block_x = (col * self.width)+16
                block_y = (row * self.height)+215
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                #assign block strength based on row
                if row < 2:
                    strength = 4
                elif row < 4:
                    strength = 3
                elif row < 6:
                    strength = 2
                elif row < 8:
                    strength = 1
                #create a list at this point to store the rect and colour data
                block_individual = [rect, strength]
                #append that individual block to the block row
                block_row.append(block_individual)
            #append the row to the full list of blocks
            self.blocks.append(block_row)


    def draw_bricks(self, screen):
        for row in self.blocks:
            for block in row:
                #assign a colour based on block strength
                if block[1] == 4:
                    block_col = pygame.color.Color('red')
                elif block[1] == 3:
                    block_col = pygame.color.Color('orange')
                elif block[1] == 2:
                    block_col = pygame.color.Color('yellow')
                elif block[1] == 1:
                    block_col = pygame.color.Color('green')
                pygame.draw.rect(screen, block_col, block[0])
                pygame.draw.rect(screen, pygame.color.Color('black'), (block[0]), 2)

    def draw_walls(self, screen, screen_width, screen_height):
        GREY = pygame.color.Color("grey")
        BLUE = pygame.color.Color("blue")
        wall_width = 16

        brick_gap_y = 5
        paddle_height = 16

        pygame.draw.line(screen, GREY, [0, 19], [screen_width, 19], 40)
        pygame.draw.line(screen, GREY, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, screen_height], wall_width)
        pygame.draw.line(screen, GREY, [(screen_width - wall_width / 2) - 1, 0], [(screen_width - wall_width / 2) - 1, screen_height],
                         wall_width)

        pygame.draw.line(screen, BLUE, [(wall_width / 2) - 1, screen_height - 65 + paddle_height / 2 - 54 / 2],
                         [(wall_width / 2) - 1, screen_height - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)
        pygame.draw.line(screen, BLUE, [(screen_width - wall_width/ 2) - 1, screen_height - 65 + paddle_height / 2 - 54 / 2],
                         [(screen_width - wall_width/ 2) - 1, screen_height - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)
