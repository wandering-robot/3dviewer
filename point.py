
class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

        #pixel coordinates to be updated by the space.update a b function
        self.a = None
        self.b = None

    def __repr__(self):
        return f'(x:{self.x:.2f} y:{self.y:.2f} z:{self.z:.2f})\t(a:{self.a:.2f} b:{self.b:.2f})'