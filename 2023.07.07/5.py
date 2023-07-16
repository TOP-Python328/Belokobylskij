num_1 = input('Введите целую часть: ')
num_2 = input('Введите дробную часть:')
miles = num_1 + '.' + num_2
kilometers = round(float(miles) * 1.61, 1)
print(f'{miles} миль = {kilometers} километров.')

# Введите целую часть: 3
# Введите дробную часть:48
# 3.48 миль = 5.6 километров.