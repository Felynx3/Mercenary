# ------------------------CLASES-------------------------
TAMANOS_SPRITES = {
    "swordman": {"colision": (20, 35), "ataque": (65, 40), "salto": (32, 37), "movimiento": (28, 35)},
    "goblin": {"colision": (17, 18), "ataque": (34, 19), "salto": (0, 0), "movimiento": (18, 20)},
    "gargolaT": {"colision": (25, 27), "ataque": (30, 31), "salto": (0, 0), "quieto": (25, 29), "carga": (30, 30)}
    }

ALTURAS_GOLPES = {
    "swordman": [0],
    "goblin": [4, 2],
    "gargolaT": [10]  # CAMBIAR
    }

GOLPES_POR_ATAQUE = {
    "swordman": 1,
    "goblin": 2,
    "gargolaT": 1
}

DELAY_DISPARO = {
    "gargolaT": 500.0
}

TIEMPO_CARGA = {
    "gargolaT": 600.0
}

TIPO_ATAQUE = {
    "swordman": "mele",
    "goblin": "mele",
    "gargolaT": "hibrido"
}

TAMANOS_ATAQUES = {
    "swordman": [(45, 40)],
    "goblin": [(10, 7), (17, 8)],
    "gargolaT": [(10, 10)]  # CAMBIAR
}

ANIMACION_DELAY = {
    "swordman": 100.0,
    "goblin": 100.0,
    "gargolaT": 120.0
}

NUMERO_SALTOS = {
    "swordman": 1,
    "goblin": 0,
    "gargolaT": 1
}

VELOCIDAD_MOVIMIENTO = {
    "swordman": 4,
    "goblin": 2.5,
    "gargolaT": 0
}

VIDA = {
    "swordman": 16,
    "goblin": 4,
    "gargolaT": 24
}

DANO_ATAQUE = {
    "swordman": [2],
    "goblin": [1, 2],
    "gargolaT": [6]
}

FRAMES_DANO = {  # 0 = null | frames donde hace dano
    "swordman": [3],
    "goblin": [2, 5],
    "gargolaT": [3]  # CAMBIAR
}

FRAMES_ANIMACION = {
    "swordman": {"ataque": 4, "salto": 6, "movimiento": 8},
    "goblin": {"ataque": 8, "salto": 0, "movimiento": 4},
    "gargolaT": {"quieto": 3, "cargando": 4}  # CAMBIAR
}

# ----------------------PROYECTILES---------------------------
PROYECTILES = {
    "gargolaT": ["vackura"]
}

TAMANO_PROYECTIL = {
    "vackura": {"normal": (40, 30), "colision": (24, 30), "muerte": (28, 28)}
}

DANO_PROYECTIL = {
    "vackura": 4
}

VELOCIDAD_PROYECTIL = {
    "vackura": 3
}

FRAMES_PROYECTIL = {
    "vackura": {"normal": 3, "muerte": 3}
}

ANIMACION_DELAY_PROYECTIL = {
    "vackura": 100.0
}

# --------------------------ETAPAS---------------------------
ENEMIGOS_ETAPA = {
    "1-1": 5,
    "1-2": 8,
    "1-3": 10,
    "2-1": 12,
    "2-2": 15,
    "2-3": 18
}

CLASES_ETAPA = {
    "1-1": ["goblin"],
    "1-2": ["goblin"],
    "1-3": ["goblin"],
    "2-1": ["goblin"],
    "2-2": ["goblin"],
    "2-3": ["goblin"]
}

# ------------------------OTROS------------------------------
ULTIMA_ZONA = 2
VELOCIDAD_TRANSICION = 10
ALTURA_BASE = 40