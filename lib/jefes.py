import pygame
from Sprite import Sprite
from IA import IA
from Proyectil import Proyectil
from datos import*
import random


class GargolaT(Sprite):

    def __init__(self, objetivo):
        self.imagenesQuieto = []
        self.imagenesCargando = []
        Sprite.__init__(self, "Gargola Terrestre", "gargolaT", True)
        self.ia = GargolaTIA(self, objetivo)
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

    def transportar(self, direccion):
        transporte = ProyectilTransporte(direccion, self.collisionRect.right, self.collisionRect.centery - 10, 2, self)
        evento = pygame.event.Event(PROYECTIL, proyectil=transporte)
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
        self.tiempoTransporte = 700
        self.delayTransporte = 1000

    def update(self):
        self.distanciaObjetivo = self.objetivo.collisionRect.centerx - self.sprite.collisionRect.centerx
        if self.distanciaObjetivo > 0:
            self.sprite.direccion = "right"
        else:
            self.sprite.direccion = "left"
        self.tiempoDisparo -= 1000 / 60
        self.tiempoTransporte -= 1000 / 60
        if self.tiempoTransporte < 0:
            self.tiempoTransporte = -1
        if self.estado == "cargando":
            self.tiempoCarga -= 1000 / 60
        if self.tiempoCarga <= 0:
            self.disparar()
        if abs(self.distanciaObjetivo) < 150 and self.tiempoTransporte <= 0:
            self.transportar()
            print(pygame.time.Clock().get_time())
        self.actuar()

    def transportar(self):
        self.tiempoTransporte = self.delayTransporte
        if self.sprite.x < self.objetivo.x:  # transporte a la derecha
            self.sprite.transportar("right")
        else:
            self.sprite.transportar("left")

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


class ProyectilTransporte(pygame.sprite.Sprite):

    def __init__(self, direccion, x, y, escala, carga):  # carga -> sprite a transportar
        pygame.sprite.Sprite.__init__(self)
        self.carga = carga
        self.image = None
        self.rect = None
        self.x, self.y = x, y
        self.imagenes = []
        self.index = 0
        if direccion == "left":
            self.sentido = -1
        else:
            self.sentido = 1
        self.delayAnimacion = 400
        self.tiempoAnimacion = self.delayAnimacion
        self.cargarImagenes(escala, direccion)

    def update(self):
        self.tiempoAnimacion -= 1000 / 60
        if self.tiempoAnimacion <= 0:
            self.tiempoAnimacion = self.delayAnimacion
            self.animar()
        self.x += 5 * self.sentido
        self.rect.centerx = self.x
        if (self.sentido == -1 and self.x < 150) or (self.sentido == 1 and self.x > WIDTH - 150):
            self.transportar()

    def transportar(self):
        self.carga.posicionar(self.x, self.carga.y)
        self.kill()

    def animar(self):
        self.index += 1
        if self.index > 2:
            return
        self.image = self.imagenes[self.index]

    def cargarImagenes(self, escala, direccion):
        for i in range(1, 4):
            imagen = pygame.image.load("./media/imagenes/proyectiles/transporte/transporte" + str(i) + ".png")
            imagen = pygame.transform.scale(imagen, (imagen.get_rect().w * escala, imagen.get_rect().h * escala))
            if direccion == "left":
                imagen = pygame.transform.flip(imagen, True, False)
            self.imagenes.append(imagen)
        self.image = self.imagenes[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)