import random


def generateDirt(manor_dirty):
    new_dirt_placed = False
    while (not new_dirt_placed):
        random_posX = random.randint(0, len(manor_dirty)-1)
        random_posY = random.randint(0, len(manor_dirty)-1)
        if (manor_dirty[random_posX][random_posY] == 0):
            manor_dirty[random_posX][random_posY] = 1
            new_dirt_placed = True
            print("New Dirt")
    return manor_dirty


def generateJewel(manor_jewel):
    new_jewel_placed = False
    while (not new_jewel_placed):
        random_posX = random.randint(0, len(manor_jewel)-1)
        random_posY = random.randint(0, len(manor_jewel)-1)
        if (manor_jewel[random_posX][random_posY] == 0):
            manor_jewel[random_posX][random_posY] = 1
            new_jewel_placed = True
            print("New Jewel")
    return manor_jewel


def shouldThereBeANewDirtySpace(dirtys_number):
    if (dirtys_number < 25):
        random_dirty_test = random.randint(0, 4)
        if (random_dirty_test == 0):
            return True
    return False


def shouldThereBeANewLostJewel(jewels_number):
    if (jewels_number < 25):
        random_jewel_test = random.randint(0, 4)
        if (random_jewel_test == 0):
            return True
    return False


def drawManor(manor_dirty, manor_jewel):
    for i in range(len(manor_dirty)):
        for j in range(len(manor_dirty)):
            print("[", manor_dirty[i][j], "-", manor_jewel[i][j], "]", end=" ")
        print("\n")
    print("##############################")
    print("##############################")
