class RGB(object):

    def __init__(self, r,g,b):
        self.r = r
        self.g = g
        self.b = b

    def __mul__(self, a):
        return RGB(self.r*a,self.g*a,self.b*a)

    def __mod__(self,a):
        return RGB(self.r*a.r,self.g*a.g,self.b*a.b)

    def __add__(self, cor):
        return RGB(min(self.r+cor.r,255),min(self.g+cor.g,255),min(self.b+cor.b,255))

    def __div__(self, a):
        return RGB(self.r/a,self.g/a,self.b/a)

    def __str__(self):
        return "("+str(self.r)+", "+str(self.g)+", "+str(self.b)+")"