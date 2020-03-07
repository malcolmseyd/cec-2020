import numpy as np

class Drone:
    def __init__(self, n):
        self.x = 0
        self.y = 0
        self.z = 0
        self.max = n
        self.storageHopper = {}
        self.solved = False
        self.needs = []
        self.notNeeds = []
        self.cubes = []
        self.hopperMax = np.floor(np.sqrt(n * n * n) / 2)
        self.lastTouchedBlock = None
        for i in range(0, n):
            self.needs.append([])
            self.notNeeds.append([])
            self.cubes.append([])
            for j in range(0, n):
                self.cubes[i].append([])
                self.needs.append([])
                self.notNeeds.append([])

    def moveright(self, image):
        self.x = self.x + 1
        self.movetop(image)
        return 1
    def moveleft(self, image):
        self.x = self.x - 1
        self.movetop(image)
        return 1
    def moveup(self, image):
        self.y = self.y + 1
        self.movetop(image)
        return 1
    def movedown(self, image):
        self.y = self.y - 1
        self.movetop(image)
        return 1
    def movetop(self, image):
        newZ = self.max - 1
        while(image[self.x][self.y][newZ] == None):
            newZ = newZ - 1
        self.z = newZ

    def pickup(self, color):
        if color in self.storageHopper:
            count = self.storageHopper.get(color)
            count = count + 1
            self.storageHopper[color] = count
        else:
            self.storageHopper[color] = 1

        self.z = self.z - 1
        if color == self.lastTouchedBlock:
            self.lastTouchedBlock = color;
            return 2
        else:
            self.lastTouchedBlock = color;
            return 3
    def dropoff(self, color):
        count = self.storageHopper.get(color)
        count = count - 1
        self.storageHopper[color] = count
        self.z = self.z + 1
        if color == self.lastTouchedBlock:
            self.lastTouchedBlock = color
            return 2
        else:
            self.lastTouchedBlock = color
            return 3
    def scan(self, image):
        #using self x, y, z
        return image[self.x][self.y][self.z]







