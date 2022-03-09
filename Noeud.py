import Etat
import Case

class Noeud:

    def __init__(self, etat, noeudsEnfants, caseAction = None, noeudParent = None, cout = None, profondeur = None):
        #Cas general
        if (caseAction and noeudParent and cout and profondeur):
            self.etat = etat
            self.positionCase = caseAction
            self.noeudParents = noeudParent
            self.noeudsEnfants = noeudsEnfants
            self.cout = cout
            self.profondeur = profondeur
        #Cas racine
        else:
            self.etat = etat
            self.positionCase = etat.getRobotCase()
            self.noeudParent = None
            self.noeudsEnfants = noeudsEnfants
            self.cout = 0
            self.profondeur = 0


    def getEtat(self):
        return self.etat
    def getNoeudParent(self):
        return self.noeudParent
    def getNoeudsEnfants(self):
        return self.noeudsEnfants
    def getCout(self):
        return self.cout
    def getProfondeur(self):
        return self.profondeur
    def getPositionCase(self):
        return self.positionCase

    def setEtat(self, etat):
        self.etat = etat
    def setNoeudParent(self, noeudParent):
        self.noeudParent = noeudParent
    def setNoeudsEnfants(self, noeudsEnfants):
        self.noeudsEnfants = noeudsEnfants
    def setCout(self, cout):
        self.cout = cout
    def setProfondeur(self, profondeur):
        self.profondeur = profondeur
    def setPositionCase(self, positionCase):
        self.positionCase = positionCase

    def ajouterEnfants(noeudsEnfants):
        self.noeudsEnfants.add(noeudsEnfants)
