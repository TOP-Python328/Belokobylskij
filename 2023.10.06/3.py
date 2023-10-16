class ChessKing:
    """Описывает шахматную фигуру короля"""
    files = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    ranks = {'1':1, '2':2, '3':3, '4':4 ,'5':5, '6':6, '7':7, '8':8}
    
    def __init__(self, color: str= 'white', square: str= None):
        self.color = color
        if not square:
            if color == 'black':
                square = 'e8'
                self.square = square
            else:
                square = 'e1' 
                self.square = square
        else:
            self.square = square
    def __repr__(self):
        if self.color == 'white':
            return f'\'WK: {self.square}\''
        else:
            return f'\'BK: {self.square}\''

    def __str__(self):
        if self.color == 'white':
            return f'WK: {self.square}'
        else:
            return f'BK: {self.square}'

    def is_turn_valid(self, new_square: str)-> bool:
        """Проверяет правильность хода"""
        right_move = [-1,0,1]
        vertical = self.files[self.square[0]] - self.files[new_square[0]]
        horizont = self.ranks[self.square[1]] - self.ranks[new_square[1]]
        if vertical in right_move and horizont in right_move:
            return True
        else:
            return False

    def turn(self, new_square: str)-> None:
        """Выполняет ход"""
        try:
            if self.is_turn_valid(new_square):
                self.square = new_square
            else:
                raise TypeError('ValueError')
        except TypeError:
            print('ValueError')

# C:\Users\User\HomeWork\2023.10.06>python -i 3.py
# >>> wk=ChessKing()
# >>> wk.color
# 'white'
# >>> wk.square
# 'e1'
# >>> wk.turn('f1')
# >>> wk
# 'WK: f1'
# >>> wk.turn('d4')
# ValueError
# >>> bk = ChessKing('black')
# >>> print(bk)
# BK: e8
# >>>