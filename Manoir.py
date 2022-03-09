import Aspirobot
import random
import time

class Manoir:

    def __init__(self, hauteur, largeur):
        self.hauteur = hauteur
        self.largeur = largeur
        self.manoir = [['0' for _ in range(hauteur)] for _ in range(largeur)]
        self.dirtyPos = [['0' for _ in range(hauteur)] for _ in range(largeur)]
        self.jewelPos = [['0' for _ in range(hauteur)] for _ in range(largeur)]
        self.robotPos = [['0' for _ in range(hauteur)] for _ in range(largeur)]
        self.dirtys_number = 0
        self.jewels_number = 0
        self.running = True


    def getDirtysNumber(self):
        return self.dirtys_number
    def getDirtysNumber(self):
        return self.jewels_number
    def getDirtyPos(self):
        return self.dirtyPos
    def getJewelPos(self):
        return self.jewelPos
    def getHauteur(self):
        return self.hauteur
    def getLargeur(self):
        return self.largeur

    def setDirtysNumber(self, dirtys_number):
        self.dirtys_number = dirtys_number
    def setJewelsNumber(self, jewels_number):
        self.jewels_number = jewels_number
    def setDirtyPos(self, dirtyPos):
        self.dirtyPos = dirtyPos
    def setJewelPos(self, jewelPos):
        self.jewelPos = jewelPos

    def aspirerPoussierre(self, case):
        x = case.getPosX()
        y = case.getPosY()
        self.DirtyPos[x][y] = 0

    def ramasserBijou(self, case):
        x = case.getPosX()
        y = case.getPosY()
        self.jewelPos[x][y] = 0



    def generateDirt(self):
        new_dirt_placed = False
        while (not new_dirt_placed):
            random_posX = random.randint(0, len(self.dirtyPos)-1)
            random_posY = random.randint(0, len(self.dirtyPos)-1)
            if (self.dirtyPos[random_posX][random_posY] == '0'):
                self.dirtyPos[random_posX][random_posY] = 'P'
                new_dirt_placed = True
                print("New Dirt")

    def generateJewel(self):
        new_jewel_placed = False
        while (not new_jewel_placed):
            random_posX = random.randint(0, len(self.jewelPos)-1)
            random_posY = random.randint(0, len(self.jewelPos)-1)
            if (self.jewelPos[random_posX][random_posY] == '0'):
                self.jewelPos[random_posX][random_posY] = 'B'
                new_jewel_placed = True
                print("New Jewel")

    def shouldThereBeANewDirtySpace(self):
        if (self.dirtys_number < 25):
            random_dirty_test = random.randint(0, 4)
            if (random_dirty_test == 0):
                return True
        return False

    def shouldThereBeANewLostJewel(self):
        if (self.jewels_number < 25):
            random_jewel_test = random.randint(0, 4)
            if (random_jewel_test == 0):
                return True
        return False


    def draw(self):
        for i in range(len(self.dirtyPos)):
            for j in range(len(self.dirtyPos)):
                print("[", self.dirtyPos[i][j], "-", self.jewelPos[i][j], "-", self.robotPos[i][j], "]", end=" ")
            print("\n")
        print("##############################")
        print("##############################")

    def Arreter(self):
        self.running = False

    def InsererRobot( self, case):
        x = case.getPosX()
        y = case.getPosY()
        self.robotPos[x][y] = 'R';

    def ModifierPositionRobot(self, case):
        x2 = case.getPosX()
        y2 = case.getPosY()
        for i in range(self.hauteur):
            for j in range(self.largeur):
                if(self.robotPos[i][j] == 'R'):
                    self.robotPos[i][j] = '0'

        self.robotPos[x2][y2] = 'R'


    def run(self):
        changement = False
        if (self.shouldThereBeANewDirtySpace()):
            self.generateDirt()
            self.dirtys_number += 1
            changement = True
        if (self.shouldThereBeANewLostJewel()):
            self.generateJewel()
            self.jewels_number += 1
            changement = True
        if (not changement):
            print("Nothing Appeared")
        self.draw()
        time.sleep(2)

    def initialisation(self):
        if (self.shouldThereBeANewDirtySpace()):
            self.generateDirt()
            self.dirtys_number += 1
        if (self.shouldThereBeANewLostJewel()):
            self.generateJewel()
            self.jewels_number += 1
