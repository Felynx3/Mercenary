from lib import*
from random import randint
from clases import*
from jefes import*


class EnemySpawner:

    def __init__(self, gameState, enemigos, dificultad, objetivo):  # 1 = facil
        self.objetivo = objetivo
        self.dificultad = dificultad
        self.enemigos = enemigos
        self.gameState = gameState
        self.clases = CLASES_ETAPA[self.gameState.getEtapa()]
        self.spawnDelay = 1.2 / dificultad
        self.tiempoEspera = 2.0
        self.jefeDesplegado = False

    def update(self):
        self.tiempoEspera -= 0.01
        if self.tiempoEspera <= 0:
            self.spawnEnemy()
            self.tiempoEspera = self.spawnDelay

    def reiniciar(self):
        self.clases = CLASES_ETAPA[self.gameState.getEtapa()]
        self.jefeDesplegado = False
        self.enemigos.empty()
        self.tiempoEspera = 2.5

    def spawnEnemy(self):
        numeroClase = randint(0, (len(self.clases) - 1) * 3) / 3
        clase = self.clases[numeroClase]
        if clase == "jefe":
            if not self.jefeDesplegado:
                self.desplegarJefe()
            return
        enemigo = Sprite("enemigo", clase, True)
        enemigo.enemigo(self.dificultad, self.objetivo)
        ladoEntrada = randint(0, 1)
        lados = ["left", "right"]
        enemigo.entrar(lados[ladoEntrada])
        self.enemigos.add(enemigo)

    def desplegarJefe(self):
        self.jefeDesplegado = True
        if self.gameState.zona == 1:
            jefe = GargolaT(self.objetivo)
            jefe.posicionar(40, 0)
            self.enemigos.add(jefe)