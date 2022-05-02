import pygame

class Ball:
    WHITE = (255,255,255)
    DEFAULT_MAX_X_VELOCITY = 6

    def __init__(self, x, y, radius, color = WHITE, max_velocity = DEFAULT_MAX_X_VELOCITY):

        ##x and y values are the center points of the ball
        self.x = self.original_x = x
        self.y = self.original_y = y

        self.radius = radius
        self.color = color

        self.max_velocity = max_velocity
        self.x_velocity = -max_velocity
        self.y_velocity = 0

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
    
    def move(self):
        self.x +=  self.x_velocity
        self.y +=  self.y_velocity
    
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

        self.x_velocity = self.max_velocity
        self.y_velocity = 0
