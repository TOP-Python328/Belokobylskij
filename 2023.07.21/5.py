user_inp = input('Напишите текст: ').split(' ')
str_char = ''
price = 0.30
for word in user_inp:
    str_char += word
cost = str(len(str_char) * price).split('.')  
print(f'{cost[0]}руб. {cost[1] + "0"}коп. ')    

# Напишите текст: грузите апельсины бочках братья карамазовы
# 11руб. 40коп.

# Напишите текст: Текст (от лат. textus - ткань; сплетение, сочетание) - зафиксированная на каком-либо материальном носителе человеческая мысль; в общем плане связная и полная последовательность символов.
# 48руб. 90коп.

# Какая то странная история произошла у меня! Вначале я присваивал переменным подобные значения: a = len(str_char) * price и при записи в f-строку этих переменных интерпретатор выдавал значение 0. Причем если в f-строку вписывал таким образом -  len(str_char) * price, то все вычислялось норм. И после того как я переписал код, в инспекции смотрел за поведением этих переменных и им начали присваиваться нормальные значения. Вы когда нибудь с таким сталкивались? Я очень долго пытался что то сделать  с теми переменными и это привело меня к тому что я переписал код.  