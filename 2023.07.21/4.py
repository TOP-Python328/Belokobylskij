# ПЕРЕИМЕНОВАТЬ: разряды чисел — digits, ranks
user_num = int(input('Введите количество разрядов числа: '))
list_num = []
list_num2 = []

for num in range(1, int('1' + '0'*user_num)):
    # ИСПРАВИТЬ: выполнять преобразование в строку и вычислять длину этой строки на каждой итерации — это ОЧЕНЬ неоптимально
    if len(str(num)) == user_num:
        list_num += [num]

# ИСПОЛЬЗОВАТЬ: вместо того, чтобы генерировать последовательность чисел от единицы, а затем проверять каждое число, стоило вычислить обе границы искомого диапазона
left = int('1' + '0'*(user_num - 1))
right = left * 10

# ИСПРАВИТЬ: избыточная генерация последовательности — ранее вы создали список требуемых чисел, значит здесь можете перебрать элементы в уже готовом списке (именно так работает цикл for в Python)
for numb in range(list_num[0], list_num[-1] + 1):
    dividers = 0
    # ИСПРАВИТЬ: здесь ваша задача не найти все делители, а проверить, является ли число простым (тест на простоту) — в переборе делителей для этого достаточно найти только один делитель кроме единицы и самого числа (которые являются делителями всегда, а потому проверять их нет смысла), и все последующие итерации станут избыточными
    # ИСПРАВИТЬ: диапазон перебора, конечно, тоже надо поправить — это вы можете отработать в предыдущей задаче
    for num2 in range(1, numb + 1):
        if numb % num2 == 0:
            dividers += 1
    # ДОБАВИТЬ: и вспомните, что я рассказывал про else блок циклов — здесь он вам пригодится
    if dividers == 2:
        list_num2 += [numb]
print(len(list_num2))


# Введите количество разрядов числа: 3
# 143

# Введите количество разрядов числа: 4
# 1061


# 1) Насколько я понимаю код не самый оптимальный. 5 разрядные числа комп за 2 минуты не посчитал и проц нагрузил почти на 50% или это нормально и для такого количества цифр надо много времени?
# КОММЕНТАРИЙ: не нормально, конечно: есть много алгоритмов проверки числа на простоту, но даже при использовании "лобового", но оптимизированного перебора делителей для пятиразрядных чисел достаточно 100–300 мс

# 2) Очень долго думал над кодом и придумал такой вариант, придумал сам. Только единственное я изначально написал без счетчика  dividers и немного другое условие во вложенном цикле писал и вывод был не верным и очень много дублей было, сам не смог справиться и обратился к яндексу. И в связи с этим вопрос! Искать подсказки в интернете это прям позор и полагается линейкой по рукам настучать)) или если по чуть-чуть и не в наглую списывать решение, а разобрать пример и применить на практике, это можно и не возбраняется!?
# КОММЕНТАРИЙ: позор — это без рефлексии взять готовое решение; а если пошагово разобрались и целиком восприняли алгоритм и код, то не возбраняется, конечно
# ОТВЕТИТЬ: а где придуманный/найденный способ-то?)


# ИТОГ: нужно лучше, доработать — 2/5
