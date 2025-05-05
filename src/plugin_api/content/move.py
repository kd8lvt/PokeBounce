import pygame
from src import physics
from src.debug import showHitboxes
from src.globals import g
from src.sprite_loader import INSTANCE as sprites

class MoveText:
    ttl = 60
    alpha = 0

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def tick(self):
        self.ttl -= 1
        self.y -= 0.50

        if self.ttl >= 50 and self.alpha < 230:
            self.alpha += 20
        elif self.ttl <= 20 and self.alpha > 15:
            self.alpha -= 10


class Move(physics.PhysicsObject):

    def __init__(self,type,colour,damage,graphic,usingTime,acceleration,linearAcceleration,growth,linearGrowth,image):
        self.type = type
        self.colour = colour
        self.damage = damage
        self.graphic = graphic
        self.usingTime = usingTime
        self.acceleration = acceleration
        self.linearAcceleration = linearAcceleration
        self.growth = growth
        self.linearGrowth = linearGrowth
        self.image = image

    def spawn(self, poke):
        self.x = poke.x + poke.size / 2
        self.y = poke.y + poke.size / 2
        super().__init__(self.x, self.y, self.size, self.size, True)
        self.ttl = 0
        self.rotate = 0
        self.rotSpeed = 0
        self.poke = poke

    def update(self):
        self.move()

    def move(self):
        self.x += self.xVel
        self.y += self.yVel

        self.xVel += self.linearAcceleration
        self.yVel += self.linearAcceleration

        self.xVel *= self.acceleration
        self.yVel *= self.acceleration

        self.size += self.linearGrowth
        self.size *= self.growth

        if self.size < 1:
            physics.allObjects.remove(self)
            return

        self.resize(self.size, self.size)
        self.rotate += self.rotSpeed

        self.ttl -= 1
        if self.ttl == 0:
            physics.allObjects.remove(self)

    def draw(self):
        if showHitboxes:
            pygame.draw.rect(g.window, self.colour, self.getCollider())
        if self.graphic == "image":
            moveImage = sprites.moves.get(self.image)
            if moveImage is None:
                raise Exception(f"Move image is <None>! {self.image}")
            moveImage = pygame.transform.scale(moveImage, (self.size, self.size))
            if moveImage is None:
                print("Move image is <None>! "+self.image)

            rotatedImage = pygame.transform.rotate(moveImage, self.rotate)

            new_rect = rotatedImage.get_rect(center=moveImage.get_rect(center=(self.x + self.size/2, self.y + self.size/2)).center)
            g.window.blit(rotatedImage, new_rect)
        elif self.graphic == "rect":
            pygame.draw.rect(g.window, self.colour, self.getCollider())
        elif self.graphic == "circle":
            pygame.draw.circle(g.window, self.colour, self.getCollider().center, self.size/2)
    
    def use(self,poke):
        if poke.usingMoveTimer == self.usingTime:
            poke.moveText = MoveText(poke.x, poke.y, poke.usingMove)
        poke.usingMoveTimer -= 1
        if poke.usingMoveTimer == 0:
            poke.usingMove = ""