# num = int(input('Введите кол-во минут и мы посчитаем сколько это часов и минут: '))
# УДАЛИТЬ: эти переменные используются каждая только единожды — в их создании нет необходимости
# hour = num // 60
# minute = num % 60
# ИСПРАВИТЬ: несоответствие требуемому формату (см. комментарий к тесту)
# print(f'{num} минут - это {hour} ч. и {minute} мин. ')


# Введите кол-во минут и мы посчитаем сколько это часов и минут: 176
# 176 минут - это 2 ч. и 56 мин.
# КОММЕНТАРИЙ: а должно быть:
# 176 мин - это 2 час 56 мин

# КОММЕНТАРИЙ: в случае если вы будете генерировать строку не для человека, а для другой функции/класса/программы — это может стоить вам неработающего приложения

num = int(input('Введите кол-во минут и мы посчитаем сколько это часов и минут: '))
print(f'{num} мин - это {num // 60} час и {num % 60} мин ')

# Введите кол-во минут и мы посчитаем сколько это часов и минут: 176
# 176 мин - это 2 час и 56 мин
# ИТОГ: хорошо, но можно лучше — 3/5
