import pygame


class InputHandler:

    def __init__(self):
        self.eventos = pygame.event.get()

    def get(self):
        return self.eventos