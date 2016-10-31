import os
import pygame
from datos import*


class MenuPrincipal:

    def __init__(self, jugador):
        self.font = pygame.font.Font(os.path.join(".", "media", "fuentes", "8-BIT WONDER.TTF"), 40)

        self.jugar = pygame.sprite.Sprite()
        self.jugar.image = pygame.image.load(os.path.join(".", "media", "imagenes", "clases", "goblin", "walk4.png"))
        self.jugar.image = pygame.transform.scale(self.jugar.image, (self.jugar.image.get_rect().w * 4, self.jugar.image.get_rect().h * 4))
        self.jugarRect = self.jugar.image.get_rect()
        self.jugarRect.left, self.jugarRect.bottom = 120, HEIGHT - ALTURA_BASE

    def update(self):
        pass

    def getOpcion(self, personaje):
        if personaje.collisionRect.colliderect(self.jugarRect):
            return "jugar"
        return(None)

    def draw(self, screen):
        screen.blit(self.jugar.image, self.jugarRect)