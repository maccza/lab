"""
Częśćć 1 (1 pkt): Uzupełnij klasę Vector tak by reprezentowała wielowymiarowy wektor.
Klasa posiada przeładowane operatory równości, dodawania, odejmowania,
mnożenia (przez liczbę i skalarnego), długości
oraz nieedytowalny (własność) wymiar.
Wszystkie operacje sprawdzają wymiar.
Część 2 (1 pkt): Klasa ma statyczną metodę wylicznia wektora z dwóch punktów
oraz metodę fabryki korzystającą z metody statycznej tworzącej nowy wektor
z dwóch punktów.
Wszystkie metody sprawdzają wymiar.
"""
import math
import sys
class Vector:
    dim = None  # Wymiar vectora
    def __init__(self, *args):
        dim = len(args)
        
        self.var = (args)
        
    @property
    def len(self):
        temp = 0
        for val in self.var:
            temp += val**2
            
        temp = math.sqrt(temp)
        return temp
    @property
    def dim(self):
        return len(self.var)
    def __eq__(self,vector):
        if self.var == vector.var:
            return True
        else:
            return False         
    def __add__(self,vector):
        
        temp = []
        if len(self.var) == len(vector.var):
            for i in range(len(self.var)):
                temp.append(self.var[i]+vector.var[i])
        
        return Vector(*temp)       
    def __sub__(self,vector):
        
        temp = []
        if len(self.var) == len(vector.var):
            for i in range(len(self.var)):
                temp.append(self.var[i]-vector.var[i])
        
        return Vector(*temp)       
    def __mul__(self,other):
        temp = []
        if type(other) is int:
            for i in range(len(self.var)):
                temp.append(self.var[i]*2)
            return Vector(*temp)
        elif type(other) is Vector:
            for i in range(len(self.var)):
                temp.append(self.var[i]*other.var[i])
            
            return int(sum(temp))
    def __len__(self):
        return len(self.var)
    @staticmethod
    def calculate_vector(beg, end):
        """
        Calculate vector from given points

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: Calculated vector
        :rtype: tuple
        """
        temp = []
        if len(beg) == len(end):
            for i in range(len(beg)):
                temp.append(end[i] - beg[i])
        
        vec = tuple(temp)

        return vec
   

    @classmethod
    def from_points(cls, beg, end):
        """"""
        """
        Generate vector from given points.

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: New vector
        :rtype: tupler
        """
        
        vec = Vector.calculate_vector(beg,end)
        
        return cls(*vec)


if __name__ == '__main__':
    v1 = Vector(1,2,3)
    v2 = Vector(1,2,3)
    assert v1 + v2 == Vector(2,4,6)
    assert v1 - v2 == Vector(0,0,0)
    assert v1 * 2 == Vector(2,4,6)
    assert v1 * v2 == 14
    assert len(Vector(3,4)) == 2
    assert Vector(3,4).dim == 2
    assert Vector(3,4).len == 5.    
    assert Vector.calculate_vector([0, 0, 0], [1,2,3]) == (1,2,3)
    assert Vector.from_points([0, 0, 0], [1,2,3]) == Vector(1,2,3)
