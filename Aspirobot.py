import Capteur
import Manoir
import Etat
import Effecteur
import time
import Case
import Noeud
import Probleme


class Aspirobot:

    def __init__(self, manoir : Manoir, case):
        self.case = case
        self.uniteElectrique = 0
        self.capteur = Capteur.Capteur(manoir)
        self.etat = Etat.Etat(case, manoir.getDirtysNumber())
        self.running = True
        self.effecteur = Effecteur.Effecteur(self.capteur)

    def getCase(self):
        return self.case
    def getCapteur(self):
        return self.capteur
    def setCase(self, case):
        self.case = case

    def moveLEFT(self):
        self.case.setPosY(self.case.getPosY() - 1)
        self.uniteElectrique+= 1
    def moveRIGHT(self):
        self.case.setPosY(self.case.getPosY() + 1)
        self.uniteElectrique += 1
    def moveUP(self):
        self.case.setPosX(self.case.getPosX() - 1)
        print(self.case.getPosX())
        print(self.case.getPosY())
        self.uniteElectrique += 1
    def moveDOWN(self):
        self.case.setPosX(self.case.getPosX() + 1)
        self.uniteElectrique += 1


    def deplacement(self, direction):
        if (self.deplacement == "HAUT"):
            self.case.setPosX(self.case.getPosX() - 1)
            self.uniteElectrique += 1
        if (self.deplacement == "BAS"):
            self.case.setPosX(self.case.getPosX() + 1)
            self.uniteElectrique += 1
        if (self.deplacement == "GAUCHE"):
            self.case.setPosY(self.case.getPosY() - 1)
            self.uniteElectrique+= 1
        if (self.deplacement == "DROITE"):
            self.case.setPosY(self.case.getPosY() + 1)
            self.uniteElectrique += 1
        if (self.deplacement == "ASPIRER"):
            self.capteur.getManoir().aspirerPoussierre(self.case)
        if (self.deplacement == "RAMASSER"):
            self.capteur.getManoir().ramasserBijou(self.case)
        self.uniteElectrique += 1

    def calculDeplacements(caseDepart, caseArrivee):
        listeDesDeplacements = []
        departX = caseDepart.getPosX()
        arriveeX = caseArrivee.getPosX()
        if (departX < arriveeX):
            while (departX != arriveeX):
                listeDesDeplacements.append("BAS")
                departX +=1
        else:
            while (departX != arriveeX):
                listeDesDeplacements.append("HAUT")
                departX -=1
        departY = caseDepart.getPosY()
        arriveeY = caseArrivee.getPosY()
        if(departY < arriveeY):
            while(departY != arriveeY):
                listeDesDeplacements.append("DROITE")
                departY += 1
        else:
            while(departY != arriveeY):
                listeDesDeplacements.append("GAUCHE")
                departY -= 1
        listeDesDeplacements.append("ASPIRER")
        return listeDesDeplacements

    def noeudToAction(self, solution):
        listeDesDeplacements = []
        listeDesChemins = []
        listeDesChemins.append(solution)
        while(solution.getNoeudParent() != None):
            listeDesChemins.append(solution.getNoeudParent())
            solution = solution.getNoeudParent()
        while(len(listeDesChemins) != 1):
            listeDesDeplacements.append(self.calculDeplacements(listeDesChemins[0], listeDesChemins[len(listeDesChemins)]))
        return listeDesDeplacements




#    def heuristique(probleme, noeudSuccesseur, listeEtat, dejaVisite):
 #       somme = 0
  #      thisdic
   #     indexMin = 0
    #    while(indexMin != -1):
     #       noeudsEnfants = results(noeudSuccesseur, probleme)
      #      tailleEnfants = len(noeudsEnfants)
       #     indexMin = -1
       #     distanceMin = 9999999.9
       #     for i in range(tailleEnfants):
       #         if(dejaVisiteHeuristique.get(noeudsEnfants.get(i).getEtat())):
#                    if (noeudsEnfants.get(i).getCout() < distanceMin):
#                        indexMin = i
#                        distanceMin = noeudsEnfants.get(i).getCout()
#            if(indexMin != -1):
#                dejaVisiteHeuristique.append(noeudSuccesseur.getEtat(), noeudSuccesseur)
#                noeudSuccesseur = noeudsEnfants.get(indexMin)
#                somme += distanceMin
#        return somme




    def results(self, noeudParent, probleme):
        listeDesActionsPossibles = Probleme.fonctionDeSuccession(noeudParent.getEtat())
        nombreActions = len(listeDesActionsPossibles)
        for i in range(nombreActions):
            listeDesActionsPossiblesSuccesseur = listeDesActionsPossibles
            perceptSuccesseur = listeDesActionsPossibles
            listeDesActionsPossiblesSuccesseur.append(noeudParent.getPositionCase())
            listeDesActionsPossiblesSuccesseur.pop(listeDesActionsPossibles.index())
            etatSuccesseur = Etat.Etat(listeDesActionsPossibles.index(), perceptSuccesseur)
            cout = Probleme.calculDuCout(noeudParent.getEtat(), etatSuccesseur)
            noeudEnfant = Noeud.Noeud(etatSuccesseur, listeDesActionsPossibles.index(), noeudParent, [], cout, noeudParent.getProfondeur() + 1)
            noeudParent.ajouterEnfants(noeudEnfant)
        return noeudParent.getNoeudsEnfants()

    def uniform_cost_search(self, probleme):
        frontiere = []
        dejaVisite = []
        racine = Noeud.Noeud(probleme.getEtat(), [])
        frontiere.append(racine)
        dejaVisite.append(racine.getEtat(), racine)
        if (Probleme.testDuBut(racine) == True):
            return racine
        while(len(frontiere) > 0):
            NoeudParent = frontiere[0]
            frontiere.pop(0)
            noeudsSuccesseurs = self.results(NoeudParent, probleme)
            tailleSuccesseurs = len(noeudsSuccesseurs)
            coutMinimum = 9999999.9
            indexMinimum = -1
            for i in range(tailleSuccesseurs):
                if(noeudsSuccesseurs.get(i).getCout() < coutMinimum and dejaVisite.get(noeudsSuccesseurs.get(i).getEtat()) == None):
                    coutMinimum = noeudsSuccesseurs.get(i).getCout()
                    indexMinimum = i

            noeudEnfant = noeudsSuccesseurs.get(indexMinimum)
            dejaVisite.append(noeudEnfant.getEtat(), noeudEnfant())
            frontiere.append(noeudEnfant)
            if (Probleme.testDuBut() == True):
                return noeudEnfant
        return None


