num_1= float(input('Написать любое число:'))
num_2 = float(input('Ещё одно:'))
num_3 = float(input('И последнее:'))

if num_1 > 0 and num_2 > 0 and num_3 > 0:
    summ = num_1 + num_2 + num_3
elif num_1 > 0 and num_2 > 0 and num_3 <= 0:
    summ = num_1 + num_2
elif num_1 <= 0 and num_2 > 0 and num_3 > 0:
    summ = num_2 + num_3
elif num_1 > 0 and num_2 <= 0 and num_3 > 0:
    summ = num_1 + num_3

if summ % 1 == 0 :
   print(int(summ))     
else:
    print(summ)

# Написать любое число:20.89
# Ещё одно:5
# И последнее:-1
# 25.89