from GameOver import*


class GameState:

    def __init__(self, fondo):
        self.fondo = fondo
        self.zona = 1
        self.etapa = 1
        self.estado = "menu"
        self.pausa = False

        self.gameOverScreen = GameOver()

    def siguienteEtapa(self):
        self.etapa += 1
        if self.etapa > 3:
            self.etapa = 1
            self.zona += 1
        self.fondo.cambioEscena(self.zona, self.etapa)
        if self.etapa > 3:
            self.etapa = 1
            self.zona += 1
        if self.zona >= 3:
            #hacer algo cuando se termina el juego
            print("ganaste")
            pygame.event.post(pygame.event.Event(QUIT))
        self.fondo.cambioEscena(self.zona, self.etapa)

    def reiniciarZona(self):
        self.etapa = 2
        self.etapa = 1
        self.fondo.cambioEscena(self.zona, 1)
        self.estado = "jugando"
        self.pausa = False

    def getEtapa(self):
        return str(self.zona) + "-" + str(self.etapa)

    def pausar(self):
        if self.estado == "jugando":
            self.pausa = not self.pausa

    def jugar(self):
        self.estado = "jugando"
        self.pausa = False
        self.fondo.cambioEscena(1, 1)

    def gameOver(self):
        self.estado = "gameover"

    def drawGameOver(self, screen):
        self.gameOverScreen.draw(screen)