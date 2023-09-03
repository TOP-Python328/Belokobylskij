def math_function_resolver (
                                    func: 'function',
                                    *numb: float, 
                                    string: bool = False
) -> list [float | str]:
                                    
    """Принимает позиционные аргументы: любую математическую функцию с одним аргументом и число или произвольный кортеж чисел и возвращает вычисленное значение мат.функцией для переданного в нее числа или кортежа чисел."""
    
    result = []
    for el in numb:
        if string:
            result.append(str(round(float(func(el)),2)))
        else:    
            result.append(round(float(func(el)),2)) 
    return result
    
# Я не совсем понял на счет передаваемой в аргументы функии. Я правильно сделал что взял из вашего примера или надо было написать свою?    

 # >>> math_function_resolver(lambda x: 2.72**x, *range(1, 10),string=True)
# ['2.72', '7.4', '20.12', '54.74', '148.88', '404.96', '1101.49', '2996.07', '8149.3']

# >>> math_function_resolver(lambda x: 2*x + 1, *range(1, 10),string=True)
# ['3.0', '5.0', '7.0', '9.0', '11.0', '13.0', '15.0', '17.0', '19.0']

# >>> math_function_resolver(lambda x: 2*x + 1, *range(1, 10))
# [3.0, 5.0, 7.0, 9.0, 11.0, 13.0, 15.0, 17.0, 19.0]

# >>> math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10))
# [1.5, 1.0, 0.5, 0.0, -0.5, -1.0, -1.5, -2.0, -2.5]

# >>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
# [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5]