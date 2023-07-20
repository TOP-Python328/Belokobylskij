year = int(input('Введите год и проверим високосный ли он:'))

if year % 4 == 0 and year % 400 == 0:
    print('Да')
elif year % 4 == 0 and year % 100 != 0:
    print('Да')
else: 
    print('Нет')
    
    # Введите год и проверим високосный ли он:2023
# Нет