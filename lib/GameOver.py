import os
import pygame
from datos import*


class GameOver:

    def __init__(self):
        self.font = pygame.font.Font(os.path.join(".", "media", "fuentes", "8-BIT WONDER.TTF"), 60)
        self.mensaje = self.font.render("REINICIAR (R)", True, (0, 0, 0))
        self.mensajeRect = self.mensaje.get_rect()
        self.mensajeRect.center = (WIDTH / 2, HEIGHT / 2)

    def draw(self, screen):
        screen.blit(self.mensaje, self.mensajeRect)