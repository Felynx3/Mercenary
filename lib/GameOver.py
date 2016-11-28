import os
import pygame
from datos import*


class GameOver:

    def __init__(self):
        self.marco = pygame.Surface((WIDTH * 0.8 + 30, HEIGHT * 0.3 + 30))
        self.marco.fill((40, 0, 80))
        self.fondo = pygame.Surface((WIDTH * 0.8, HEIGHT * 0.3))
        self.fondo.fill((90, 40, 120))
        self.font = pygame.font.Font(os.path.join(".", "media", "fuentes", "8-BIT WONDER.TTF"), 60)
        self.reiniciar = self.font.render("REINICIAR (R)", True, (0, 0, 0))
        self.taberna = self.font.render("TABERNA (T)", True, (0, 0, 0))

        self.reiniciarRect = self.reiniciar.get_rect()
        self.reiniciarRect.centerx = WIDTH / 2
        self.reiniciarRect.bottom = HEIGHT / 2 - 5
        self.tabernaRect = self.taberna.get_rect()
        self.tabernaRect.centerx = WIDTH / 2
        self.tabernaRect.top = HEIGHT / 2 + 5
        self.fondoRect = self.fondo.get_rect()
        self.fondoRect.center = (WIDTH / 2, HEIGHT / 2)
        self.marcoRect = self.marco.get_rect()
        self.marcoRect.center = (WIDTH / 2, HEIGHT / 2)

    def draw(self, screen):
        screen.blit(self.marco, self.marcoRect)
        screen.blit(self.fondo, self.fondoRect)
        screen.blit(self.reiniciar, self.reiniciarRect)
        screen.blit(self.taberna, self.tabernaRect)