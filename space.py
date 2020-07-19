from obj import Obj
from vector import Vector
from math import pi,sqrt,cos,sin

class Space:
    def __init__(self,plane_t=50):
        self.objs = []

        self.alpha = pi/4
        self.gamma = pi/4
        self.epsilon = (1 + cos(self.gamma)**2)

        self.plane_t = plane_t
        self.plane = Plane(self,plane_t)

        #for debugging purposes
        self.add_object('cube',100)

    def add_object(self,name,size):
        obj = Obj(name,size)
        self.objs.append(obj)

    def update_objects_ab(self):   #translates the points (x,y,z) into (a,b)
        for obj in self.objs:
            for point in obj.points.values():
                top = point.x*cos(self.alpha) + point.y*sin(self.alpha) + point.z*cos(self.gamma)
                t = top/(self.epsilon**(3/2) - self.epsilon)
                #point of intersection with the point's vector and the plane
                xA = point.x + t*cos(self.alpha)
                yA = point.y + t*sin(self.alpha)
                zA = point.z + t*cos(self.gamma)
                #vector from plane origin to POI
                wv = Vector(xA - self.plane.x0, yA - self.plane.y0, zA - self.plane.z0)
                #dot product wv with the plane's basis vectors to get respective a b coordinates
                point.a = wv.dot(self.plane.av)
                point.b = wv.dot(self.plane.bv)
                point.pixel = (point.a,point.b)
            #additional code to update the ab values of the lines by making the lines reevaluate their points ab values
            for edge in obj.edges:
                edge.update_ab()


class Plane:
    def __init__(self,space,t0):
        self.t0 = t0

        self.space = space

        self.update()

    def update_basis(self):
        self.bv = Vector(-cos(self.space.alpha)*cos(self.space.gamma)/self.space.epsilon, -sin(self.space.alpha)*cos(self.space.gamma)/self.space.epsilon,1/self.space.epsilon)
        self.av = Vector(-sin(self.space.alpha), cos(self.space.alpha), 0)

    def update(self):
        self.d0 = self.t0 * sqrt(1+cos(self.space.gamma)**2)

        self.x0 = self.d0 * cos(self.space.alpha)
        self.y0 = self.d0 * sin(self.space.alpha)
        self.z0 = self.d0 * cos(self.space.gamma)

        self.update_basis()

    def display(self):
        print(self.space.alpha,self.space.gamma)

if __name__ == "__main__":
    space = Space(50)
    space.plane.display()
    space.gamma = pi
    space.plane.update()
    space.plane.display()

    

