from data.scripts.globals import *
from data.sprites.box import Box

class Snake:
    def __init__(self, pos):
        #Body starts with two pieces
        self.body = [Box(pos), Box((pos[0]-1, pos[1]))]
        self.vel = [1,0]
        self.turns = {}
        self.move_cooldown = self.initial_move_cooldown = fps//6

    def show(self):
        for i, b in enumerate(self.body):
            #Rendering the eyes
            if i == 0:
                b.show(True)
            else:
                b.show()

    def move(self):
        #Updating the velocity according to the key presses
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.vel[1] != 1:
            self.vel = [0, -1]
            self.turns[self.body[0].pos[:]] = self.vel
        if keys[pygame.K_s] and self.vel[1] != -1:
            self.vel = [0,  1]
            self.turns[self.body[0].pos[:]] = self.vel
        if keys[pygame.K_a] and self.vel[0] != 1:
            self.vel = [-1, 0]
            self.turns[self.body[0].pos[:]] = self.vel
        if keys[pygame.K_d] and self.vel[0] != -1:
            self.vel = [ 1, 0]
            self.turns[self.body[0].pos[:]] = self.vel

        #Moving the snake periodically
        if self.move_cooldown == 0:
            for i, b in enumerate(self.body):
                p = b.pos[:]

                #Turning the piece of body at particular location
                if p in self.turns:
                    vel = self.turns[p]
                    b.move(vel)
                    if i == len(self.body)-1:
                        self.turns.pop(p)
                #Or else moving it with the initial velocity of the box or piece
                else:
                    b.move(b.vel)

            self.move_cooldown = self.initial_move_cooldown

        #Updating the move cooldown
        self.move_cooldown -= 1

    def eats(self, pos):
        #Checking if the head is on the particulat position
        return self.body[0].pos == pos

    def grow(self):
        #Adding a piece of according to the snake's tail's velocity
        tail = self.body[-1]
        vel = tail.vel

        if vel[1] == 1:
            self.body.append(Box((tail.pos[0], tail.pos[1]-1), vel=vel))
        elif vel[1] == -1:
            self.body.append(Box((tail.pos[0], tail.pos[1]+1), vel=vel))
        if vel[0] == 1:
            self.body.append(Box((tail.pos[0]-1, tail.pos[1]), vel=vel))
        elif vel[0] == -1:
            self.body.append(Box((tail.pos[0]+1, tail.pos[1]), vel=vel))

    def bites_itself(self):
        #Checking if the head of the snake is within the body
        return self.body[0].pos in [b.pos for b in self.body[1:]]

    def reset(self, pos):
        #Resetting the parameters of the snake
        self.body = [Box(pos), Box((pos[0]-1, pos[1]))]
        self.vel = [1,0]
        self.turns = {}
        self.move_cooldown = self.initial_move_cooldown
