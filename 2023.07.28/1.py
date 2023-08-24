user_email = input('Введите электронную почту: ')
result = ''
if user_email.find('@') > 0 < user_email.find('.'):
    result = 'Да'
else:
    result = 'нет'
print(result)


# Введите электронную почту: aedfsfsfwef
# нет

# Введите электронную почту: asdf@sdffd
# нет

# Введите электронную почту: asdfsdf.sdf
# нет

# Введите электронную почту: asdfs@sdf.dsf
# Да

