list_fruits = []
stop_list = ['', ' ']
result_list = ''

while True:
    user_inp = input('Напишите фрукт: ')
    if user_inp in stop_list:
        break
    else:
        list_fruits += [user_inp]
len_list_fruits = len(list_fruits)                

if len_list_fruits == 1:
    result_list += list_fruits[0]
elif len_list_fruits == 2:
    result_list += ' и '.join(list_fruits)
elif len_list_fruits > 2:
    result_list += ', '.join(list_fruits[:-1]) + ' и ' + list_fruits[-1]
print(result_list)    

# Напишите фрукт: яблоко
# Напишите фрукт:
# яблоко

# Напишите фрукт: яблоко
# Напишите фрукт: груша
# Напишите фрукт:
# яблоко и груша

# Напишите фрукт: яблоко
# Напишите фрукт: груша
# Напишите фрукт: банан
# Напишите фрукт:
# яблоко, груша и банан

# Напишите фрукт: яблоко
# Напишите фрукт: груша
# Напишите фрукт: банан
# Напишите фрукт: киви
# Напишите фрукт:
# яблоко, груша, банан и киви