from pygame.locals import*

WIDTH = 800
HEIGHT = 500
flags = FULLSCREEN | DOUBLEBUF
#flags = DOUBLEBUF
#------
#USEREVENTS
MUERTO = USEREVENT
ATAQUE_MELE = USEREVENT + 1
ENEMIGO_MUERTO = USEREVENT + 2
META_COMPLETADA = USEREVENT + 3
HABILITAR_ATAQUE = USEREVENT + 4