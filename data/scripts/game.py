from data.scripts.globals import *
from data.sprites.box import Box
from data.sprites.snake import Snake
import random

class Game:
    def __init__(self):
        #Starting position of the snake
        self.start = (2,2)
        self.snake = Snake(self.start)
        self.apple = Box(self.random_pos(), red)
        self.font = pygame.font.SysFont('comicsans', 60)

    def random_pos(self):
        pos = None

        #Generating random positions until the position is not in the snake
        while pos == None:
            random_pos = (random.randrange(squares), random.randrange(squares))

            #Setting the apple's position if the random position is not in the snake's body
            if random_pos not in [b.pos[:] for b in self.snake.body]:
                pos = random_pos

        return pos

    def run(self):
        clock.tick(fps)

        screen.fill(black)

        self.apple.show()
        self.snake.show()
        self.snake.move()

        #If the snake eats the apple, it grows in size
        if self.snake.eats(self.apple.pos[:]):
            self.snake.grow()

            #Setting new position for the apple
            self.apple.pos = self.random_pos()

        #If snake bites itself, resetting the game
        if self.snake.bites_itself():
            #Rendering text 'YOU LOST'
            label = self.font.render('YOU LOST', 1, red)
            screen.blit(label, (width//2 - label.get_width()//2, height//2 - label.get_height()//2))
            pygame.display.update()

            #Saving the new highscore if there is any
            self.save_scores()

            self.snake.reset(self.start)

            self.game_over = True

            #1 second delay
            pygame.time.wait(1000)

        pygame.display.update()

    def event_loop(self):
        for event in pygame.event.get():
            #Closing the window if the window close button is clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def main_loop(self):
        #Resetting the game over to False eveytime this function is run
        self.game_over = False

        while not self.game_over:
            self.event_loop()
            self.run()

    def save_scores(self):
        score = len(self.snake.body)
        highscore = int(open('data/scores/scores.txt', 'r').read().split('\n')[0])

        #Setting the current score as new highscore, if the current score is greater than the highscore
        if score > highscore:
            highscore_file = open('data/scores/scores.txt', 'w')
            highscore_file.write(str(score)+'\n')
            highscore_file.close()
