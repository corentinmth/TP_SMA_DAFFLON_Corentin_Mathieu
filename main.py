import core

from body import Body
from agent import Agent
from fustrum import Fustrum


def setup():
    core.fps = 3
    core.WINDOW_SIZE = [800, 600]

def run():
    core.cleanScreen()



def computePerception():
    for agent in self.list_agents:
        for index, agent in enumerate(self.list_agents):
            if agent.body.distance_to_agt(agent.body.pos) < (agent.fustrum.vision + agent.body.radius):
                agent.fustrum.list_voisins.append(agent)


def computeDecision():




def applyDecision():

    for agent in self.list_agents:
        self.computePerception()
        self.computeDecision()



core.main(setup, run)