import Manoir
import Capteur
import Case

class Effecteur:
    def __init__(self, capteur : Capteur):
        self.capteur = capteur

    def Asprirer(self, case):
        x = case.getPosX()
        y = case.getPosY()
        self.capteur.manoir.getDirtyPos()[x][y] = '0'
        self.capteur.manoir.getJewelPos()[x][y] = '0'
        self.capteur.dirtys.remove(case)
        self.capteur.jewels.remove(case)

    def Ramasser(self, case):
        x = case.getPosX()
        y = case.getPosY()
        self.capteur.manoir.getJewelPos()[x][y] = '0'
        self.capteur.jewels.remove(case)
