import os
import pygame
from datos import*
from SpriteEstatico import SpriteEstatico


class MenuPrincipal:

    def __init__(self, jugador):
        self.font = pygame.font.Font(os.path.join(".", "media", "fuentes", "8-BIT WONDER.TTF"), 40)
        self.opciones = []
        self.cargarOpciones()

    def update(self):
        for opcion in self.opciones:
            opcion.update()

    def getOpcion(self, personaje):
        for opcion in self.opciones:
            if personaje.collisionRect.colliderect(opcion.rect):
                return opcion.opcion
        return(None)

    def draw(self, screen):
        for opcion in self.opciones:
            screen.blit(opcion.image, opcion.rect)

    def cargarOpciones(self):
        jugar = SpriteEstatico("jugar")
        self.opciones.append(jugar)