from lib import*


class CollisionManager:

    def __init__(self):
        pass

    def colisionConGrupo(self, personaje, grupo):
        personajeCollisionRect = personaje.collisionRect
        for sprite in grupo.sprites():
            groupCollisionRect = sprite.collisionRect
            if personajeCollisionRect.colliderect(groupCollisionRect):
                personaje.colisionar(groupCollisionRect)
                sprite.colisionar(personajeCollisionRect)

    def colisionArma(self, armaRect, esEnemigo, personaje, grupo, dano):
        if not esEnemigo:
            for enemy in grupo.sprites():
                if armaRect.colliderect(enemy.collisionRect):
                    enemy.herir(dano)
        if esEnemigo and personaje is not None:
            if armaRect.colliderect(personaje.collisionRect):
                personaje.herir(dano)