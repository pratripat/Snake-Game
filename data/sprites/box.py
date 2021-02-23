from data.scripts.globals import *

class Box:
    def __init__(self, pos, color=green, vel=[1,0]):
        self.pos = (pos[0]%squares, pos[1]%squares)
        self.vel = vel
        self.color = color

    def show(self, eyes=False):
        pygame.draw.rect(screen, self.color, (self.pos[0]*res, self.pos[1]*res, res, res))

        #Drawing the eyes of the snake
        if eyes:
            pygame.draw.circle(screen, black, (self.pos[0]*res+res//4, self.pos[1]*res+res//2), res//10)
            pygame.draw.circle(screen, black, (self.pos[0]*res+res//4*3, self.pos[1]*res+res//2), res//10)

    def move(self, vel):
        #Moving the box
        self.vel = vel

        #Putting the modulo operator, inorder to keep the box within the screen or the world
        self.pos = ((self.pos[0] + self.vel[0]) % squares, (self.pos[1] + self.vel[1]) % squares)
