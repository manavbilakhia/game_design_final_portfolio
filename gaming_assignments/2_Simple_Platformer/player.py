"""
Derived from code provided at
http://programarcadegames.com/
"""
import pygame


from spritesheet_functions import SpriteSheet
from vector import Vector

class Player(pygame.sprite.Sprite):

    # -- Attributes
    # Set speed vector of player

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []


    # -- Methods
    def __init__(self):
        """ Constructor function """
        #This is ugly, but it came with the example code...

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        self.v = Vector(0,0)

        self.direction = "R"
        self.world = None


        sprite_sheet1 = SpriteSheet("p1_walk_right.png")
        # Load all the right facing images into a list
        image = sprite_sheet1.get_image(0, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet1.get_image(66, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet1.get_image(132, 0, 67, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet1.get_image(0, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet1.get_image(66, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet1.get_image(132, 93, 72, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet1.get_image(0, 186, 70, 90)
        self.walking_frames_r.append(image)
        # Set the image the player starts with


        # Load all the left facing images into a list

        image = sprite_sheet1.get_image(0, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet1.get_image(66, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet1.get_image(132, 0, 67, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet1.get_image(0, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet1.get_image(66, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet1.get_image(132, 93, 72, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet1.get_image(0, 186, 70, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        self.image = self.walking_frames_r[0]


        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

    def update(self,screen_size):
        """ Move the player. """ # big ugly block, maybe break it down more?
        self.calc_grav(screen_size)
        pos = self.rect.x
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        self.simulate_horizontal()
        platform_hit_list = pygame.sprite.spritecollide(self, self.world.platform_list, False)
        for block in platform_hit_list:
            if self.v.x > 0:
                self.rect.right = block.rect.left
            elif self.v.x < 0:
                self.rect.left = block.rect.right
        self.simulate_verticle()
        platform_hit_list = pygame.sprite.spritecollide(self, self.world.platform_list, False)
        for block in platform_hit_list:
            if self.v.y > 0:
                self.rect.bottom = block.rect.top
            elif self.v.y < 0:
                self.rect.top = block.rect.bottom



    def simulate_horizontal(self):
        self.rect.x += self.v.x

    def simulate_verticle(self):
        self.rect.y += self.v.y



    def calc_grav(self,screen_size):
        """ Calculate effect of gravity. """
        if self.v.y == 0:
            self.v.y += 10
        else:
            self.v.y += .35

        #check if on ground
        if self.rect.y >= screen_size[1] - self.rect.height and self.v.y >= 0:
            self.v.y = 0
            self.rect.y = screen_size[1] - self.rect.height


    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.v += Vector(-2,0)
        self.direction = "L"
        pass
    def go_down(self):
        """ Called when the user hits the left arrow. """
        self.v = Vector(0,1)
        pass
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.v += Vector(2,0)
        self.direction = "R"
        pass

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.v = Vector(0,0)
        pass
    def jump(self, screen_size):
        self.rect.y += 8
        platform_hit_list = pygame.sprite.spritecollide(self, self.world.platform_list, False)
        self.rect.y -= 8

        if len(platform_hit_list) > 0 or self.rect.bottom >= screen_size[1]:
            self.v.y = -10
        pass




if __name__ == "__main__":
    size = (640,480)
    screen = pygame.display.set_mode(size)
    p = Player()