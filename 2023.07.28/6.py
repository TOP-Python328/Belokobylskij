# В общем я думаю что это не код, а дичь полная! Просто в голове 0 идей как эту задачу выполнить! В первый раз такое. Я предполагаю что здесь какое то не сильно сложное решение, но понять не могу. Прям бесит))) Я обе лекции пересмотрел и в документации лазил и ничего не натолкнуло на какую то идею оптимально код написать! Подскажите пожалуйста что делать надо.
user_inp = input('Введите число в двоичной системе счисления: ')
list_user_inp = [user_inp.split('b')]
prefix = ['', '0']
binary_set = {'1', '0'}
set_user_num = set()
result = 'Нет'
if 'b' in user_inp:
    for pref, num in list_user_inp:
        if pref in prefix:
            set_user_num = {dig for dig in num}    
    for el in set_user_num:
        if set(el) < binary_set:
            result = 'Да' 
else:
    set_user_num = {dig for dig in user_inp}
    for el in set_user_num:
        if set(el) <= binary_set:
            result = 'Да'
print(result)
# Введите число в двоичной системе счисления: 0101
# Да
# Введите число в двоичной системе счисления: 0b11001
# Да
# Введите число в двоичной системе счисления: b11
# Да

# Введите число в двоичной системе счисления: 1b01011
# Да
 