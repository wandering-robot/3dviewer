from point import Point, Edge, Face

from math import pi,sin,cos,sqrt

class Obj:
    def __init__(self,name,size,center=(0,0,0)):
        self.points = {}
        self.points_list = []   #litterally just to be able to start iterating through points
        self.edges = []
        self.faces = []

        self.center = center
        self.shape_name = name.lower()
        self.size = size
        self.colour = (255,0,0)

        self.check_shape()
    
    def __repr__(self):
        return self.shape_name

    def check_shape(self):
        if self.shape_name == 'cube':
            self.create_cube_points()
            self.create_cube_edges()
            self.create_cube_faces()

    def add_point(self,tup):
        point = Point(*tup)
        self.points[tup] = point
        self.points_list.append(point)

    def add_edge(self,p1,p2):
        self.edges.append(Edge(p1,p2))

    def add_face(self,face_center,point_list):
        self.faces.append(Face(face_center,point_list))

    def create_cube_points(self):
        for i in [self.center[0]-self.size, self.center[0]+self.size]:
            for j in [self.center[1]-self.size, self.center[1]+self.size]:
                for k in [self.center[2]-self.size, self.center[2]+self.size]:
                    self.add_point((i,j,k))
        self.generate_neighbours()

    def generate_neighbours(self):
        for point in self.points.values():
            for dim in range(3):                #hardcoded bc only drawing in 3d
                if point.tup[dim] == self.center[dim] - self.size:
                    new_coord = point.tup[:dim] + (self.center[dim] + self.size,) + point.tup[dim+1:]
                elif point.tup[dim] == self.center[dim] + self.size:
                    new_coord = point.tup[:dim] + (self.center[dim] - self.size,) + point.tup[dim+1:]
                point.add_neighbour(self.points[new_coord])

    def create_cube_edges(self):
        points2go = list(self.points.values())
        start = points2go[0]
        self._edge_rec(start)

    def _edge_rec(self,point):
        while point.edge2build:
            neighbour = point.edge2build[0]
            self.add_edge(point,neighbour)
            neighbour.edge2build.remove(point)
            point.edge2build.remove(neighbour)
            self._edge_rec(neighbour)

    def create_cube_faces(self):
        for dim in range(3):                                       #dealing with the dim axis
            for pos_neg in [-1,1]:                                  #dealing with the pos_neg side of the dim axis
                face_center = [0,0,0]
                face_center[dim] = self.center[dim] + pos_neg*self.size
                theta = pi/4
                r = self.size*sqrt(2)
                face_points = []
                for _ in range(5):
                    vals = (r*cos(theta), r*sin(theta))
                    coord = face_center.copy()
                    j = 0
                    for i in range(3):
                        if i == dim:
                            continue
                        else:
                            coord[i] = round(vals[j]+self.center[i])
                            j += 1
                    point = self.points[tuple(coord)]
                    face_points.append(point)
                    theta += pi/2
                self.add_face(face_center,face_points)
                    

                    

                 

                




if __name__ == "__main__":
    tup1 = (1,2,3)
    tup2 = tup1[:2]+(4,)
    print(tup2)

