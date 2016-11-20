from lib import*


class CollisionManager:

    def __init__(self):
        pass

    def colisionConGrupo(self, personaje, grupo):
        rect = personaje.collisionRect
        for sprite in grupo.sprites():
            grouprect = sprite.collisionRect
            if rect.colliderect(grouprect):
                personaje.colisionar(grouprect)
                sprite.colisionar(rect)

    def colisionArma(self, armaRect, esEnemigo, personaje, grupo, dano, direccion):
        if not esEnemigo:
            for enemy in grupo.sprites():
                if armaRect.colliderect(enemy.collisionRect):
                    enemy.herir(dano)
                    enemy.empujar(direccion)
        if esEnemigo and personaje is not None:
            if armaRect.colliderect(personaje.collisionRect):
                personaje.herir(dano)
                personaje.empujar(direccion)

    def collisionProyectiles(self, personaje, enemigos, proyectiles):
        for proyectil in proyectiles:
            if proyectil.enemigo:
                if personaje.collisionRect.colliderect(proyectil.collisionRect) and not proyectil.muerto:
                    personaje.herir(proyectil.dano)
                    proyectil.kill()
            else:
                for enemigo in enemigos:
                    if enemigo.collisionRect.colliderect(proyectil.collisionRect) and not proyectil.muerto:
                        enemigo.herir(proyectil.dano)
                        proyectil.kill()