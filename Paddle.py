import pygame

class Paddle:
    WHITE = (255,255,255)
    VEL = 6

    def __init__(self, x, y, width, height, velocity = VEL, color = WHITE):
        self.x = self.original_x =  x
        self.y = self.original_y =  y
        self.width = width
        self.height = height
        self.color = color
        self.velocity = velocity
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
    
    def move(self, upDir = True):
        if upDir:
            self.y -= self.velocity
        else:
            self.y += self.velocity

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
