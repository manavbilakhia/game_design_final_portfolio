
# Author: Manav Bilakhia

import pygame
from moving_ball_2d import MovingBall
from vector import Vector


class SteeringBall (MovingBall):

    beak_tip = Vector(0,20)

    speedlimit = Vector(500,500)

    # All steering inputs
    steering = []

    def draw (self, window):
        # draw the body
        pygame.draw.circle(window, self.color, (int(self.p.x),int(self.p.y)),self.r)
        # draw the beak
        speed = self.v.length()
        if speed != 0:
            self.beak_tip = self.v.normalize() * 20
        pygame.draw.line(window,self.color,(int(self.p.x),int(self.p.y)),(self.p.x+self.beak_tip.x,self.p.y+self.beak_tip.y), 3)

        if self.drawvec:
            for vec in self.steering:
                arrowvec = Vector(0,0)
                arrowvec = arrowvec + vec
                arrowvec = arrowvec + self.p
                pygame.draw.line(window,pygame.color.Color("red"),(int(self.p.x),int(self.p.y)),(arrowvec.x,arrowvec.y),2)


    def __str__ (self):
        return str(self.p)+", "+str(self.v)+", "+str(self.a) 


    def apply_steering (self):
        ## add all steering inputs to current velocity vector
        for s in self.steering:
            self.v += s


    def seek (self, target, weight):
        #find difference between my location and target location
        desired_direction = (target.p - self.p).normalize()
        #multiply direction by max speed
        max_speed = self.speedlimit.length()
        desired_velocity = desired_direction * max_speed
        ## first find the "error" between current velocity and desired velocity, and then multiply that error
        ## by the weight, and then add it to steering inputs
        self.steering += [(desired_velocity - self.v)*weight]

    def arrive(self,target, weight,speed_multiplier = 1.05):
       if (self.p-target.p).length() < 4*(self.r+target.r):
           self.seek(target, weight)
       else:
        desired_direction = (target.p - self.p).normalize()
        max_speed = self.speedlimit.length()*speed_multiplier
        threshhold_distance = 4*(self.r+target.r)
        desired_velocity = desired_direction * max_speed * ((self.p-target.p).length()/threshhold_distance)
        self.steering += [(desired_velocity - self.v)*weight]

    def flee(self, target, weight):
        if (self.p - target.p).length() < 2* (self.r + target.r):
            desired_direction = (self.p - target.p).normalize()
            max_speed = self.speedlimit.length()
            desired_velocity = desired_direction * max_speed
            self.steering += [(desired_velocity - self.v) * weight]
        else:
            self.seek(target, weight)

    def cohesion(self, centroid, weight):
        self.seek(centroid, weight)


    def separation(self, char_list, weight):
        velocity_adjustment = Vector(0,0)
        threshhold_distance = 8 * (self.r)
        for boid in char_list:
            if boid != self:
                current_distance = (self.p - boid.p).length()
                if (self.p - boid.p).length() < threshhold_distance:
                    target_direction = (boid.p - self.p).normalize()
                    velocity_adjustment += target_direction* current_distance
        desired_velocity = (self.v-velocity_adjustment)
        self.steering += [desired_velocity* weight]

    def align(self, char_list, weight):

        average_velocity = Vector(0,0)
        for boid in char_list:
            if boid != self:
                average_velocity += boid.v
        average_velocity = average_velocity / (len(char_list)-1)
        velocity_difference = average_velocity - self.v
        self.steering += [(velocity_difference)*weight]





