from math import  sqrt

class Tetrahedron:
    """Вычисляет площадь и объем тэтраэдра"""
    
    def __init__ (self, edge: float):
        self.edge = float(edge)   

    def surface (self)-> float:
        """возвращает вычисленную площадь"""
        square = self.edge**2  * sqrt(3)
        return square

    def  volume (self)-> float:
        """Возвращает вычисленный объем"""
        vol = self.edge**3 / 12 * sqrt(2)
        return vol

# C:\Users\User\HomeWork\2023.10.06>python -i 1.py
# >>> t1 = Tetrahedron(5)
# >>> t1.edge
# 5.0
# >>> t1.surface()
# 43.30127018922193
# >>> t1.volume()
# 14.73139127471974
# >>> t1.edge = 6
# >>> t1.surface()
# 62.35382907247958
# >>>