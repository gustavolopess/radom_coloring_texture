class Escalona(object):

    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def esc(self):
        l1 = self.l1 / self.l1.a
        l2 = self.l2 % l1
        l3 = self.l3 % l1
        l2 = l2 / l2.b
        l1 = l1^l2
        l3 = l3^l2
        l3 = l3 / l3.c
        l1 = l1 + l3
        l2 = l2 + l3

        return (l1.d, l2.d, l3.d)

