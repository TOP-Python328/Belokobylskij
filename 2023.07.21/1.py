list_num = []
while True:
    user_inp = int(input('Введите число: '))
    if user_inp % 7 != 0:
        break
    else:  list_num += [user_inp]
print (*reversed(list_num))    

# Введите число: 14
# Введите число: 21
# Введите число: 7
# Введите число: 14
# Введите число: 14
# Введите число: 2
# 14 14 7 21 14