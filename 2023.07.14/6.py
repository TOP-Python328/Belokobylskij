user_coord_1 = input('Король. Введите координату откуда ходим:').lower()
user_coord_2 = input('Введите координату куда ходим:').lower()

chees_coord_x = '-abcdefgh'

coord_y_1 = int(user_coord_1[1])
coord_y_2 = int(user_coord_2[1])

# УДАЛИТЬ: эти переменные используются каждая только единожды — в их создании нет необходимости
coord_x_1 = user_coord_1[0]
coord_x_2 = user_coord_2[0]

a = chees_coord_x.index(coord_x_1)
b = chees_coord_x.index(coord_x_2)

# ИСПРАВИТЬ: упростите логические выражения (в том числе избавившись от вложенного) используя модуль числа и неравенства
if chees_coord_x[a] == chees_coord_x[b] or chees_coord_x[a-1] == chees_coord_x[b] or chees_coord_x[a+1] == chees_coord_x[b]:
    if coord_y_1 - coord_y_2 == -1 or coord_y_1 - coord_y_2 == 0 or coord_y_1 - coord_y_2 == 1:
        print('Ход верный.')
    else:
        print('Ход не верный.')
else:
    print('Ход не верный.')


# Король. Введите координату откуда ходим:c3
# Введите координату куда ходим:d2
# Ход верный.

# Король. Введите координату откуда ходим:a5
# Введите координату куда ходим:h4
# Ход не верный.


# (chees_coord_x = '-abcdefgh')- подскажите пожалуйста это норм что я так сделал? Я [0] элемент добавил не очевидный, для того чтоб в этом участке кода (or chees_coord_x[a -1] == chees_coord_x[b]) все правильно считалось, получается если "а" будет [0] элемент то если сравнивать с "h" прога говорит что всё правильно хотя не должно быть.  Или это прям дилетанство и надо было что то придумать другое? Я просто не смог лучше придумать))))
# КОММЕНТАРИЙ: сама задумка со строкой, в которой ищете индексы, это вполне хорошая мысль — а добавление в эту строку лишнего элемента '-' это костыль, который нужен для оправдания малоосмысленной идеи обратного перехода от чисел индексов к символам вертикалей (chees_coord_x[a] и прочее)
# КОММЕНТАРИЙ: во вложенном блоке if вы проверяете горизонтали вычитанием соответствующих координат — прекрасно, почему бы не сделать то же самое с вертикалями? вы же получали для них числа через индексы


# ИТОГ: неплохо, но нужно лучше — 3/5


# КОММЕНТАРИЙ: следите за пробелами в коде и в выводе
