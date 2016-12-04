import pygame
import os
from random import randint


class CajaMusica:

    def __init__(self):
        self.musicPath = os.path.join(".", "media", "sonidos", "musica", "fondo")
        self.canciones = []
        self.derrota = None
        self.index = 0
        self.cantidadCanciones = 1
        self.cargarCanciones()

    def cargarCanciones(self):
        for i in range(1, self.cantidadCanciones + 1):
            cancion = self.musicPath + str(i) + ".mp3"
            self.canciones.append(cancion)
        self.derrota = os.path.join(".", "media", "sonidos", "musica", "derrota.mp3")
        self.musicaTaberna = os.path.join(".", "media", "sonidos", "musica", "taberna.mp3")

    def update(self):
        if not pygame.mixer.music.get_busy():
            self.index += 1
            if self.index >= self.cantidadCanciones:
                self.index = 0
            pygame.mixer.music.load(self.canciones[self.index])
            pygame.mixer.music.play(0)

    def gameOver(self):
        pygame.mixer.music.load(self.derrota)
        pygame.mixer.music.play(0)

    def reiniciar(self):
        num = randint(0, self.cantidadCanciones - 1)
        pygame.mixer.music.load(self.canciones[num])

    def taberna(self):
        pygame.mixer.music.load(self.musicaTaberna)
        pygame.mixer.music.play(0)