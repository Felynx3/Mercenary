import pygame
import os
from datos import*
from CajaSonidos import*
from IA import*


class Sprite(pygame.sprite.Sprite):

    def __init__(self, name, clase, esEnemigo):
        pygame.sprite.Sprite.__init__(self)
        self.esEnemigo = esEnemigo
        self.name = name
        self.clase = clase
        self.vida = VIDA[clase]
        self.danoAtaque = DANO_ATAQUE[clase][0]
        self.ia = None
        self.dificultad = 1.0

        self.imagePath = os.path.join(".", "media", "imagenes", "clases", clase, "")
        if self.clase == "goblin" and not esEnemigo:
            self.imagePath = os.path.join(".", "media", "imagenes", "clases", clase, "especial", "")
        self.image = pygame.image.load(self.imagePath + "normal.png")
        self.escala = 2.5
        self.rect = self.image.get_rect()  # Solo usado para pygame.sprite.Group.draw()
        self.collisionRect = pygame.rect.Rect((0, 0), TAMANOS_SPRITES[clase]["colision"])  # para colisiones con margen, enemigos y ataques.
        self.weaponRect = pygame.rect.Rect((0, 0), TAMANOS_ATAQUES[self.clase][0])
        self.width, self.height = self.image.get_rect().w, self.image.get_rect().h
        self.gravedad = HEIGHT / 120
        self.tiempoSalto = 0.0
        self.numeroSaltos = NUMERO_SALTOS[self.clase]
        self.saltos = 1
        self.entrando = False
        self.direccion = "right"
        self.velocidadMovimiento = VELOCIDAD_MOVIMIENTO[self.clase]
        self.vx, self.vy = 0.0, 0.0
        self.x, self.y = 0.0, 0.0
        self.cajaSonidos = CajaSonidos(clase)

        self.empuje = None
        self.muerto = False

        self.atacando = False
        self.golpesPorAtaque = GOLPES_POR_ATAQUE[self.clase]
        self.golpe = 0
        self.framesDano = FRAMES_DANO[self.clase]
        self.alturaGolpes = ALTURAS_GOLPES[self.clase]

        self.framesAnimacion = FRAMES_ANIMACION[self.clase]
        self.animacionDelay = ANIMACION_DELAY[self.clase]
        self.tiempoParaAnimar = self.animacionDelay
        self.imagenesCorriendo = []  # [Izquierda][Derecha]
        self.imagenesAtacando = []
        self.imagenesSaltando = []
        self.imagenNormal = [pygame.transform.flip(self.image, True, False), self.image]
        self.cargarImagenes()
        self.imagenIndex = 0

        self.escalar(2)

    def reiniciar(self):
        if not self.esEnemigo:
            self.vida = VIDA[self.clase]
            self.posicionar(WIDTH / 2, HEIGHT / 2)

    def enemigo(self, dificultad, objetivo):
        if self.esEnemigo:
            self.dificultad = dificultad
            self.ia = IA(self, objetivo)
            self.vida = int(self.vida * dificultad)

    def entrar(self, lado):
        self.entrando = True
        if lado == "left":
            self.vx = self.velocidadMovimiento / 3
            self.posicionar(-self.collisionRect.w, HEIGHT)
        else:
            self.vx = -self.velocidadMovimiento / 3
            self.posicionar(WIDTH + self.collisionRect.w, HEIGHT)

    def empujar(self, direccion):
        if self.empuje is None:
            self.saltos += 1
            self.tiempoSalto = 0.0
            self.vy = -4
            self.empuje = direccion

    def detenerEmpuje(self):
        self.empuje = None

    def saltar(self):
        if self.saltos < self.numeroSaltos:
            self.cajaSonidos.reproducir("salto")
            self.saltos += 1
            self.tiempoSalto = 0.0
            self.vy = -self.collisionRect.h / 5.5
            if not self.atacando:
                self.imagenIndex = 0

    def cancelarSalto(self):
        self.saltos = 0
        self.vy = 0.0
        if self.tiempoSalto > 0.1:
            self.cajaSonidos.reproducir("caida")
        self.tiempoSalto = 0.0

    def correr(self, direccion):
        if self.esEnemigo:
            self.vx = 0
        if direccion == "left":
            self.vx -= self.velocidadMovimiento
        if direccion == "right":
            self.vx += self.velocidadMovimiento
        if not self.atacando:
            self.direccion = direccion

    def detener(self, direccion):
        if direccion == "left":
            self.vx += self.velocidadMovimiento
            if not self.atacando:
                if self.vx > 0:
                    self.direccion = "right"
                elif self.vx == 0:
                    self.direccion = "left"
        if direccion == "right":
            self.vx -= self.velocidadMovimiento
            if not self.atacando:
                if self.vx < 0:
                    self.direccion = "left"
                elif self.vx == 0:
                    self.direccion = "right"

    def colisionar(self, rect):
        self.detenerEmpuje()
        self.mover(-self.vx, 0)
        # en caso de que sea enemigo
        # si esta a la derecha
        if self.collisionRect.centerx > rect.centerx and self.esEnemigo:
            self.mover(1, 0)
        # si esta a la izquierda
        elif self.collisionRect.centerx < rect.centerx and self.esEnemigo:
            self.mover(-1, 0)
        if self.collisionRect.bottom > rect.top and self.collisionRect.bottom < rect.top + self.vy + 1:
            self.cancelarSalto()
            self.setBottom(rect.top)
            self.herir(1)
            if self.collisionRect.centerx < rect.centerx:
                self.empujar("left")
            else:
                self.empujar("right")

    def herir(self, dano):
        self.vida -= int(dano)
        if self.vida <= 0:
            self.kill()
            if self.esEnemigo:
                enemigoMuerto = pygame.event.Event(ENEMIGO_MUERTO, posicion=self.collisionRect.center)
                pygame.event.post(enemigoMuerto)
            else:
                pygame.event.post(pygame.event.Event(MUERTO))
        sonido = pygame.mixer.Sound("./media/sonidos/golpe.mp3")
        sonido.play()

    def curar(self, cantidad):
        self.vida += cantidad
        if self.vida >= VIDA[self.clase]:
            self.vida = VIDA[self.clase]

    def atacar(self):
        if not self.atacando:
            self.golpe = 1
            self.atacando = True
            self.imagenIndex = 0

    def siguienteGolpe(self):
        self.golpe += 1
        if self.golpe > self.golpesPorAtaque:
            self.golpe = self.golpesPorAtaque
        self.danoAtaque = DANO_ATAQUE[self.clase][self.golpe - 1] * self.dificultad
        self.weaponRect = pygame.rect.Rect((0, 0), TAMANOS_ATAQUES[self.clase][self.golpe - 1])
        self.weaponRect.w = int(self.weaponRect.w * self.escala)
        self.weaponRect.h = int(self.weaponRect.h * self.escala)

    def mover(self, vx, vy):
        self.x, self.y = self.x + vx, self.y + vy
        self.collisionRect.center = (self.x, self.y)

    def posicionar(self, x, y):
        self.x, self.y = x, y
        self.collisionRect.center = (x, y)
        self.alinearRects()

    def setBottom(self, bottom):
        self.collisionRect.bottom = bottom
        self.posicionar(self.x, self.collisionRect.centery)

    def alinearRects(self):
        self.rect = self.image.get_rect()
        if self.direccion == "left":
            self.rect.right = self.collisionRect.right
            self.weaponRect.right = self.collisionRect.left
        elif self.direccion == "right":
            self.rect.left = self.collisionRect.left
            self.weaponRect.left = self.collisionRect.right
        self.rect.bottom = self.collisionRect.bottom
        self.weaponRect.bottom = self.collisionRect.bottom - self.alturaGolpes[self.golpe - 1]

    def update(self):
        if self.esEnemigo and not self.entrando:
            self.ia.update()
        escenaRect = pygame.rect.Rect(0, 0, WIDTH, HEIGHT - ALTURA_BASE)
        self.tiempoSalto += 0.017
        self.tiempoParaAnimar -= 1000 / 60
        if self.tiempoParaAnimar <= 0:
            self.animar()
            self.tiempoParaAnimar = self.animacionDelay
        self.vy += self.gravedad * self.tiempoSalto
        if self.empuje is not None:
            if self.empuje == "left":
                self.mover(-4, self.vy)
            elif self.empuje == "right":
                self.mover(4, self.vy)
        else:
            self.mover((self.vx), (self.vy))
        self.mantenerDentroDe(escenaRect)
        self.alinearRects()

    def escalar(self, escala):
        self.escala = escala
        self.image = pygame.transform.scale(self.image, (int(self.width * self.escala), int(self.height * self.escala)))
        self.collisionRect.w = int(self.collisionRect.w * escala)
        self.collisionRect.h = int(self.collisionRect.h * escala)
        self.collisionRect.center = (self.x, self.y)
        self.weaponRect.w = int(self.weaponRect.w * escala)
        self.weaponRect.h = int(self.weaponRect.h * escala)
        if VELOCIDAD_MOVIMIENTO[self.clase] != 0:
            wMov, hMov = TAMANOS_SPRITES[self.clase]["movimiento"][0] * escala, TAMANOS_SPRITES[self.clase]["movimiento"][1] * escala
        wAtaque, hAtaque = TAMANOS_SPRITES[self.clase]["ataque"][0] * escala, TAMANOS_SPRITES[self.clase]["ataque"][1] * escala
        wSalto, hSalto = TAMANOS_SPRITES[self.clase]["salto"][0] * escala, TAMANOS_SPRITES[self.clase]["salto"][1] * escala
        for j in range(2):
            for i in range(len(self.imagenesCorriendo)):
                self.imagenNormal[j] = pygame.transform.scale(self.imagenNormal[j], (int(self.width * self.escala), int(self.height * self.escala)))
                self.imagenesCorriendo[i][j] = pygame.transform.scale(self.imagenesCorriendo[i][j], (int(wMov), int(hMov)))
            for i in range(len(self.imagenesSaltando)):
                    self.imagenesSaltando[i][j] = pygame.transform.scale(self.imagenesSaltando[i][j], (int(wSalto), int(hSalto)))
            for i in range(len(self.imagenesAtacando)):
                    self.imagenesAtacando[i][j] = pygame.transform.scale(self.imagenesAtacando[i][j], (int(wAtaque), int(hAtaque)))

    def animar(self):
        self.imagenIndex += 1
        # Controla el numero del frame a dibujar segun la situacion
        # atacando
        if self.atacando:
            for frame in self.framesDano:
                if self.imagenIndex == frame - 1:
                    atacar = pygame.event.Event(ATAQUE_MELE, weaponRect=self.weaponRect, esEnemigo=self.esEnemigo, dano=self.danoAtaque, direccion=self.direccion)
                    pygame.event.post(atacar)
                    self.siguienteGolpe()
            # fin del ataque
            if self.imagenIndex >= self.framesAnimacion["ataque"]:
                self.danoAtaque = DANO_ATAQUE[self.clase][0] * self.dificultad
                self.imagenIndex = 0
                self.atacando = False
                if self.vx > 0:
                    self.direccion = "right"
                elif self.vx < 0:
                    self.direccion = "left"
        # si esta saltando
        elif self.saltos > 0 and self.numeroSaltos > 0:
            # hacia arriba
            if self.vy < 0 and self.imagenIndex >= int(self.framesAnimacion["salto"] / 2):  # 2
                self.imagenIndex = int(self.framesAnimacion["salto"] / 2) - 1
            # cayendo
            if self.vy > 0 and self.imagenIndex >= self.framesAnimacion["salto"]:
                self.imagenIndex = self.framesAnimacion["salto"] - 1
        # Si esta corriendo
        elif self.imagenIndex >= self.framesAnimacion["movimiento"]:
            self.imagenIndex = 0
        # camina hacia la derecha
        if not self.atacando:
            if self.vx > 0 and self.saltos == 0:
                self.image = self.imagenesCorriendo[int(self.imagenIndex)][1]
            # camina hacia la izquierda
            elif self.vx < 0 and self.saltos == 0:
                self.image = self.imagenesCorriendo[int(self.imagenIndex)][0]
            # se detiene mirando hacia la derecha
            elif self.direccion == "right" and self.vx == 0:
                self.image = self.imagenNormal[1]
            # se detiene mirando hacia la izquierda
            elif self.direccion == "left" and self.vx == 0:
                self.image = self.imagenNormal[0]
            # esta saltando
            if self.saltos > 0 and self.numeroSaltos > 0:
                # carga la imagen segun direccion
                if self.direccion == "right":
                    self.image = self.imagenesSaltando[int(self.imagenIndex)][1]
                elif self.direccion == "left":
                    self.image = self.imagenesSaltando[int(self.imagenIndex)][0]
        elif self.atacando:
            # carga la imagen segun direccion
            if self.direccion == "left":
                self.image = self.imagenesAtacando[self.imagenIndex][0]
            elif self.direccion == "right":
                self.image = self.imagenesAtacando[self.imagenIndex][1]
        self.rect = self.image.get_rect()

    def mantenerDentroDe(self, rect):
        if self.collisionRect.right >= rect.right and not self.entrando:
            self.collisionRect.right = rect.right
            self.x = self.collisionRect.centerx
        if self.collisionRect.left <= rect.left and not self.entrando:
            self.collisionRect.left = rect.left
            self.x = self.collisionRect.centerx
        if self.collisionRect.top <= rect.top:
            self.collisionRect.top = rect.top
            self.y = self.collisionRect.centery
        if self.collisionRect.bottom > rect.bottom:
            self.setBottom(rect.bottom)
            self.cancelarSalto()
            self.detenerEmpuje()
        if self.entrando and (self.collisionRect.left > rect.left and self.collisionRect.right < rect.right):
            self.entrando = False

    def cargarImagenes(self):
        for i in range(1, FRAMES_ANIMACION[self.clase]["movimiento"] + 1):
            imagen = pygame.image.load(self.imagePath + "walk" + str(i) + ".png")
            imagenD = pygame.transform.scale(imagen, (int(self.width * self.escala), int(self.height * self.escala)))
            imagenI = pygame.transform.flip(imagenD, True, False)
            self.imagenesCorriendo.append([imagenI, imagenD])
        for i in range(1, FRAMES_ANIMACION[self.clase]["salto"] + 1):
            imagen = pygame.image.load(self.imagePath + "jump" + str(i) + ".png")
            imagenD = pygame.transform.scale(imagen, (int(self.width * self.escala), int(self.height * self.escala)))
            imagenI = pygame.transform.flip(imagenD, True, False)
            self.imagenesSaltando.append([imagenI, imagenD])
        for i in range(1, FRAMES_ANIMACION[self.clase]["ataque"] + 1):
            imagen = pygame.image.load(self.imagePath + "ataque" + str(i) + ".png")
            imagenD = pygame.transform.scale(imagen, (int(imagen.get_rect().w * self.escala), int(imagen.get_rect().h * self.escala)))
            imagenI = pygame.transform.flip(imagenD, True, False)
            self.imagenesAtacando.append([imagenI, imagenD])