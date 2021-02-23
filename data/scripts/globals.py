import pygame

#Pygame initialization
pygame.init()

#Window dimensions
width = height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake game')

squares = 30
res = width//squares

clock = pygame.time.Clock()
fps = 100

#Colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
orange = (255,128,0)
green = (0,255,0)
