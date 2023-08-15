natural_num = int(input('Введите натуральное число: '))
summ = 0
iteration = 1
while iteration <= natural_num:
    other_num = int(input('Введите любые целые числа: '))
    iteration += 1
    if other_num > 0:
        summ += other_num
print(summ)        

# Введите натуральное число: 5
# Введите любые целые числа: -2
# Введите любые целые числа: 0
# Введите любые целые числа: 1
# Введите любые целые числа: 9
# Введите любые целые числа: 15
# 25