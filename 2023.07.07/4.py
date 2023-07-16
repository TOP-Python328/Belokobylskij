number =int(input('Введите любое трёхзначное число:'))
num_3 = number % 10
num_2 = int(number / 10) % 10
num_1 = int(number / 100)
num_sum = num_1 + num_2 + num_3
multiplication = num_1 * num_2 * num_3
print(f'Сумма всех цифр числа "{number}": {num_sum} \nПроизведение всех цифр числа "{number}": {multiplication} ')


# Введите любое трёхзначное число:325
# Сумма всех цифр числа "325": 10
# Произведение всех цифр числа "325": 30