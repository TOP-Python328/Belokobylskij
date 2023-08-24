user_inp1 = input('Введите число: ').split(' ')
user_inp2 = input('Введите ещё число: ').split(' ')
result = 'Нет'
list_num = [int(elem) for elem in user_inp1]
sublist_num = [int(elem) for elem in user_inp2]

# ---------------------Это первый вариант(но скажу честно я немного подсмотрел его)-----------------
# len_sublist = len(sublist_num)
# for index in range(len(list_num) - len_sublist + 1):
#     if list_num[index:index + len_sublist] == sublist_num:
#         result = 'Да'
# print(result) 

# Введите число: 313 21 34 1 2 515 32 2 90
# Введите ещё число: 21 313 34 1
# Нет
# Введите число: 313 21 34 1 2 515 32 2 90
# Введите ещё число: 1 2 515
# Да


# ---------------Этот я сам написал (правда потратил на него часов 6)--------------
index_list = []
list_tuples = enumerate(list_num)
result_list_num = []
index_list = [el[0] for el in list_tuples if el[1] in sublist_num]
for i in index_list:
    n = 1
    if index_list[n] - index_list[n-1] == 1:
        n += 1
        result_list_num += [list_num[i]]
if result_list_num == sublist_num:
    result = 'Да'
print(result)


# Введите число: 12 31 2 34 11 23 1 5 123 43 90
# Введите ещё число: 34 11 23
# Да

# Введите число: 12 31 2 34 11 23 1 5 123 43 90
# Введите ещё число: 31 11 23 1
# Нет

