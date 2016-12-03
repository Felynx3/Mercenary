import pygame
from datosClases import*


class CajaSonidos:

    def __init__(self):
        self.directorio = "./media/sonidos/efectos/"

    def reproducir(self, sonido):
        sonido = pygame.mixer.Sound(self.directorio + sonido + ".wav")
        sonido.play()