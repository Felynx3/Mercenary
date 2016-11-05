import random
import pygame
from datos import*


class IA:

    def __init__(self, sprite, objetivo):  # int 1 -> facil
        self.objetivo = objetivo
        self.distanciaObjetivo = 0
        self.sprite = sprite
        self.estado = "patrullando"
        self.areaVision = pygame.rect.Rect(0, 0, 2 * WIDTH / 3, HEIGHT / 2)
        if TIPO_ATAQUE[sprite.clase] == "mele":
            self.distanciaAtaque = TAMANOS_SPRITES[sprite.clase]["ataque"][0] * 2  # ancho del ataque por 2
        else:
            self.distanciaAtaque = WIDTH

    def update(self):
        self.revisarEstado()
        self.actualizarParametros()

    def revisarEstado(self):
        self.areaVision.centerx = self.sprite.collisionRect.centerx
        self.areaVision.bottom = HEIGHT
        self.distanciaObjetivo = self.objetivo.collisionRect.centerx - self.sprite.collisionRect.centerx
        if self.areaVision.colliderect(self.objetivo.collisionRect):
            self.estado = "acercandose"
            if abs(self.distanciaObjetivo) <= self.distanciaAtaque:
                self.estado = "atacando"
        else:
            self.estado = "patrullando"

    def actualizarParametros(self):
        if self.estado == "patrullando":
            direcciones = ["left", "right"]
            randNum = random.randint(0, 50)
            if randNum == 0 or randNum == 1:  # Girar
                self.sprite.correr(direcciones[randNum])
        if self.estado == "acercandose" or self.estado == "atacando":
            if self.distanciaObjetivo < 0:  # objetivo a la izquierda
                self.sprite.correr("left")
            else:
                self.sprite.correr("right")
        if self.estado == "atacando":
            self.sprite.atacar()