import pygame
import os
from datos import*


class Hud:

    def __init__(self, jugador, enemigos, gameState):
        self.gameState = gameState
        self.jugador = jugador
        self.enemigos = enemigos
        self.vida = jugador.sprite.vida
        self.metaEnemigos = ENEMIGOS_ETAPA[str(gameState.zona) + "-" + str(gameState.etapa)]
        self.cantEnemigos = 0
        self.font = pygame.font.Font(os.path.join(".", "media", "fuentes", "8-BIT WONDER.TTF"), 50)
        self.textoEnemigos = self.font.render(str(self.cantEnemigos) + "/" + str(self.metaEnemigos), True, (0, 0, 0))
        self.rect = pygame.rect.Rect((0, 0), (0, 0))
        self.enemigosRect = self.textoEnemigos.get_rect()
        self.imagePath = os.path.join(".", "media", "imagenes", "interfaz", "")

        self.corazones = []
        self.estadosCorazones = []
        self.imagenesCorazones = []
        self.inicializarCorazones()

    def reiniciar(self):
        self.cantEnemigos = 0
        self.metaEnemigos = ENEMIGOS_ETAPA[str(self.gameState.zona) + "-" + str(self.gameState.etapa)]

    def update(self):
        self.metaEnemigos = ENEMIGOS_ETAPA[str(self.gameState.zona) + "-" + str(self.gameState.etapa)]
        if self.jugador.sprite is not None:
            self.vida = int(self.jugador.sprite.vida)
        else:  # el sprite es None cuando esta muerto.
            self.vida = 0
        if self.cantEnemigos >= self.metaEnemigos:
            self.cantEnemigos = 0
            metaCompletada = pygame.event.Event(META_COMPLETADA)
            pygame.event.post(metaCompletada)
        self.enemigosRect = self.textoEnemigos.get_rect()
        self.enemigosRect.right = WIDTH
        self.textoEnemigos = self.font.render(str(self.cantEnemigos) + "/" + str(self.metaEnemigos), True, (0, 0, 0))
        self.actualizarCorazones()

    def draw(self, screen):
        for corazon in self.corazones:
            screen.blit(corazon.image, corazon.rect)
        screen.blit(self.textoEnemigos, self.enemigosRect)

    def enemigoMuerto(self):
        self.cantEnemigos += 1

    def actualizarCorazones(self):
        vida = self.vida
        for i in range(len(self.corazones)):
            if vida >= 4:
                self.estadosCorazones[i] = 4
                vida -= 4
            else:
                self.estadosCorazones[i] = vida
                vida = 0
            self.corazones[i].image = self.imagenesCorazones[self.estadosCorazones[i]]

    def inicializarCorazones(self):
        vida = self.vida
        while True:
            if vida >= 4:
                self.estadosCorazones.append(4)
                vida -= 4
            else:
                if vida != 0:
                    self.estadosCorazones.append(vida)
                break
        # Cargar imagenes
        for i in range(5):
            imagenCorazon = pygame.image.load(self.imagePath + "corazon" + str(i) + ".png")
            self.imagenesCorazones.append(pygame.transform.scale(imagenCorazon, (HEIGHT / 8, HEIGHT / 8)))
        # Crear sprites
        i = 0
        for vidaCorazon in self.estadosCorazones:
            corazon = pygame.sprite.Sprite()
            corazon.image = self.imagenesCorazones[vidaCorazon]
            corazon.rect = corazon.image.get_rect()
            corazon.rect.left = i * (corazon.rect.w * 1.1) + corazon.rect.h / 10
            corazon.rect.top = corazon.rect.h / 10
            self.corazones.append(corazon)
            i += 1