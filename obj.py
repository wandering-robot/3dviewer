from point import Point, Edge

class Obj:
    def __init__(self,name,size,center=(0,0,0)):
        self.points = {}
        self.edges = []

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

    def add_point(self,tup):
        self.points[tup] = Point(*tup)

    def add_edge(self,p1,p2):
        self.edges.append(Edge(p1,p2))

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
        # if point.edge_num == len(point.neighbours):
        #     return True
        # else:
        while point.edge2build:
            neighbour = point.edge2build[0]
            self.add_edge(point,neighbour)
            # point.edge_num += 1
            # neighbour.edge_num += 1
            neighbour.edge2build.remove(point)
            point.edge2build.remove(neighbour)
            self._edge_rec(neighbour)






if __name__ == "__main__":
    tup1 = (1,2,3)
    tup2 = tup1[:2]+(4,)
    print(tup2)

