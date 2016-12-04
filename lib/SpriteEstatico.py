import pygame
import os
from datos import*


class SpriteEstatico(pygame.sprite.Sprite):

    def __init__(self, opcion):
        pygame.sprite.Sprite.__init__(self)
        self.opcion = opcion
        self.image = None
        self.imagenes = []
        self.cargarImagenes()
        self.rect = self.image.get_rect()
        self.rect.center = self.ajustarPosicion()

        self.index = 0
        self.sentido = 1
        self.animacionDelay = 900
        self.tiempoAnimacion = self.animacionDelay

    def update(self):
        self.tiempoAnimacion -= 60
        if self.tiempoAnimacion <= 0:
            self.tiempoAnimacion = self.animacionDelay
            self.animar()

    def animar(self):
        if ANIMACION_PING_PONG[self.opcion]:
            self.index += 1 * self.sentido
            if self.index >= FRAMES_OPCION[self.opcion]:
                self.index -= 2
                self.sentido *= -1
            if self.index < 0:
                self.index += 2
                self.sentido *= -1
            self.image = self.imagenes[self.index]

    def ajustarPosicion(self):
        return (POSX_OPCION[self.opcion], HEIGHT - ALTURA_BASE - int(self.rect.h / 2))

    def cargarImagenes(self):
        imagePath = os.path.join(".", "media", "imagenes", "menu", "")
        for i in range(1, FRAMES_OPCION[self.opcion] + 1):
            imagen = pygame.image.load(imagePath + self.opcion + str(i) + ".png")
            if self.opcion == "jugar":
                imagen = pygame.transform.scale(imagen, (int(imagen.get_rect().w * 2.2), int(imagen.get_rect().h * 2.2)))
            else:
                imagen = pygame.transform.scale(imagen, (int(imagen.get_rect().w * 1.5), int(imagen.get_rect().h * 1.7)))

            self.imagenes.append(imagen)
        self.image = self.imagenes[0]