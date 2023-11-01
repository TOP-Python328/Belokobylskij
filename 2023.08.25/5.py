def logger(func: 'function') -> 'function':
    """Ведет журнал вызовов функций в стандартном потоке вывода + перехват исключений и их вывод"""
    def wraper(*args, **kwargs):
        arguments = (str(el) for el in args[:func.__code__.co_argcount])
        try:
            def_args = ''
            if func.__defaults__:
                for el in func.__defaults__:
                    def_args = f', default= {el}' 
            if kwargs:
                for k,v in kwargs.items():
                    kwdef = f'{k}= {v}'
            else:
                for k,v in func.__kwdefaults__.items():
                    kwdef = f'{k}= {v}'
            str_func = f'{func.__name__}({ ", ".join(arguments) + def_args}, {kwdef}) -> '
            res = func(*args, **kwargs)
        except Exception as exc:
            pass
            print(str_func + f'{type(exc).__name__}: {exc}')
        else:
            print(str_func + f'{res}')
            return res    
    return wraper        


# У меня имеется вопрос!  Я не пойму как быть с значением по умолчанию, а конкретно не догоню как сделать чтоб его небыло в выводе если мы не используем это самое значение.
# КОММЕНТАРИЙ: считать уже использованные значения (см. пример)


def div_round(num1, num2: int = 2, *, digits=0):
    return round(num1 / num2, digits)
div_round = logger(div_round)    

# >>> div_round(14,4)
# div_round(14, 4, default= 2, digits= 0) -> 4.0
# 4.0

# >>> div_round(14)
# div_round(14, default= 2, digits= 0) -> 7.0
# 7.0

# >>> div_round(14,4,digits= 2)
# div_round(14, 4, default= 2, digits= 2) -> 3.5
# 3.5

# >>> div_round(14,0,digits= 2)
# div_round(14, 0, digits= 2) -> ZeroDivisionError: division by zero
# >>>


# ИТОГ: неплохо, доработайте — 4/7
