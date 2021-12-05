import sys

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)
    def __repr__(self):
        return str(self)


class Box:
    def __init__(self, length, width, height, x, y, z):
        self.length = length
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({}, {}, {}, {}, {}, {})".format(self.length, self.width, self.height, self.x, self.y, self.z)
    def __repr__(self):
        return str(self)

    def surfaceArea(self):
        #calculates surface area
        return 2*(self.length*self.width + self.length*self.height + self.width*self.height)

    def getPoints(self):
        #gets corners/points of a box
        pointList = [Point(self.x, self.y, self.z),
                     Point(self.x + self.length, self.y, self.z),
                     Point(self.x + self.length, self.y, self.z + self.width),
                     Point(self.x, self.y, self.z + self.width),
                     Point(self.x, self.y + self.height, self.z),
                     Point(self.x + self.length, self.y + self.height, self.z),
                     Point(self.x + self.length, self.y + self.height, self.z + self.width),
                     Point(self.x, self.y + self.height, self.z + self.width)]

        return pointList

    def getOrientations(self):
        #Gets all 6 orientations of a box
        orientationList = [Box(self.length, self.width, self.height, self.x, self.y, self.z),
                           Box(self.length, self.height, self.width, self.x, self.y, self.z),
                           Box(self.width, self.length, self.height, self.x, self.y, self.z),
                           Box(self.width, self.height, self.length, self.x, self.y, self.z),
                           Box(self.height, self.length, self.width, self.x, self.y, self.z),
                           Box(self.height, self.width, self.length, self.x, self.y, self.z),]
        return orientationList

    def boxToPoint(self, setx, sety, setz):
        #changes a box's position
        self.x = setx
        self.y = sety
        self.z = setz

    def clone(self):
        #clones box
        return Box(self.length, self.width, self.height, self.x, self.y, self.z)


class Stack:
    def __init__(self):
        self.boxes = []

    def addBox(self, box):
        #Adds box to a stack
        self.boxes.append(box)

    def getCorners(self):
        #Gets all of the points/corners of a stack
        corners = []
        for e in self.boxes:
            p = e.getPoints()
            corners += p
        return corners

    def getPackage(self):
        #Calculates a package that fits around a stack
        minX = sys.maxsize
        maxX = -sys.maxsize
        minY = sys.maxsize
        maxY = -sys.maxsize
        minZ = sys.maxsize
        maxZ = -sys.maxsize

        corners = self.getCorners()

        for e in corners:
            if e.x < minX:
                minX = e.x
            if e.x > maxX:
                maxX = e.x
            if e.y < minY:
                minY = e.y
            if e.y > maxY:
                maxY = e.y
            if e.z < minZ:
                minZ = e.z
            if e.z > maxZ:
                maxZ = e.z

        pLength = maxX - minX
        pWidth = maxZ - minZ
        pHeight = maxY - minY

        package = Box(pLength,pWidth, pHeight, minX, minY, minZ)
        return package

    def axisCollide(self, a1, a2, b1, b2):
        #Calculates if two boxes collide on an axis
        if a2 > b1 and a1 < b2:
            return True
        if a2 < b1 and a1 > b2:
            return True

        return False

    def collide(self, b1, b2):
        #Checks if two boxes are colliding
        xc = self.axisCollide(b1.x, b1.x + b1.length, b2.x, b2.x + b2.length)
        yc = self.axisCollide(b1.y, b1.y + b1.height, b2.y, b2.y + b2.height)
        zc = self.axisCollide(b1.z, b1.z + b1.width, b2.z, b2.z + b2.width)
        if xc and yc and zc:
            return True
        return False

    def removeBox(self):
        #Removes a box from the stack
        self.boxes.pop()

    def clone(self):
        #Clones stack
        s = Stack()
        for e in self.boxes:
            s.addBox(e.clone())
        return s

    def checkCollide(self, box):
        #Checks if there are any boxes colliding with others
        for b in self.boxes:
            if self.collide(b, box):
                return True
        return False


def getBestBox(stack, items, n):
    #Main function - gets the best box if given a list of items
    if n == len(items):
        #If there are no items left, return the surface area & orientations
        return (stack.getPackage().surfaceArea(), stack)

    minSArea = sys.maxsize
    minStack = Stack()
    cItem = items[n]
    o = cItem.getOrientations()
    for l in o: #for each orientation
        bCorners = l.getPoints() #box corners
        sCorners = stack.getCorners() #stack corners

        if len(sCorners) == 0: #if it is the first time
            stack.addBox(l)
            (sArea, sk) = getBestBox(stack, items, n + 1) #Calls itself
            if sArea < minSArea:
                minSArea = sArea
                minStack = sk.clone()
            stack.removeBox()
        else: #if there are already items in the stack
            #Looping through all combinations of corners
            for c1 in bCorners:
                for c2 in sCorners:
                    l.boxToPoint(c2.x - c1.x, c2.y - c1.y, c2.z - c1.z)#Moves the box to the corner
                    if stack.checkCollide(l): #Tests if the box collides with others in the stack
                        continue
                    stack.addBox(l)
                    if stack.getPackage().surfaceArea() < minSArea: #If the surface area is smaller than the last smallest surface area
                        (sArea, sk) = getBestBox(stack, items, n + 1) #Calls itself
                        if sArea < minSArea:
                            #Replaces the min surface area & best stack with better surface area & stack
                            minSArea = sArea
                            minStack = sk.clone()
                    stack.removeBox() #Removes box so it can try again

    return (minSArea, minStack) #Final return, returns the smallest surface area &  best stack





b = Box(3, 3, 3, 0, 0, 0)
t = Box(3, 3, 3, 0, 0, 0)
l = Box(3, 3, 3, 0, 0, 0)

s = Stack()
i = [b, t, l]
(a, b) = getBestBox(s, i, 0)
print(a)
for o in b.boxes:
    print(o)