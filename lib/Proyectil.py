import pygame
import os
from datos import*


class Proyectil(pygame.sprite.Sprite):

    def __init__(self, nombre, direccion, enemigo, escala, (x, y)):
        pygame.sprite.Sprite.__init__(self)
        self.muerto = False
        self.nombre = nombre
        self.enemigo = enemigo
        self.direccion = direccion
        self.imagePath = os.path.join(".", "media", "imagenes", "proyectiles", nombre, "")
        self.image = pygame.image.load(self.imagePath + "normal1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x, self.y = x, y
        self.collisionRect = pygame.rect.Rect(self.rect.left, self.rect.top, TAMANO_PROYECTIL[nombre]["colision"][0] * escala, TAMANO_PROYECTIL[nombre]["colision"][1] * escala)
        self.dano = DANO_PROYECTIL[nombre]
        self.velocidad = VELOCIDAD_PROYECTIL[nombre]
        if self.direccion == "left":
            self.velocidad *= -1
        self.animacionDelay = ANIMACION_DELAY_PROYECTIL[nombre]
        self.tiempoParaAnimar = self.animacionDelay
        self.imageIndex = -1

        self.imagenes = []
        self.imagenesMuerte = []
        self.cargarImagenes(escala)
        self.alinearRects()

    def update(self):
        self.tiempoParaAnimar -= 1000 / 60
        if self.tiempoParaAnimar <= 0:
            self.animar()
            self.tiempoParaAnimar = self.animacionDelay
        self.x += self.velocidad
        #self.rect.centerx += self.velocidad
        self.alinearRects()
        if self.rect.left >= WIDTH or self.rect.right <= 0:
            pygame.sprite.Sprite.kill(self)

    def alinearRects(self):
        self.rect.center = (self.x, self.y)
        self.collisionRect.centery = self.rect.y
        if self.direccion == "left":
            self.collisionRect.left = self.rect.left
        else:
            self.collisionRect.right = self.rect.right

    def animar(self):
        self.imageIndex += 1
        if self.imageIndex >= len(self.imagenes) and not self.muerto:
            self.imageIndex = 0
        elif self.imageIndex >= len(self.imagenesMuerte) and self.muerto:
            pygame.sprite.Sprite.kill(self)
            return
        if self.muerto:
            self.image = self.imagenesMuerte[self.imageIndex]
            muerteRect = self.image.get_rect()
            muerteRect.center = self.rect.center
            if self.direccion == "left":
                muerteRect.left = self.rect.left
            else:
                muerteRect.right = self.rect.right
            self.rect = muerteRect
            return
        if self.direccion == "left":
            self.image = self.imagenes[self.imageIndex][0]
        else:
            self.image = self.imagenes[self.imageIndex][1]

    def cargarImagenes(self, escala):
        for i in range(FRAMES_PROYECTIL[self.nombre]["normal"]):
            imagenD = pygame.image.load(self.imagePath + "normal" + str(i + 1) + ".png")
            imagenD = pygame.transform.scale(imagenD, (imagenD.get_rect().w * escala, imagenD.get_rect().h * escala))
            imagenI = pygame.transform.flip(imagenD, True, False)
            self.imagenes.append([imagenI, imagenD])

        for i in range(FRAMES_PROYECTIL[self.nombre]["muerte"]):
            imagen = pygame.image.load(self.imagePath + "muerte" + str(i + 1) + ".png")
            imagen = pygame.transform.scale(imagen, (imagen.get_rect().w * escala, imagen.get_rect().h * escala))
            self.imagenesMuerte.append(imagen)

        self.image = self.imagenes[0][1]
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def kill(self):
        self.muerto = True
        self.imageIndex = 0
        self.velocidad = 0