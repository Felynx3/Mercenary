import pygame
from datosClases import*


class CajaSonidos:

    def __init__(self, clase):
        self.clase = clase
        directorio = "./media/sonidos/" + clase + "/"
        if NUMERO_SALTOS[self.clase] > 0:
            self.sonidos = {
                "salto": pygame.mixer.Sound(directorio + "salto.mp3"),
                "caida": pygame.mixer.Sound(directorio + "caida.mp3")}
        else:
            self.sonidos = {
                "caida": pygame.mixer.Sound(directorio + "caida.mp3")}

    def reproducir(self, sonido):
        self.sonidos[sonido].play()

        #ARREGLAR SONIDO MUERTE: