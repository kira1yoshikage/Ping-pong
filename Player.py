from pygame import *
from GameSprite import GameSprite

class Player(GameSprite):
    def movement1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_d] and self.rect.y < self.height - 100:
            self.rect.y += self.speed

    def movement2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.y < self.height - 100:
            self.rect.y += self.speed