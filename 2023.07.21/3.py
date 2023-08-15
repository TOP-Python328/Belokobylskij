user_num = int(input('Введите натуральное число: '))

# sum_divider = 0
# for num in range(1, user_num + 1):
    # if user_num % num == 0:
        # sum_divider += num
        
sum_divider = sum([num for num in range(1, user_num + 1) if user_num % num == 0])
print(sum_divider)   

# Введите натуральное число: 51
# 72

# Введите натуральное число: 50
# 93
