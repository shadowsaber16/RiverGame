import pygame
pygame.init()


class Global(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 950))
        self.icon = pygame.image.load("boat.png")
        self.player1Img = pygame.image.load("player1.png")
        self.player2Img = pygame.image.load("player2.png")
        self.ship1Img = pygame.image.load("sea-ship.png")
        self.ship2Img = pygame.image.load("sea-ship.png")
        self.ship3Img = pygame.image.load("sea-shipright.png")
        self.rock1Img = pygame.image.load("rocks.png")
        self.startimg = pygame.image.load("start.png")
        self.finishimg = pygame.image.load("finish.png")
        self.font = pygame.font.Font('freesansbold.ttf', 64)
        self.font1 = pygame.font.Font('freesansbold.ttf', 128)
        self.running = True
