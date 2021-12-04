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
        return 2*(self.length*self.width + self.length*self.height + self.width*self.height)

    def getPoints(self):
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
        orientationList = [Box(self.length, self.width, self.height, self.x, self.y, self.z),
                           Box(self.length, self.height, self.width, self.x, self.y, self.z),
                           Box(self.width, self.length, self.height, self.x, self.y, self.z),
                           Box(self.width, self.height, self.length, self.x, self.y, self.z),
                           Box(self.height, self.length, self.width, self.x, self.y, self.z),
                           Box(self.height, self.width, self.length, self.x, self.y, self.z),]
        return orientationList

    def boxToPoint(self, setx, sety, setz):
        self.x = setx
        self.y = sety
        self.z = setz

    def clone(self):
        return Box(self.length, self.width, self.height, self.x, self.y, self.z)


class Stack:
    def __init__(self):
        self.boxes = []

    def addBox(self, box):
        self.boxes.append(box)

    def getCorners(self):
        corners = []
        for e in self.boxes:
            p = e.getPoints()
            corners += p
        return corners

    def getPackage(self):
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
        if a2 > b1 and a1 < b2:
            return True
        if a2 < b1 and a1 > b2:
            return True

        return False

    def collide(self, b1, b2):
        xc = self.axisCollide(b1.x, b1.x + b1.length, b2.x, b2.x + b2.length)
        yc = self.axisCollide(b1.y, b1.y + b1.height, b2.y, b2.y + b2.height)
        zc = self.axisCollide(b1.z, b1.z + b1.width, b2.z, b2.z + b2.width)
        if xc and yc and zc:
            return True
        return False

    def removeBox(self):
        self.boxes.pop()

    def clone(self):
        s = Stack()
        for e in self.boxes:
            s.addBox(e.clone())
        return s

    def checkCollide(self, box):
        for b in self.boxes:
            if self.collide(b, box):
                return True
        return False


def getBestBox(stack, items, n):
    if n == len(items):
        return (stack.getPackage().surfaceArea(), stack)

    minSArea = sys.maxsize
    minStack = Stack()
    cItem = items[n]
    o = cItem.getOrientations()
    for l in o:
        bCorners = l.getPoints()
        sCorners = stack.getCorners()

        if len(sCorners) == 0:
            stack.addBox(l)
            (sArea, sk) = getBestBox(stack, items, n + 1)
            if sArea < minSArea:
                minSArea = sArea
                minStack = sk.clone()
            stack.removeBox()
        else:
            for c1 in bCorners:
                for c2 in sCorners:
                    l.boxToPoint(c2.x - c1.x, c2.y - c1.y, c2.z - c1.z)
                    if stack.checkCollide(l):
                        continue
                    stack.addBox(l)
                    (sArea, sk) = getBestBox(stack, items, n + 1)
                    if sArea < minSArea:
                        minSArea = sArea
                        minStack = sk.clone()
                    stack.removeBox()

    return (minSArea, minStack)





b = Box(3, 3, 3, 0, 0, 0)
t = Box(3, 3, 3, 0, 0, 0)
l = Box(3, 3, 3, 0, 0, 0)

s = Stack()
i = [b, t, l]
(a, b) = getBestBox(s, i, 0)
print(a)
for o in b.boxes:
    print(o)