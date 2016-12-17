import numpy as np


def point_in_triangle(point, triangle):
    sign = lambda p1, p2, p3: (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    b1 = sign(point, triangle.v1, triangle.v2) < 0.0
    b2 = sign(point, triangle.v2, triangle.v3) < 0.0
    b3 = sign(point, triangle.v3, triangle.v1) < 0.0

    return (b1 == b2) and (b2 == b3)


def baricentric_coordinates(point, triangle):
    v0 = triangle.v2 - triangle.v1
    v1 = triangle.v3 - triangle.v1
    v2 = point - triangle.v1


    d00 = np.dot(v0, v0)
    d01 = np.dot(v0, v1)
    d11 = np.dot(v1, v1)
    d20 = np.dot(v2, v0)
    d21 = np.dot(v2, v1)

    denom = float(d00 * d11 - d01 * d01)

    alfa = (d11 * d20 - d01 * d21) / denom
    beta = (d00 * d21 - d01 * d20) / denom
    gama = max(0, 1.0 - alfa - beta)

    return alfa, beta, gama



class Triangle(object):
    """docstring for Triangle"""
    
    def __init__(self, v1, v2, v3, ind1=None, ind2=None, ind3=None, norm=None):
        super(Triangle, self).__init__()
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

        self.ind1 = ind1
        self.ind2 = ind2
        self.ind3 = ind3

        self.norm = norm

        sorted_by_x = sorted([self.v1, self.v2, self.v3], key=lambda v: v[0])
        sorted_by_y = sorted([self.v1, self.v2, self.v3], key=lambda v: v[1])
        self.min_x, self.max_x = sorted_by_x[0], sorted_by_x[-1]
        self.min_y, self.max_y = sorted_by_y[0], sorted_by_y[-1]



class TriangleWithRef(object):
    """docstring for Triangle
        v1, v2, v3 are in screen_coordinates
        ref is saved if needed to access the position.
    """
    
    def __init__(self, v1, v1_ref, v2, v2_ref, v3, v3_ref):
        super(TriangleWithRef, self).__init__()
        self.v1 = v1
        self.v1_ref = v1_ref
        self.v2 = v2
        self.v2_ref = v2_ref
        self.v3 = v3
        self.v3_ref = v3_ref

    def sort_asc_x(self):
        if (self.v1[0] > self.v2[0]):
            vTmp = self.v1
            vTmp_ref = self.v1_ref
            self.v1 = self.v2
            self.v1_ref = self.v2_ref
            self.v2 = vTmp
            self.v2_ref = vTmp_ref

        if (self.v1[0] > self.v3[0]):
            vTmp = self.v1
            vTmp_ref = self.v1_ref
            self.v1 = self.v3
            self.v1_ref = self.v3_ref
            self.v3 = vTmp
            self.v3_ref = vTmp_ref

        if (self.v2[0] > self.v3[0]):
            vTmp = self.v2
            vTmp_ref = self.v2_ref
            self.v2 = self.v3
            self.v2_ref = self.v3_ref
            self.v3 = vTmp
            self.v3_ref = vTmp_ref

    def sort_asc_y(self):
        if (self.v1[1] > self.v2[1]):
            vTmp = self.v1
            vTmp_ref = self.v1_ref
            self.v1 = self.v2
            self.v1_ref = self.v2_ref
            self.v2 = vTmp
            self.v2_ref = vTmp_ref

        if (self.v1[1] > self.v3[1]):
            vTmp = self.v1
            vTmp_ref = self.v1_ref
            self.v1 = self.v3
            self.v1_ref = self.v3_ref
            self.v3 = vTmp
            self.v3_ref = vTmp_ref
        if (self.v2[1] > self.v3[1]):
            vTmp = self.v2
            vTmp_ref = self.v2_ref
            self.v2 = self.v3
            self.v2_ref = self.v3_ref
            self.v3 = vTmp
            self.v3_ref = vTmp_ref

class PointP4(object):
    """docstring for Triangle"""
    
    def __init__(self, v4, v4_ref):
        super(PointP4, self).__init__()
        self.v4 = v4
        self.v4_ref = v4_ref
