import Case

class Etat:
    def __init__(self, robotCase, emplacementsPoussieres):
        self.robotCase = robotCase
        self.emplacementsPoussieres = emplacementsPoussieres

    def getRobotCase(self):
        return self.robotCase

    def setRobotCase(self, newRobotCase):
        self.robotCase = newRobotCase

    def getEmplacementsPoussieres(self):
        return self.emplacementsPoussieres

    def setEmplacementsPoussieres(self, newEmplacementsPoussieres):
        self.emplacementsPoussieres = newEmplacementsPoussieres
