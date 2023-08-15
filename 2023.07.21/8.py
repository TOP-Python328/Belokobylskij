user_num = int(input('Введите число: '))
index = 1
num_fibo = [1,1]
while len(num_fibo) < user_num:
    num_fibo += [num_fibo[index -1] + num_fibo[index]]    
    index += 1
if user_num == 1:
    print(num_fibo[0])
else: print(*num_fibo)

# Введите число: 1
# 1

# Введите число: 3
# 1 1 2

# Введите число: 18
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584