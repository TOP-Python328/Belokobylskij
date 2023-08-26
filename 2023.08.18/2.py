def taxi_cost (distance: int, wait: int = 0) -> int | None:
    """Расчитывает стоимость поездки"""
    cost = 0
    basic_price_and_waiting =  80 + wait * 3
    if distance < 0:
        return None
    elif distance == 0:
        cost = basic_price_and_waiting + 80
    elif distance > 0:
        cost = (distance / 150) * 6 + basic_price_and_waiting
    return round(cost)    
    
 # >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0,5)
# 175
# >>> taxi_cost(42130,8)
# 1789
# >>> print(taxi_cost(-200))
# None