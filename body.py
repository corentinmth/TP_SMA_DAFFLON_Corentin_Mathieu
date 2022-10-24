import random

import core
import pygame
from random import randint

from fustrum import Fustrum
from epidemie import Epidemie

class Body:
    def __init__(self):
        self.fustrum = Fustrum()
        longueur, largeur = pygame.display.get_surface().get_size()
        self.radius = 10
        self.pos = [randint(self.radius, longueur), randint(self.radius, largeur)]
        self.color = (255, 255, 255)
        self.vitesse =Vector2(0,0)


    def update(self):
        if(statut="I"):
            self.color =(255,0,0)
        if(statut="R"):
            self.color = (0,255,0)

        if(distance_to_agt <= distContagion):
            contamination = random.random() * 100
            if contamination <= self.epidemie.tauxTransmission :
                self.agent.statut = "I"




    def distance_to_agt(self, agt_pos):
        return pygame.math.Vector2(self.pos[0], self.pos[1]).distance_to(agt_pos)
