from data.scripts.globals import *
from data.scripts.button import Button
from data.scripts.game import Game

class Menu:
    def __init__(self):
        #Setting up play button
        self.game_button = Button({'x':width//2, 'y':height//2+100, 'w':130, 'h':50}, {'color':white, 'hover_color':green, 'font_color':black, 'alpha':128}, {'text':'Play', 'font':'comicsans', 'font_size':30})
        self.game = Game()
        self.image = pygame.image.load('data/image/title.png')
        self.font = pygame.font.SysFont('comcisans', 25)

    def run(self):
        screen.fill(black)

        #Rendering the current highscore
        high_score = 'Highscore: ' + open('data/scores/scores.txt', 'r').read().split('\n')[0]
        label = self.font.render(high_score, 1, orange)

        screen.blit(self.image, (width//2-self.image.get_width()//2, 120+self.image.get_height()//2))
        screen.blit(label, (width//2-label.get_width()//2, 150+self.image.get_height()*1.5))

        #Updating the play button
        self.game_button.update()
        self.game_button.show()

        pygame.display.update()

    def event_loop(self):
        for event in pygame.event.get():
            #Closing the window if the close button is clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Running the game if the play button is clicked
                self.game_button.on_click(self.game.main_loop)

    def main_loop(self):
        while True:
            self.event_loop()
            self.run()
