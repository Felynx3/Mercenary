import pygame
from Sprite import Sprite
from IA import IA
from Proyectil import Proyectil
from datos import*
import random


class GargolaT(Sprite):

    def __init__(self):
        self.imagenesQuieto = []
        self.imagenesCargando = []
        Sprite.__init__(self, "Gargola Terrestre", "gargolaT", True)
        self.collisionRect.center = (WIDTH / 2, HEIGHT / 2)
        self.alturaProyectil = ALTURAS_GOLPES["gargolaT"][0]

    def animar(self):
        direcciones = {"left": 0, "right": 1}
        direccion = direcciones[self.direccion]
        self.imagenIndex += 1
        if self.ia.estado == "quieto":
            if self.imagenIndex >= len(self.imagenesQuieto):
                self.imagenIndex = 0
            self.image = self.imagenesQuieto[self.imagenIndex][direccion]
            return
        if self.ia.estado == "cargando":
            if self.imagenIndex >= 3:
                self.imagenIndex = 1
            self.image = self.imagenesCargando[self.imagenIndex][direccion]
            return
        if self.ia.estado == "disparando":
            if self.imagenIndex >= 4:
                self.disparar()
                self.imagenIndex = 0
                self.ia.reiniciar()
            self.image = self.imagenesCargando[self.imagenIndex][direccion]

    def cargarImagenes(self):
        for i in range(1, FRAMES_ANIMACION[self.clase]["quieto"] + 1):
            imagen = pygame.image.load(self.imagePath + "quieto" + str(i) + ".png")
            imagenD = pygame.transform.scale(imagen, (int(imagen.get_rect().w * self.escala), int(imagen.get_rect().h * self.escala)))
            imagenI = pygame.transform.flip(imagenD, True, False)
            self.imagenesQuieto.append([imagenI, imagenD])
        for i in range(1, FRAMES_ANIMACION[self.clase]["cargando"] + 1):
            imagen = pygame.image.load(self.imagePath + "cargando" + str(i) + ".png")
            imagenD = pygame.transform.scale(imagen, (int(imagen.get_rect().w * self.escala), int(imagen.get_rect().h * self.escala)))
            imagenI = pygame.transform.flip(imagenD, True, False)
            self.imagenesCargando.append([imagenI, imagenD])

    def disparar(self):
        if self.direccion == "left":
            posX = self.collisionRect.left
        else:
            posX = self.collisionRect.right
        posY = self.collisionRect.bottom - self.alturaProyectil - TAMANO_PROYECTIL["vackura"]["normal"][1] * self.escala / 2
        proyectil = Proyectil("vackura", self.direccion, True, self.escala, (posX, posY))
        evento = pygame.event.Event(PROYECTIL, proyectil=proyectil)
        pygame.event.post(evento)


class GargolaTIA(IA):

    def __init__(self, sprite, objetivo):
        IA.__init__(self, sprite, objetivo)
        self.estado = "quieto"
        self.distanciaDisparo = WIDTH
        self.delayDisparo = DELAY_DISPARO["gargolaT"]
        self.tiempoDisparo = self.delayDisparo
        self.delayCarga = TIEMPO_CARGA["gargolaT"]
        self.tiempoCarga = self.delayCarga

    def update(self):
        self.distanciaObjetivo = self.objetivo.collisionRect.centerx - self.sprite.collisionRect.centerx
        if self.distanciaObjetivo > 0:
            self.sprite.direccion = "right"
        else:
            self.sprite.direccion = "left"
        self.tiempoDisparo -= 1000 / 60
        if self.estado == "cargando":
            self.tiempoCarga -= 1000 / 60
        if self.tiempoCarga <= 0:
            self.disparar()
        self.actuar()

    def disparar(self):
        self.estado = "disparando"
        self.tiempoCarga = self.delayCarga
        self.tiempoDisparo = self.delayDisparo

    def actuar(self):
        num = random.randint(1, 50)
        if num == 5 and self.tiempoDisparo <= 0 and abs(self.distanciaObjetivo) < self.distanciaDisparo:
            self.estado = "cargando"
            self.sprite.imagenIndex = 0

    def reiniciar(self):
        self.estado = "quieto"
        self.tiempoDisparo = self.delayDisparo