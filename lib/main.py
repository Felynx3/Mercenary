import pygame
import sys
from pygame.locals import*
from datos import*
from clases import*


class Mercenary:
    pygame.mixer.pre_init(22050, 16, 2, 64)
    pygame.mixer.init()
    pygame.init()
    pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
    pygame.mixer.music.load("./media/sonidos/musica/fondo1.mp3")
    pygame.mixer.music.play(-1)

    def __init__(self):
        self.collisionManager = CollisionManager()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
        self.fondo = Fondo(self.screen)
        self.gameState = GameState(self.fondo)

        self.jugador = pygame.sprite.GroupSingle()
        self.enemigos = pygame.sprite.Group()
        self.items = pygame.sprite.Group()

        self.items = pygame.sprite.Group()
        self.personaje = Sprite("jugador", "swordman", False)
        self.personaje.posicionar(WIDTH / 2, HEIGHT / 2)

        self.enemySpawner = EnemySpawner(self.gameState, self.enemigos, 1, self.personaje)
        self.itemSpawner = ItemSpawner(self.items, 1)
        self.jugador.add(self.personaje)

        self.menu = MenuPrincipal(self.personaje)
        self.hud = Hud(self.jugador, self.enemigos, self.gameState)

    def keyHandler(self, event):
        if event.type == KEYDOWN:
            key = pygame.key.name(event.key)
            if key == "q":
                pygame.quit()
                sys.exit()
            if key == "space":
                self.personaje.saltar()
            if key == "left":
                self.personaje.correr("left")
            if key == "right":
                self.personaje.correr("right")
            if key == "p":
                self.gameState.pausar()
            if key == "r" and self.gameState.estado == "gameover":
                self.gameState.reiniciarZona()
                self.enemySpawner.reiniciar()
                self.itemSpawner.reiniciar()
                self.personaje.reiniciar()
                self.hud.reiniciar()
                self.jugador.add(self.personaje)
            if key == "z":
                if self.gameState.estado == "jugando":
                    self.personaje.atacar()
                if self.gameState.estado == "menu":
                    if self.menu.getOpcion(self.personaje) == "jugar":
                        self.gameState.jugar()
            if key == "a":
                self.enemySpawner.spawnEnemy()
            if key == "o":
                pygame.display.toggle_fullscreen()
            if key == "t" and self.gameState.estado == "gameover":
                self.gameState.taberna()
                self.personaje.reiniciar()
                self.jugador.add(self.personaje)
        if event.type == KEYUP:
            key = pygame.key.name(event.key)
            if key == "left":
                self.personaje.detener("left")
            if key == "right":
                self.personaje.detener("right")

    def update(self):
        self.fondo.update()
        self.gameState.update()
        if self.gameState.estado == "jugando":
            if not self.gameState.pausa:
                self.jugador.update()
                self.enemigos.update()
                self.items.update()
                self.collisionManager.colisionConGrupo(self.personaje, self.enemigos)
                self.hud.update()
                self.enemySpawner.update()
                self.itemSpawner.update(self.jugador.sprite)
        if self.gameState.estado == "menu":
            self.jugador.update()
            self.menu.update()

    def draw(self):
        if self.gameState.estado == "jugando":
            self.items.draw(self.screen)
            self.enemigos.draw(self.screen)
            self.jugador.draw(self.screen)
            self.hud.draw(self.screen)

        if self.gameState.estado == "menu":
            self.menu.draw(self.screen)
            self.jugador.draw(self.screen)
        if self.gameState.estado == "gameover":
            self.gameState.drawGameOver(self.screen)

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN or event.type == KEYUP:
                    self.keyHandler(event)
                if event.type == MUERTO:
                    self.gameState.gameOver()
                if event.type == ATAQUE_MELE:
                    self.collisionManager.colisionArma(event.weaponRect, event.esEnemigo, self.jugador.sprite, self.enemigos, event.dano)
                if event.type == ENEMIGO_MUERTO:
                    self.hud.enemigoMuerto()
                if event.type == META_COMPLETADA:
                    self.gameState.siguienteEtapa()
                    self.enemySpawner.reiniciar()
                    self.itemSpawner.reiniciar()

            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(60)
