year = int(input('Введите год и проверим високосный ли он: '))

if year % 4 == 0:
    print('Да')
elif year % 4 == 0 and year % 100 != 0:
    print('Да')
else: 
    print('Нет')
    
# Введите год и проверим високосный ли он: 2000
# Да

# Введите год и проверим високосный ли он: 1996
# Да

# Введите год и проверим високосный ли он: 2002
# Нет
# -------------------------------------------------------------------------

# year = int(input('Введите год и проверим високосный ли он:'))

# ИСПРАВИТЬ: условие в левом операнде лишнее: если число кратно 400, значит точно кратно 4
# if year % 4 == 0 and year % 400 == 0:
    # print('Да')
# elif year % 4 == 0 and year % 100 != 0:
    # print('Да')
# else: 
    # print('Нет')


# Введите год и проверим високосный ли он:2023
# Нет

# ДОБАВИТЬ: тесты с другими входными данными


# ИТОГ: хорошо — 2/3
