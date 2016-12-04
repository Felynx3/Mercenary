# ------------------------CLASES-------------------------
TAMANOS_SPRITES = {
    "swordman": {"colision": (20, 35), "ataque": (65, 40), "salto": (32, 37), "movimiento": (28, 35)},
    "goblin": {"colision": (17, 18), "ataque": (34, 19), "salto": (0, 0), "movimiento": (18, 20)},
    "minitroll": {"colision": (17, 18), "ataque": (34, 19), "salto": (0, 0), "movimiento": (18, 20)},
    "frozen": {"colision": (17, 18), "ataque": (34, 19), "salto": (0, 0), "movimiento": (18, 20)},
    "imp": {"colision": (17, 18), "ataque": (34, 19), "salto": (0, 0), "movimiento": (18, 20)},
    "gargolaT": {"colision": (25, 27), "ataque": (30, 31), "salto": (0, 0), "quieto": (25, 29), "carga": (30, 30)}
    }

ALTURAS_GOLPES = {
    "swordman": [0],
    "goblin": [4, 2],
    "minitroll": [4, 2],
    "frozen": [4, 2],
    "imp": [4, 2],
    "gargolaT": [10]  # CAMBIAR
    }

GOLPES_POR_ATAQUE = {
    "swordman": 1,
    "goblin": 2,
    "minitroll": 2,
    "frozen": 2,
    "imp": 2,
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
    "gargolaT": "hibrido",
    "minitroll": "mele",
    "imp": "mele",
    "frozen": "mele"
}

TAMANOS_ATAQUES = {
    "swordman": [(45, 40)],
    "goblin": [(10, 7), (17, 8)],
    "minitroll": [(10, 7), (17, 8)],
    "imp": [(10, 7), (17, 8)],
    "frozen": [(10, 7), (17, 8)],
    "gargolaT": [(10, 10)]  # CAMBIAR
}

ANIMACION_DELAY = {
    "swordman": 100.0,
    "goblin": 100.0,
    "minitroll": 80.0,
    "imp": 70,
    "frozen": 90,
    "gargolaT": 120.0
}

NUMERO_SALTOS = {
    "swordman": 1,
    "goblin": 0,
    "minitroll": 0,
    "imp": 0,
    "frozen": 0,
    "gargolaT": 1
}

VELOCIDAD_MOVIMIENTO = {
    "swordman": 4,
    "goblin": 2.5,
    "minitroll": 2.7,
    "imp": 3.0,
    "frozen": 2.6,
    "gargolaT": 0
}

VIDA = {
    "swordman": 16,
    "goblin": 4,
    "minitroll": 6,
    "imp": 8,
    "frozen": 12,
    "gargolaT": 24
}

DANO_ATAQUE = {
    "swordman": [2],
    "goblin": [1, 2],
    "minitroll": [2, 2],
    "imp": [2, 4],
    "frozen": [2, 2],
    "gargolaT": [6]
}

FRAMES_DANO = {  # 0 = null | frames donde hace dano
    "swordman": [3],
    "goblin": [2, 5],
    "minitroll": [2, 5],
    "imp": [2, 5],
    "frozen": [2, 5],
    "gargolaT": [3]  # CAMBIAR
}

FRAMES_ANIMACION = {
    "swordman": {"ataque": 4, "salto": 6, "movimiento": 8},
    "goblin": {"ataque": 8, "salto": 0, "movimiento": 4},
    "minitroll": {"ataque": 8, "salto": 0, "movimiento": 4},
    "imp": {"ataque": 8, "salto": 0, "movimiento": 4},
    "frozen": {"ataque": 8, "salto": 0, "movimiento": 4},
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
    "1-3": 12,
    "2-1": 15,
    "2-2": 1,
    "2-3": 20
}

JEFE_ZONA = {
    "1": ["gargolaT"]
    }

CLASES_ETAPA = {
    "1-1": ["goblin"],
    "1-2": ["minitroll", "goblin"],
    "1-3": ["minitroll", "imp"],
    "2-1": ["imp", "frozen"],
    "2-2": ["jefe"],
    "2-3": ["frozen"]
}

# -------------------------MENU------------------------------
FRAMES_OPCION = {
    "jugar": 3,
    "salir": 3
}

ANIMACION_PING_PONG = {
    "jugar": True,
    "salir": True
}

POSX_OPCION = {
    "jugar": 100,
    "salir": 698
}
# ------------------------OTROS------------------------------
ULTIMA_ZONA = 2
VELOCIDAD_TRANSICION = 10
ALTURA_BASE = 60