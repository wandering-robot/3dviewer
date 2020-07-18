from point import Point

class Obj:
    def __init__(self,name,size):
        self.points = []
        self.shape_name = name.lower()
        self.size = size
        self.colour = (255,0,0)

        self.check_shape()
    
    def __repr__(self):
        return self.shape_name

    def check_shape(self):
        if self.shape_name == 'cube':
            self.create_cube()

    def add_point(self,tup):
        self.points.append(Point(*tup))

    def create_cube(self):
        for i in [-self.size,self.size]:
            for j in [-self.size,self.size]:
                for k in [-self.size,self.size]:
                    self.points.append(Point(i,j,k))

            


if __name__ == "__main__":
    cube = Obj()
    cube.create_cube(1)
    print(cube.points)

