TAMANOS_SPRITES = {
    "swordman": {"colision": (20, 35), "ataque": (65, 40), "salto": (32, 37), "movimiento": (28, 35)},
    "goblin": {"colision": (17, 18), "ataque": (34, 19), "salto": (0, 0), "movimiento": (18, 20)}
    }

ALTURAS_GOLPES = {
    "swordman": [0],
    "goblin": [4, 2]
    }

GOLPES_POR_ATAQUE = {
    "swordman": 1,
    "goblin": 2
}

TIPO_ATAQUE = {
    "swordman": "mele",
    "goblin": "mele"}

TAMANOS_ATAQUES = {
    "swordman": [(45, 40)],
    "goblin": [(10, 7), (17, 8)]
}

ANIMACION_DELAY = {
    "swordman": 100.0,
    "goblin": 100.0
}

NUMERO_SALTOS = {
    "swordman": 1,
    "goblin": 0
}

VELOCIDAD_MOVIMIENTO = {
    "swordman": 4,
    "goblin": 2.5
}

VIDA = {
    "swordman": 6,
    "goblin": 4
}

DANO_ATAQUE = {
    "swordman": [2],
    "goblin": [1, 2]
}

FRAMES_DANO = {  # 0 = null | frames donde hace dano
    "swordman": [3],
    "goblin": [2, 5]
}

FRAMES_ANIMACION = {
    "swordman": {"ataque": 4, "salto": 6, "movimiento": 8},
    "goblin": {"ataque": 8, "salto": 0, "movimiento": 4}
}

ENEMIGOS_ETAPA = {
    "1-1": 5,
    "1-2": 8,
    "1-3": 10,
    "2-1": 15,
    "2-2": 20,
    "2-3": 25
}

CLASES_ETAPA = {
    "1-1": ["goblin"],
    "1-2": ["goblin"],
    "1-3": ["goblin"],
    "2-1": ["goblin"],
    "2-2": ["goblin"],
    "2-3": ["goblin"]
}

VELOCIDAD_TRANSICION = 10