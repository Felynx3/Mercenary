import pygame
import os


class CajaMusica:

    def __init__(self):
        pygame.mixer.pre_init(22050, 16, 2, 64)
        pygame.mixer.init()
        self.musicPath = os.path.join(".", "media", "sonidos", "musica", "fondo")
        self.canciones = []
        self.derrota = None
        self.index = 0
        self.cantidadCanciones = 2
        self.cargarCanciones()

    def cargarCanciones(self):
        for i in range(1, 2):
            cancion = self.musicPath + str(i) + ".mp3"
            self.canciones.append(cancion)

    def update(self):
        if not pygame.mixer.music.get_busy():
            self.index += 1
            if self.index >= self.cantidadCanciones:
                self.index = 0
            pygame.mixer.music.load(self.canciones[self.index])
            pygame.mixer.music.play(0)

    def gameOver(self):

    def taberna(self):
        pass
        # Cambiar la cancion a la destinada para la taberna :p