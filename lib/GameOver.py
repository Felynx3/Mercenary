import os
import pygame
from datos import*


class GameOver:

    def __init__(self):
        self.font = pygame.font.Font(os.path.join(".", "media", "fuentes", "8-BIT WONDER.TTF"), 60)
        self.reiniciar = self.font.render("REINICIAR (R)", True, (0, 0, 0))
        self.taberna = self.font.render("TABERNA (T)", True, (0, 0, 0))

        self.reiniciarRect = self.reiniciar.get_rect()
        self.reiniciarRect.center = (WIDTH / 2, HEIGHT / 2)
        self.tabernaRect = self.taberna.get_rect()
        self.tabernaRect.center = (WIDTH / 2, HEIGHT / 2 + self.tabernaRect.h * 1.4)

    def draw(self, screen):
        screen.blit(self.reiniciar, self.reiniciarRect)
        screen.blit(self.taberna, self.tabernaRect)