# ИСПРАВИТЬ: вам может потребоваться использовать имя в разных контекстах, и далеко не везде будет нужна запятая
# name = input('Напишите своё имя:') + ','
# КОММЕНТАРИЙ: функция input() в отличие от print() ничего не дописывает в stdout после вывода переданного аргумента — поэтому для лучшей читаемости вам необходимо самостоятельно добавить пробел, или табуляцию, или символ конца строки в конец аргумента функции input()
# last_name = input('Напишите свою фамилию:')
# year = int(input('Напишите год своего рождения:'))
# age = 2023 - year
# print(last_name, name, age)


# Напишите своё имя:Виктор
# Напишите свою фамилию:Белокобыльский
# Напишите год своего рождения:1991
# Белокобыльский Виктор, 32
# -------------------------------------------------------------
# Исправил. Надеюсь я вас правильно понял и сделал так как надо было.

user_name = input('Напишите своё имя: ')
user_last_name = input('Напишите свою фамилию: ')
user_year = int(input('Напишите год своего рождения: '))
user_age = 2023 - user_year

print(user_last_name, user_name + ',', user_age)

# Напишите своё имя: Виктор
# Напишите свою фамилию: Белокобыльский
# Напишите год своего рождения: 1991
# Белокобыльский Виктор, 32
# ИТОГ: очень хорошо, немного изменить — 3/4
