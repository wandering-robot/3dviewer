
class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def dot(self,other):
        return self.i*other.i + self.j*other.j + self.k*other.k