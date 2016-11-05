from lib import*
from random import randint
from clases import*


class EnemySpawner:

    def __init__(self, gameState, enemigos, dificultad, objetivo):  # 1 = facil
        self.objetivo = objetivo
        self.dificultad = dificultad
        self.enemigos = enemigos
        self.gameState = gameState
        self.clases = CLASES_ETAPA[self.gameState.getEtapa()]
        self.spawnDelay = 1 / dificultad
        self.tiempoEspera = 2.0

    def update(self):
        self.tiempoEspera -= 0.01
        if self.tiempoEspera <= 0:
            self.spawnEnemy()
            self.tiempoEspera = self.spawnDelay

    def reiniciar(self):
        self.clases = CLASES_ETAPA[self.gameState.getEtapa()]
        self.enemigos.empty()
        self.tiempoEspera = 2.5

    def spawnEnemy(self):
        numeroClase = randint(0, (len(self.clases) - 1) * 3) / 3
        clase = self.clases[numeroClase]
        enemigo = Sprite("enemigo", clase, True)
        enemigo.enemigo(self.dificultad, self.objetivo)
        ladoEntrada = randint(0, 1)
        lados = ["left", "right"]
        enemigo.entrar(lados[ladoEntrada])
        self.enemigos.add(enemigo)