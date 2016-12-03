import pygame
import os
from constantes import*


class Muerto(pygame.sprite.Sprite):

    def __init__(self, (x, y)):
        pygame.sprite.Sprite.__init__(self)
        self.escala = 2
        self.imagePath = os.path.join(".", "media", "imagenes", "muerto", "muerte")
        self.image = None
        self.rect = None
        self.x, self.y = x, y
        self.collisionRect = (0, 0, -1, -1)
        self.imageIndex = 0
        self.imagenes = []
        self.cargarImagenes()
        self.delayAnimacion = 1000 / 10
        self.tiempoAnimacion = self.delayAnimacion
        self.reproducirSonido()

    def reproducirSonido(self):
        evento = pygame.event.Event(SONIDO, sonido="muerte")
        pygame.event.post(evento)

    def cargarImagenes(self):
        for i in range(1, 6):
            imagen = pygame.image.load(self.imagePath + str(i) + ".png")
            imagen = pygame.transform.scale2x(imagen)
            self.imagenes.append(imagen)
        self.image = self.imagenes[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        self.tiempoAnimacion -= 1000 / 60
        if self.tiempoAnimacion <= 0:
            self.tiempoAnimacion = self.delayAnimacion
            self.animar()

    def animar(self):
        self.imageIndex += 1
        if self.imageIndex > 4:
            self.kill()
            return
        self.image = self.imagenes[self.imageIndex]

    def draw(self, screen):
        screen.blit(self.imagen, self.rect)