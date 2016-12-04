from GameOver import*
import pygame


class GameState:

    def __init__(self, fondo):
        self.fondo = fondo
        self.zona = 1
        self.etapa = 1
        self.estado = "menu"
        self.pausa = False
        self.boss = False

        self.taberna()
        self.gameOverScreen = GameOver()

    def update(self):
        if self.estado == "apareciendo":
            if not self.fondo.apareciendo:
                self.estado = "jugando"
        if self.estado == "cargandoMenu":
            if not self.fondo.apareciendo:
                self.estado = "menu"

    def siguienteEtapa(self):
        self.boss = False
        self.etapa += 1
        if self.etapa > 3:
            self.etapa = 1
            self.zona += 1
        if self.etapa == 3:
            self.boss = True
        if self.zona > ULTIMA_ZONA:
            #hacer algo cuando se termina el juego
            self.zona = 1
            self.etapa = 1
            pygame.event.post(pygame.event.Event(MUERTO))
        else:
            self.fondo.aparicionEscena(self.zona, self.etapa)

    def contraJefe(self):
        return self.boss

    def taberna(self):
        self.estado = "cargandoMenu"
        self.pausa = False
        self.fondo.taberna()

    def reiniciarZona(self):
        self.etapa = 1
        self.fondo.aparicionEscena(self.zona, self.etapa)
        self.estado = "jugando"
        self.pausa = False
        self.boss = False
        if self.etapa == 3:
            self.boss = True

    def reiniciarEtapa(self):
        self.fondo.aparicionEscena(self.zona, self.etapa)
        self.estado = "jugando"
        self.pausa = False
        self.boss = False
        if self.etapa == 3:
            self.boss = True

    def getEtapa(self):
        return str(self.zona) + "-" + str(self.etapa)

    def pausar(self):
        if self.estado == "jugando":
            self.pausa = not self.pausa

    def jugar(self):
        self.etapa = 1
        self.zona = 1
        self.estado = "apareciendo"
        self.pausa = False
        self.fondo.aparicionEscena(self.zona, self.etapa)

    def gameOver(self):
        self.estado = "gameover"
        self.boss = False

    def drawGameOver(self, screen):
        self.gameOverScreen.draw(screen)