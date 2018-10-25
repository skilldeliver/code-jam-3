import pygame as pg

from project.constants import Color, HEIGHT, WIDTH
from project.sprites.sprite_internals import Physics


class Projectile(Physics, pg.sprite.Sprite):
    """Basic Projectile Sprite"""
    def __init__(self, game, owner, damage: int=2, penetration: int=0, direction: int=1, spawn_point=None, image=None):
        super().__init__()
        self.game = game
        self.owner = owner

        if owner.evil:
            self.add(self.game.all_sprites, self.game.enemy_projectiles)
        else:
            self.add(self.game.all_sprites, self.game.others)

        if direction not in (1, -1):
            print('Direction should be only to mark negative or positive direction.')
        self.direction = direction
        self.damage = damage
        self.penetration = penetration

        if image is None:
            self.image = pg.Surface((15, 15))
            self.image.fill(Color.green)
        else:
            self.image = image

        if spawn_point is None:
            self.pos = owner.rect.midright
        else:
            self.pos = spawn_point

        self.rect = self.image.get_rect(center=self.pos)

    def update(self):
        # TODO BULLET LIFE TIME
        self.friction = 0.012
        super().update()
        self.vel.x = 10 * self.direction

        self.max_speed = 20

        if self.pos.y > HEIGHT:
            self.kill()
            self.owner.projectiles.pop()
        if self.pos.y < 0:
            self.kill()
            self.owner.projectiles.pop()
        if self.pos.x > WIDTH:
            self.kill()
            self.owner.projectiles.pop()
        if self.pos.x < 0:
            self.kill()
            self.owner.projectiles.pop()


class Item(pg.sprite.Sprite):
    """Represents items such as drops"""
