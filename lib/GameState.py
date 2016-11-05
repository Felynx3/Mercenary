from GameOver import*


class GameState:

    def __init__(self, fondo):
        self.fondo = fondo
        self.zona = 1
        self.etapa = 1
        self.estado = "menu"
        self.pausa = False

        self.gameOverScreen = GameOver()

    def update(self):
        if self.estado == "apareciendo":
            if not self.fondo.apareciendo:
                self.estado = "jugando"
        if self.estado == "cargandoMenu":
            if not self.fondo.apareciendo:
                self.estado = "menu"

    def siguienteEtapa(self):
        self.etapa += 1
        if self.etapa > 3:
            self.etapa = 1
            self.zona += 1
        if self.zona > ULTIMA_ZONA:
            #hacer algo cuando se termina el juego
            self.zona = 1
            self.etapa = 1
            self.taberna()
        else:
            self.fondo.cambioEscena(self.zona, self.etapa)

    def taberna(self):
        self.estado = "cargandoMenu"
        self.pausa = False
        self.fondo.taberna()

    def reiniciarZona(self):
        self.etapa = 2
        self.etapa = 1
        self.fondo.aparicionEscena(self.zona, 1)
        self.estado = "jugando"
        self.pausa = False

    def getEtapa(self):
        return str(self.zona) + "-" + str(self.etapa)

    def pausar(self):
        if self.estado == "jugando":
            self.pausa = not self.pausa

    def jugar(self):
        self.estado = "apareciendo"
        self.pausa = False
        self.fondo.aparicionEscena(self.zona, self.etapa)

    def gameOver(self):
        self.estado = "gameover"

    def drawGameOver(self, screen):
        self.gameOverScreen.draw(screen)