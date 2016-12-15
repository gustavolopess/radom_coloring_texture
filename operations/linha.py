class Linha(object):
    """docstring for Linha"""
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __div__(self,a):
        a = (a or 1)
        return Linha(self.a/a, self.b/a, self.c/a, self.d/a)

    def __mod__(self, a):
        return Linha(self.a - a.a * self.a,
                    self.b - a.b * self.a,
                    self.c - a.c * self.a,
                    self.d - a.d * self.a)
    def __xor__(self, a):
        return Linha(self.a,
                    self.b - a.b * self.b,
                    self.c - a.c * self.b,
                    self.d - a.d * self.b)

    def __add__(self, a):
        return Linha(self.a,
                    self.b,
                    self.c - a.c * self.c,
                    self.d - a.d * self.c)