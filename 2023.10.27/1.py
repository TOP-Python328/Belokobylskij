# Я не уверен что правильно реализовал методы repr и str, но лучше ничего не придумал.

# Что-то я прям растерялся как правильно нужно документировать гетеры и сетеры. Их вообще нужно документировать!?
# И как правильно аннотировать если функция или метод выбрасывают ошибку? -> None или -> TypeError?

# "- is_closed - частный - проверяет, формируют ли отрезки замкнутый многоугольник -> float" - тут наверное ошибка? В диаграмме указано что этот метод возвращает bool. 
from math import  sqrt
from typing import Self
class Point:
    """Создаёт объект класса Point, для передачи в него координат точек <x> и <y>"""
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y
    def __eq__(self, other: Self):
        return self.__x == other.__x and self.__y == other.__y
    def __repr__(self):
        return f'{self.__x, self.__y}'
    def __str__(self):
        return f'{self.__x, self.__y}'
    
    @property
    def x(self)-> float:
        return self.__x
    @x.setter
    def x(self, new_x: Self)-> None:
        raise TypeError('you cannot change the value of the "x" attribute in the "Point" object')
    @property
    def y(self)-> float:
        return self.__y
    @y.setter
    def y(self, new_y: Self)-> None:
        raise TypeError('you cannot change the value of the "y" attribute in the "Point" object')

class Line:
    """Создаёт объект класса Line, для построения отрезка по координатам точек из класса Point"""
    def __init__(self, start: Point, end: Point):
        self.__start = start
        self.__end = end
        self.__length = self.__length_calc(start, end)
    def __repr__(self):
        return f'{self.__start}---{self.__end}'
    def __str__(self):
        return f'{self.__start}---{self.__end}'
    @staticmethod
    def __length_calc(point1: Point, point2: Point)-> float:
        """Вычисляет длинну отрезка от точки <x> до точки <y>"""
        return round(sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2), 2)
    
    @property
    def start(self)-> Point:
       return self.__start
    @start.setter
    def start(self, new_start: Point)-> None:
        if new_start.__class__ is not self.__start.__class__:
            raise TypeError('the "start" attribute of the "Line" object accepts only "Point" objects')
        else: 
            self.__start = new_start
            self.__length = self.__length_calc(self.__start, self.__end)
    @property
    def end(self)-> Point:
        return self.__end
    @end.setter
    def end(self, new_end: Point)-> None:
        if new_end.__class__ is not self.__end.__class__:
            raise TypeError('the "end" attribute of the "Line" object accepts only "Point" objects')
        else:
            self.__end = new_end
            self.__length = self.__length_calc(self.__start, self.__end)
            
    @property
    def length(self)-> Point:
        return self.__length
    @length.setter
    def length(self, new_length)-> None:
        raise TypeError('you cannot assign the new value of the "length" attribute in the "Line" object')

class Polygon(list):
    """Создаёт объект класса Polygon, для построения многоугольника по отрезкам из класса Line """
    def __init__(self, side1: Line, side2: Line, side3: Line, *sides: Line):
        self += side1, side2, side3, *sides
    def _is_closed(self)-> bool:
        """Проверяет составляют ли переданные отрезки замкнутый многоугольник"""
        result = 1
        for i in range(1, len(self)):
            if self[i-1].end != self[i].start:
                result = 0
                break
        if self[-1].end != self[0].start:
            result = 0
        return bool(result)
    @property
    def perimeter(self)-> float:
        """Вычисляет периметр многоугольника"""
        result = 0
        if self._is_closed():
            for i in range(len(self)):
                result += self[i].length
            return result
        else:
            raise TypeError('line items doesn\'t form a closed polygon')


# C:\Users\User\HomeWork\2023.10.27>python -i 1.py
# >>>
# >>> p1 = Point(0,3)
# >>> p2 = Point(4,0)
# >>> p3 = Point(8,3)
# >>>
# >>> p1
# (0, 3)
# >>>
# >>> repr(p1) == str(p1)
# True
# >>>
# >>> p1 == Point(0,3)
# True
# >>> p1.x,p1.y
# (0, 3)
# >>> p2.y = 5
# ....
# TypeError: you cannot change the value of the "y" attribute in the "Point" object
# >>>
# >>>
# >>> l1 = Line(p1,p2)
# >>> l2 = Line(p2,p3)
# >>> l3 = Line(p3,p1)
# >>>
# >>> l1
# (0, 3)---(4, 0)
# >>>
# >>> repr(l1) == str(l1)
# True
# >>>
# >>> l1.length
# 5.0
# >>>
# >>> l1.length = 11
# ....
# TypeError: you cannot assign the new value of the "length" attribute in the "Line" object
# >>>
# >>> l3.start = 13
# ....
# TypeError: the "start" attribute of the "Line" object accepts only "Point" objects
# >>>
# >>>
# >>> pol1 = Polygon(l1,l2,l3)
# >>> pol1.perimeter
# 18.0
# >>>
# >>> l2.end = Point(10,10)
# >>> pol1.perimeter
# ....
# TypeError: line items doesn't form a closed polygon
# >>>