import pygame
import sys
from pygame.locals import*
from datos import*
from clases import*


def main():
    pygame.mixer.pre_init(22050, 16, 2, 64)
    pygame.mixer.init()
    pygame.init()
    pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
    pygame.mixer.music.load("./media/sonidos/musica/fondo1.mp3")
    pygame.mixer.music.play(-1)

    collisionManager = CollisionManager()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
    fondo = Fondo(1, 1, screen)
    gameState = GameState(fondo)

    jugador = pygame.sprite.GroupSingle()
    enemigos = pygame.sprite.Group()

    personaje = Sprite("aifecs", "swordman", False)
    personaje.velocidadMovimiento = 4
    personaje.posicionar(WIDTH / 2, HEIGHT / 2)
    enemySpawner = EnemySpawner(gameState, enemigos, 1, personaje)
    jugador.add(personaje)

    menu = MenuPrincipal(personaje)
    hud = Hud(jugador, enemigos, gameState)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                key = pygame.key.name(event.key)
                if key == "q":
                    pygame.quit()
                    sys.exit()
                if key == "space":
                    personaje.saltar()
                if key == "left":
                    personaje.correr("left")
                if key == "right":
                    personaje.correr("right")
                if key == "p":
                    gameState.pausar()
                if key == "r" and gameState.estado == "gameover":
                    gameState.reiniciarZona()
                    enemySpawner.reiniciar()
                    personaje.reiniciar()
                    hud.reiniciar()
                    jugador.add(personaje)
                if key == "z":
                    if gameState.estado == "jugando":
                        personaje.atacar()
                    if gameState.estado == "menu":
                        if menu.getOpcion(personaje) == "jugar":
                            gameState.jugar()
                if key == "a":
                    enemySpawner.spawnEnemy()
                if key == "o":
                    pygame.display.toggle_fullscreen()
            if event.type == KEYUP:
                key = pygame.key.name(event.key)
                if key == "left":
                    personaje.detener("left")
                if key == "right":
                    personaje.detener("right")
            if event.type == MUERTO:
                gameState.gameOver()
            if event.type == ATAQUE_MELE:
                collisionManager.colisionArma(event.weaponRect, event.esEnemigo, jugador.sprite, enemigos, event.dano)
            if event.type == ENEMIGO_MUERTO:
                hud.enemigoMuerto()
            if event.type == META_COMPLETADA:
                gameState.siguienteEtapa()
                enemySpawner.reiniciar()

        fondo.update()

        if gameState.estado == "jugando":
            if not gameState.pausa:
                jugador.update()
                enemigos.update()
                collisionManager.colisionConGrupo(personaje, enemigos)
                hud.update()
                enemySpawner.update()

            enemigos.draw(screen)
            jugador.draw(screen)
            hud.draw(screen)

        if gameState.estado == "menu":
            jugador.update()
            menu.update()
            menu.draw(screen)
            jugador.draw(screen)
            if menu.getOpcion == "jugar":
                gameState.jugar()

        if gameState.estado == "gameover":
            gameState.drawGameOver(screen)

        pygame.display.update()
        clock.tick(60)