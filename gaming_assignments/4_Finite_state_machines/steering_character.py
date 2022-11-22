
import pygame
from moving_ball_2d import MovingBall
from vector import Vector
import math
import random


class BeakBall (MovingBall):

    beak_tip = Vector(0,20)
    max_acceleration = 200.0
    width = 1024
    height = 768
    speedlimit = Vector(500,500)

    steering = []
    transitioned = False
    angle = 0
    radius =2

    def draw (self, window):
        pygame.draw.circle(window, self.color, (int(self.p.x),int(self.p.y)),self.r)
        speed = self.v.length()
        if speed != 0:
            self.beak_tip = self.v.normalize() * 20
        pygame.draw.line(window,self.color,(int(self.p.x),int(self.p.y)),(self.p.x+self.beak_tip.x,self.p.y+self.beak_tip.y), 3)

        for vec in self.steering:
            arrowvec = Vector(0,0)
            arrowvec = arrowvec + vec
            arrowvec = arrowvec + self.p
            pygame.draw.line(window,pygame.color.Color("black"),(int(self.p.x),int(self.p.y)),(arrowvec.x,arrowvec.y),2)


    def __str__ (self):
        return str(self.p)+", "+str(self.v)+", "+str(self.a) 


    def apply_steering (self):
        for s in self.steering:
            self.v = self.v + s


    def wander(self,weight):
        '''
        pick a random target some radius away from me
        and seek it
        '''
        if self.transitioned == True:
            self.change_color()
            self.transitioned = False
        random_target = Vector(0,0)
        random_target.x = random.randint(-1024,1024)
        random_target.y = random.randint(-768,768)
        max_speed = self.speedlimit.length()
        desired_velocity = random_target * max_speed
        for i in range(0,2):
            self.steering +=[(desired_velocity - self.v) * weight]


    def loop(self,weight):
        '''
        agent should move in a corkscrew manner
        James Helped me with this algorithm
        '''
        if self.transitioned == True:
            self.change_color()
            self.transitioned = False
        self.radiu = self.radius +0.001
        x = int(math.cos(self.angle)*3) + self.p.x
        y = int(math.sin(self.angle)*3) + self.p.y
        self.p.x = x
        self.p.y = y
        self.angle += 0.05
        self.wander(weight)


    def freeze(self):
        '''
        stop, hammertime
        '''
        self.v = Vector(0,0)
    def change_color(self):
        '''
        change color to a random color
        '''
        self.color = pygame.color.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))


