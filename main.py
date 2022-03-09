import functions
import Aspirobot
import time
import os
import Manoir
import Capteur
import Etat
import threading
import Case
from threading import Thread

manor_size = 5
gameIsRunning = True

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

manoir = Manoir.Manoir(manor_size, manor_size)
caseRobot = Case.Case(1, 1)
agent = Aspirobot.Aspirobot(manoir, caseRobot)
manoir.draw()

"""
while (gameIsRunning):
    clearConsole()
    if (functions.shouldThereBeANewDirtySpace(dirtys_number)):
        functions.generateDirt(manor_dirty)
        dirtys_number += 1
    if (functions.shouldThereBeANewLostJewel(jewels_number)):
        functions.generateJewel(manor_jewel)
        jewels_number += 1
    functions.drawManor(manor_dirty, manor_jewel)
    time.sleep(pause_length)
"""

for init in range(10):
    manoir.initialisation()
    init += 1

def runAgent():
    while True:
        agent.run(3)

def runManoir():
    while True:
        #clearConsole()
        manoir.ModifierPositionRobot(agent.getCase())
        manoir.run()

if __name__ == "__main__":
    t1 = Thread(target = runAgent)
    t2 = Thread(target = runManoir)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    while True:
        pass
