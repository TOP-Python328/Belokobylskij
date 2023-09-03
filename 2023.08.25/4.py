def repeat (repeats: int= 2) -> 'function':
    """Повторяет выполнение функций переданное кол-во раз, по дефолту выполняет 2 повтора"""
    def decorator(func: 'function') -> 'function':
        def wraper(*args, **kwargs):
            for n in range(repeats):
                res = func(*args, **kwargs)
            return res
        return wraper
    return decorator

@repeat(6)
def test_func():
    print('Python')
    
# >>> test_func()
# Python
# Python
# Python
# Python
# Python
# Python
# >>>    