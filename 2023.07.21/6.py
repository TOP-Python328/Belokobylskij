ticket_num = input('Введите свой билет: ')
lucky_ticket  = ''
list_digit =[int(digit) for digit in ticket_num]
if sum(list_digit[:3]) == sum(list_digit[3:]):
    lucky_ticket = 'Да'
else: lucky_ticket = 'Нет'    
print(lucky_ticket)

# Введите свой билет: 123321
# Да

# Введите свой билет: 123456
# Нет