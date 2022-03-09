import Case
import Etat
import Noeud
import math

class Probleme:

    def __init__(self,etatInitial):
        self.etatInitial = etatInitial

    def fonctionDeSuccession(etat):
        return etat.getEmplacementsPoussieres()

    def testDuBut(noeud):
        if (len(noeud.getEtat().getEmplacementsPoussieres()) == 0):
            return True
        else:
            return False

    def calculDuCout(etatDebut, etatFin):
        cout = math.sqrt(pow((etatDebut.getRobotCase().getPosX() - etatFin.getRobotCase().getPosX()),2) + pow((etatDebut.getRobotCase().getPosY() - etatFin.getRobotCase().getPosY()),2))
        return cout

    def getEtatInitial(self):
        return self.etatInitial

    def setEtatInitial(self, etatInitial):
        self.etatInitial = etatInitial
