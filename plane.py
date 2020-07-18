
class Plane():
    def __init__(self,space,t0):
        self.t0 = t0
        self.d0 = self.t0 * sqrt(1+cos(self.gamma)**2)

        self.x0 = self.d * cos(self.alpha)
        self.y0 = self.d * sin(self.alpha)
        self.z0 = self.d * cos(self.gamma)

    def update_greeks(self,alpha,gamma):
        self.alpha = alpha
        self.gama = gamma