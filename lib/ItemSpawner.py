import pygame
import os
from random import randint
from datos import*


class ItemSpawner:

    def __init__(self, items, dificultad):
        self.dificultad = dificultad
        self.items = items
        self.imagePath = os.path.join(".", "media", "imagenes", "objetos", "consumibles", "")
        self.delay = dificultad * 2500
        self.tipos = ["vida"]

    def update(self, personaje):
        self.delay -= randint(0, 3)
        if self.delay <= 0:
            self.spawn()
        if personaje is not None:
            for item in self.items:
                item.colisionar(personaje)

    def spawn(self):
        if len(self.items) < 2:
            self.delay = self.dificultad * 1000
            tipo = self.tipos[randint(0, len(self.tipos) - 1)]
            pota = Item(tipo, self.imagePath)
            self.items.add(pota)

    def reiniciar(self):
        self.delay = self.dificultad * 1000
        self.items.empty()


class Item(pygame.sprite.Sprite):

    def __init__(self, tipo, imagePath):
        pygame.sprite.Sprite.__init__(self)
        self.tipo = tipo  # vida dano etc.
        self.image = pygame.image.load(imagePath + tipo + ".png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.rect.w * HEIGHT / 200, self.rect.h * HEIGHT / 200))
        self.rect = self.image.get_rect()
        if tipo == "vida":
            self.cantidad = randint(1, 3)
        elif tipo == "armadura":
            self.cantidad = 1
        self.vy = 4
        self.rect.center = (randint(50, WIDTH - 50), HEIGHT / 2)

    def colisionar(self, personaje):
        if self.rect.colliderect(personaje.collisionRect):
            if self.tipo == "vida":
                personaje.curar(self.cantidad)
                self.kill()

    def update(self):
        self.rect.centery += self.vy
        if self.rect.bottom > HEIGHT - ALTURA_BASE:
            self.vy = 0
            self.rect.bottom = HEIGHT - ALTURA_BASE

    def draw(self, screen):
        screen.blit(self.image, self.rect)