#    def aStar(self, probleme):
#        frontiere = []
#        dejaVisite = []
#        racine = Noeud.Noeud(probleme.getEtat(), [])
#        frontiere.append(racine)
#        dejaVisite.append(racine.getEtat(), racine)
#        if (Probleme.testDuBut(racine) == True):
#            return racine
#        while (len(frontiere) > 0):
#            noeudParent = frontiere[0]
#            frontiere.pop(0)
#            noeudsSuccesseurs = self.results(noeudParent, probleme)
#            tailleSuccesseurs = len(noeudsSuccesseurs)
#            coutMinimum = 9999999.9
#            indexNotable = -1
#            for i in range(tailleSuccesseurs):
#                if(noeudsSuccesseurs.get(i).getCout() + heuristique(probleme, noeudsSuccesseurs.get(i), dejaVisite) < coutMinimum and dejaVisite.get(noeudsSuccesseurs.get(i).getEtat()) == null):
#                    coutMinimum = noeudsSuccesseurs.get(i).getCout() + heuristique(probleme, noeudsSuccesseurs.get(i), dejaVisite)
#                    indexNotable = i
#            noeudEnfant = noeudsSuccesseurs.get(indexNotable)
#            dejaVisite.append(noeudEnfant.getEtat(), noeudEnfant)
#            frontiere.append(noeudEnfant)
#            if (Probleme.testDuBut(noeudEnfant) == True):
#                return noeudEnfant
#        return None



    def majEtat(self, percept):
        newEtat = Etat.Etat(self.case, percept)
        return newEtat

    def simple_problem_solving_agent(self, percept):
        listeDesActions = []
        etat = self.majEtat(percept)
        if (len(listeDesActions) == 0):
            probleme = Probleme.Probleme(etat)
            listeDesActions = self.noeudToAction(self.uniform_cost_search(probleme))
        return listeDesActions


    def draw(self):
        print("Robot en position : ", self.case.getPosX(), " - ", self.case.getPosY())
        print("Depense en electricite : ", self.uniteElectrique)
        print("Nombre de poussieres rammassees : ")
        print("Nombre de poussieres restantes")


    def run(self, nombreEpisode):
        self.capteur.dirtys()
        print("Nombre de poussieres dans le manoir : ", len(self.getCapteur().getDirtys()))
        listeDesActions = simple_problem_solving_agent(self.capteur.getDirtys())
        while (len(listeDesActions) > 0):
            mouvement(listeDesActions[0])
            if (listeDesActions[0] == "ASPIRER"):
                self.capteur.getDirtys().pop(self.case)
            listeDesActions.pop(0)
        print("Premier run")

       # while (self.running):
       #      time.sleep(2)
       # print("apprentissage par episode")
       #      for i in range(nombreEpisode):
       #          print("Episode ", i)
       #          self.resultats[i][0] = self.affichage(25)
       #          self.resultats[i][1] = self.affichage(50)
       #          self.resultats[i][2] = affichage(75)
       #          self.resultats[i][3] = affichage(100)
       #      for i in range(4):
       #          somme = 0
       #          for j in range(nombreEpisode):
       #              somme += resultats[j][i]
       #          moyennes[i] = somme / nombreEpisode
       #      indiceMax = -1
       #      for i in range(4):
       #          if (moyennes[i] > indiceMax):
       #              indiceMax = i
       #      while (running):
       #          parametre = (indiceMax+1)*25
       #          affichage(parametre)


#     def entrainement(maxActions):
#         cpt = 0
#         uniteElectrique = 0
#         while (uniteElectrique < maxActions):
#             self.capteur.dirtys()
#             listeDesActions = simple_problem_solving_agent(self.capteur.getDirtys())
#             while (len(listeDesActions) > 0):
#                 mouvement(listeDesActions[0])
#                 if (listeDesActions[0] == "ASPIRER"):
#                     self.capteur.getDirtys().pop(0)
#                     cpt += 1
#                 listeDesActions.pop(0)
#         return cpt

#    def affichage(p):
#            perf = entrainement(p)
#            ratio = perf / sel.uniteElectrique
#            print("Nombre de poussieres dans le manoir :", len(self.capteur.getDirtys()))
#            print("Consommation electrique : ", self.uniteElectrique)
#            print("Nombre de poussieres deja rammassees :", perf)
#            print("Ratio poussiere / consommation electrique : " , ratio)
#            return perf
