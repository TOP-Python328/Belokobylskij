user_email = input('Введите электронную почту: ')
result = ''
# ИСПРАВИТЬ: символ '.' должен быть правее символа '@' (см. тест ниже)
if user_email.find('@') > 0 < user_email.find('.'):
    result = 'Да'
else:
    result = 'нет'
print(result)

# ИСПОЛЬЗОВАТЬ: когда пишете неравенства, то всегда представляйте числовую ось, нанесите на неё метки ваших литералов и выражений для истинного условия — в каком порядке у вас окажутся подписи меток, в таком же порядке записывайте неравенства — так станет куда проще воспринимать условие целиком; например для определения, является ли num двузначным числом:
# 10 <= num < 100


# Введите электронную почту: aedfsfsfwef
# нет

# Введите электронную почту: asdf@sdffd
# нет

# Введите электронную почту: asdfsdf.sdf
# нет

# Введите электронную почту: asdfs@sdf.dsf
# Да

# Введите электронную почту: ab.cd@ef
# Да


# ИТОГ: доработать — 2/4
