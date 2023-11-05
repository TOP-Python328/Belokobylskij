def repeat(repeats: int = 2) -> 'function':
    """Повторяет выполнение функций переданное кол-во раз, по дефолту выполняет 2 повтора"""
    def decorator(func: 'function') -> 'function':
        def wraper(*args, **kwargs):
            # ИСПРАВИТЬ: возврат res не гарантирован (см. тест ниже)
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

# >>> def test2():
# ...    pass
# ...
# >>> test2 = repeat(0)(test2)
# >>> test2()
# ...
# UnboundLocalError: cannot access local variable 'res' where it is not associated with a value


# ИТОГ: хорошо — 3/3
