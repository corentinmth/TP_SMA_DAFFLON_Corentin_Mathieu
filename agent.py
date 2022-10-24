from random import random

import core
import pygame
import uuid
from body import Body
from pygame.math import Vector2


class Agent:
    def __init__(self):
        self.uuid = str(uuid.uuid4())
        self.body = Body()
        #sain blanc, infecté rouge, blesse vert
        self.statut = self.statut


    def show(self, window):
        agent_pos = self.body.pos
        agent_radius = self.body.radius
        agent_color = self.body.color
        pygame.draw.circle(window, agent_color,
                           agent_pos, agent_radius)

    def update(self):
        self.vitesse = Vector2(random.randint(-10, 10), random.randint(-10, 10))
