import pygame


class CajaSonidos:

    def __init__(self, clase):
        self.clase = clase
        directorio = "./media/sonidos/" + clase + "/"
        if clase != "bomba":
            self.sonidos = {
                "salto": pygame.mixer.Sound(directorio + "salto.mp3"),
                "caida": pygame.mixer.Sound(directorio + "caida.mp3")}

    def reproducir(self, sonido):
        if self.clase != "bomba":
            self.sonidos[sonido].play()