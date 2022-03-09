import Manoir
import Case

class Capteur:
    def __init__(self, manoir : Manoir):
        self.manoir = manoir
        self.dirtys = []
        self.jewels = []

    def dirtys(self):
        for i in range(self.manoir.getHauteur()) :
            for j in range(self.manoir.getLargeur()) :
                if(self.manoir.getDirtyPos()[i][j] == 'P'):
                    newDirt = Case(i, j)
                    self.dirtys.append(newDirt)

    def jewels(self):
        for i in range(self.manoir.getHauteur()) :
            for j in range(self.manoir.getLargeur()) :
                if(self.manoir.getJewelPos()[i][j] == 'B'):
                    newJewel = Case(i, j)
                    self.jewels.append(newJewel)

    def getManoir(self):
        return self.manoir
    def getDirtys(self):
        return self.dirtys
    def getJewels(self):
        return self.jewels

    def setManoir(self, manoir):
        self.manoir = manoir
    def setDirtys(self, dirtys):
        self.dirtys = dirtys
    def setJewels(self, jewels):
        self.jewels = jewels
