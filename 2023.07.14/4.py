user_coord_1 = input('Введите координату откуда ходим:').lower()
user_coord_2 = input('Введите координату куда ходим:').lower()
coord_y_1 = int(user_coord_1[1])  
coord_x_1 = user_coord_1[0]

coord_y_2 = int(user_coord_2[1])
coord_x_2 = user_coord_2[0]
chees_coord_x = '-abcdefgh'
num_coord_x_1 = chees_coord_x.index(coord_x_1)
num_coord_x_2 = chees_coord_x.index(coord_x_2)

if (num_coord_x_1 + coord_y_1) % 2 == 0 and (num_coord_x_2 + coord_y_2) % 2 == 0 or (num_coord_x_1 + coord_y_1) % 2 != 0 and (num_coord_x_2 + coord_y_2) % 2 != 0:
    print('Одинаковые')    
else:
    print('Разные')    

# Введите координату откуда ходим:b1
# Введите координату куда ходим:f3
# Одинаковые

# Введите координату откуда ходим:d3
# Введите координату куда ходим:h8
# Разные