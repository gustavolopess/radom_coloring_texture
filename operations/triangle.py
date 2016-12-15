import numpy as np

class Triangle(object):
    """docstring for Triangle"""
    
    def __init__(self, v1, v2, v3, norm="None"):
        super(Triangle, self).__init__()
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.norm = norm

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
