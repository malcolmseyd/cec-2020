import numpy as np

class Drone:
    def __init__(self, n, image):
        self.x = 0
        self.y = 0
        self.z = self.movetop(image)
        self.max = n
        self.storageHopper = {}
        self.inStorage = 0
        self.solved = False
        self.needs = []
        self.notNeeds = []
        self.cubes = []
        self.curr_image = image
        self.hopperMax = np.floor(np.sqrt(n * n * n) / 2)
        self.lastTouchedBlock = None
        for i in range(0, n):
            self.needs.append([])
            self.notNeeds.append([])
            self.cubes.append([])
            for j in range(0, n):
                self.cubes[i].append([])
                self.needs[i].append([])
                self.notNeeds[i].append([])

    def moveright(self):
        self.x = self.x + 1
        self.z = self.movetop(self.curr_image)
        return 1
    def moveleft(self, image):
        self.x = self.x - 1
        self.z = self.movetop(self.curr_image)
        return 1
    def moveup(self, image):
        self.y = self.y + 1
        self.z = self.movetop(self.curr_image)
        return 1
    def movedown(self, image):
        self.y = self.y - 1
        self.z = self.movetop(self.curr_image)
        return 1
    def movetop(self, image):
        newZ = self.max - 1
        while(image[self.x][self.y][newZ] == -1):
            newZ = newZ - 1
        return newZ

    def pickup(self, color):
        # remove picked up block from the current image
        self.curr_image[self.x][self.y][self.z] = -1

        if color in self.storageHopper:
            count = self.storageHopper.get(color)
            count = count + 1
            self.storageHopper[color] = count
        else:
            self.storageHopper[color] = 1

        self.z = self.z - 1
        self.inStorage = self.inStorage + 1
        if color == self.lastTouchedBlock:
            self.lastTouchedBlock = color;
            return 2
        else:
            self.lastTouchedBlock = color;
            return 3
    def dropoff(self, color):
        # add dropped off block to the current image
        self.z = self.z + 1
        self.curr_image[self.x][self.y][self.z] = color

        count = self.storageHopper.get(color)
        count = count - 1
        self.storageHopper[color] = count
        
        self.inStorage = self.inStorage - 1
        if color == self.lastTouchedBlock:
            self.lastTouchedBlock = color
            return 2
        else:
            self.lastTouchedBlock = color
            return 3
    def scan(self):
        #using self x, y, z
        return curr_image[self.x][self.y][self.z]








