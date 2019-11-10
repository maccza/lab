"""
Na (1 pkt.):
- Zaimplementuj klasy: Rectangle, Square, Circle dziedziczące z klasy Figure
oraz definiujące jej metody:
    - Rectangle powinien mieć dwa atrybuty odpowiadające bokom (a i b)
    - Klasa Square powinna dziedziczyć z Rectangle.
    - Circle ma posiadać tylko atrybut r (radius).
- Przekształć metody area i perimeter we własności (properties).
---------
Na (2 pkt.):
- Zwiąż ze sobą boki a i b klasy Square (tzn. modyfikacja boku a lub boku b
powinna ustawiać tę samą wartość dla drugiego atrybutu).
- Zaimplementuj metody statyczne pozwalające na obliczenie
pola (get_area) i obwodu (get_perimeter) figury
na podstawie podanych parametrów.
- Zaimplementuj classmethod "name" zwracającą nazwę klasy.
---------
Na (3 pkt.):
- Zaimplementuj klasę Diamond (romb) dziedziczącą z Figure,
po której będzie dziedziczyć Square,
tzn. Square dziediczy i z Diamond i Rectangle.
- Klasa wprowadza atrybuty przekątnych (e i f) oraz metody:
-- are_diagonals_equal: sprawdź równość przekątnych,
-- to_square: po sprawdzeniu równości przekątnych zwróci instancję
klasy Square o takich przekątnych lub None (jeżeli przekątne nie są równe).
- Zwiąż ze sobą atrybuty a, b, e i f w klasie Square.
"""

import math
class Figure:
    @property
    def area(self):
        raise NotImplementedError
    @property
    def perimeter(self):
        raise NotImplementedError

    def name(self):
        return self.__class__.__name__

    def __str__(self):
        return (
            f'{self.name()}: area={self.area:.3f}, '
            f'perimeter={self.perimeter:.3f}'
        )
    @classmethod
    def name_class(cls):
        return cls().__class__.__name__
    @staticmethod
    def get_area():
        raise NotImplementedError
    @staticmethod
    def get_perimeter():
        raise NotImplementedError

class Circle(Figure):
    def __init__(self,radius, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.radius = radius
    @classmethod
    def name_class(cls,r):
        return cls(r).name()
    @property
    def area(self):
        return math.pi*self.radius*self.radius
    @property
    def perimeter(self):
        return 2*self.radius*math.pi
    @staticmethod
    def get_area(radius):
        return math.pi*radius*radius
    @staticmethod
    def get_perimeter(radius):
        return 2*radius*math.pi
class Rectangle(Figure):
    def __init__(self,a,b, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a = a
        self.b = b
    @property
    def area(self):
        return self.a*self.b
    @property
    def perimeter(self):
        return 2*(self.a + self.b)
    @staticmethod
    def get_area(a,b):
        return a*b
    @staticmethod
    def get_perimeter(a,b):
        return 2*(a + b)
    @classmethod
    def name_class(cls,a,b):
        return cls(a,b).name()
class Diamond(Figure):
    def __init__(self,e,f, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.f = f
        self.e = e
    @property
    def area(self):
        return self.e*self.f*0.5
    @property
    def perimeter(self):
        return 4*math.sqrt(0.25*(self.e*self.e+self.f*self.f))
    def are_diagonals_equal(self):
        if self.e == self.f:
            return True
        else:
            return False
    def to_square(self):
        if self.are_diagonals_equal() == True:
            return Square(self.e/math.sqrt(2))
    @staticmethod
    def get_area(e,f):
        return e*f*0.5
    @staticmethod
    def get_perimeter(e,f):
        return 4*math.sqrt(0.25*(e*e+f*f))
    @classmethod
    def name_class(cls,e,f):
        return cls(e,f).name()
class Square(Rectangle,Diamond):
    
    def __init__(self, a):
        self.a = a
        self.b = a
        self.e = a*math.sqrt(2)
        self.f =self.e
    @property
    def area(self):
        return self.a*self.b
    @property
    def perimeter(self):
        return 2*(self.a + self.b)   
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self,value):
        
        self.__a = value
        self.__b = value
        self.__e = value*math.sqrt(2)
        self.__f = value*math.sqrt(2)
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self,value):
        
        self.__a = value
        self.__b = value
        self.__e = value*math.sqrt(2)
        self.__f = value*math.sqrt(2)
    @property
    def e(self):
        return self.__e
    @e.setter
    def e(self,value):
        
        self.__a = value/math.sqrt(2)
        self.__b = value/math.sqrt(2)
        self.__e = value
        self.__f = value
    @property
    def f(self):
        return self.__f
    @f.setter
    def f(self,value):
        
        self.__a = value/math.sqrt(2)
        self.__b = value/math.sqrt(2)
        self.__e = value
        self.__f = value
    @staticmethod
    def get_area(e,f):
        return e*f*0.5
    @staticmethod
    def get_perimeter(a):
        return 4*a
    @classmethod
    def name_class(cls,a):
        return cls(a).name()
if __name__ == '__main__':
    kolo1 = Circle(1)

    assert str(kolo1) == 'Circle: area=3.142, perimeter=6.283'
    rec_1 = Rectangle(2, 4)
   
    assert str(rec_1) == 'Rectangle: area=8.000, perimeter=12.000'

    sqr_1 = Square(4)

    assert str(sqr_1) == 'Square: area=16.000, perimeter=16.000'

    diam_1 = Diamond(6, 8)
    #print(str(diam_1))
    assert str(diam_1) == 'Diamond: area=24.000, perimeter=20.000'

    diam_2 = Diamond(1, 1)
    assert str(diam_2) == 'Diamond: area=0.500, perimeter=2.828'

    sqr_3 = diam_2.to_square()
    assert str(sqr_3) == 'Square: area=0.500, perimeter=2.828'

