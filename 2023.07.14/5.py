user_coord_1 = input('Ладья. Введите координату откуда ходим:').lower()
user_coord_2 = input('Введите координату куда ходим:').lower()
coord_y_1 = user_coord_1[1]  
coord_x_1 = user_coord_1[0]

coord_y_2 = user_coord_2[1]
coord_x_2 = user_coord_2[0]

if coord_y_1 == coord_y_2 or coord_x_1 == coord_x_2:
    print('Ход верный')
else: 
    print('Ход не верный')
    
# Ладья. Введите координату откуда ходим:B4
# Введите координату куда ходим:h4
# Ход верный

# Ладья. Введите координату откуда ходим:b4
# Введите координату куда ходим:c3
# Ход не верный