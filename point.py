from math import sqrt

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

        self.tup = (x,y,z)

        #pixel coordinates to be updated by the space.update a b function
        self.a = None
        self.b = None
        self.pixel = None

        #neighbouring points in the shape for edge drawing
        self.neighbours = []
        self.edge2build = []        #list to be emptied as edges are created
        self.edge_num = 0

    def __repr__(self):
        return f'(x:{self.x:.2f} y:{self.y:.2f} z:{self.z:.2f})\t(a:{self.a:.2f} b:{self.b:.2f})'

    def dist(self,other):
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z - other.z)**2)

    def add_neighbour(self,point):
        self.neighbours.append(point)
        self.edge2build.append(point)

class Edge:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        
        self.xyz1 = (self.p1.x, self.p1.y, self.p1.z)
        self.xyz2 = (self.p2.x, self.p2.y, self.p2.z)

        self.ab1 = None
        self.ab2 = None

    def __repr__(self):
        return f'L:{self.ab1}->{self.ab2}'

    def update_ab(self):
        self.ab1 = (int(self.p1.a), int(self.p1.b))
        self.ab2 = (int(self.p2.a), int(self.p2.b))