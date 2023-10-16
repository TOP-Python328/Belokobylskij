
import datetime, decimal, numbers
class PowerMeter:
    """Описывает двух тарифный счетчик"""
    current_date = datetime.date.today()
    # Думаю что не совсем верно аннотации сделал, я просто написал так же как в дз описано.... правильно сделал или нет?
    def __init__(self, 
                            tariff1: numbers.Number = 7, 
                            tariff2: numbers.Number = 3, 
                            tariff_starts: datetime.time = 23, 
                            tariff_ends: datetime.time = 7):
        """"""
        self.tariff1 = decimal.Decimal(tariff1)
        self.tariff2 = decimal.Decimal(tariff2)
        self.tariff_starts = datetime.time(tariff_starts)
        self.tariff_ends = datetime.time(tariff_ends)
        self.power = decimal.Decimal(0)
        self.charges = dict().fromkeys(range(1,13), decimal.Decimal(0))
        
     
    def __repr__(self):
        return f'<PowerMeter: {self.power} кВт/ч>'
        
    def __str__(self):
        str_month = datetime.datetime.strftime(self.__class__.current_date, '%b' )
        return f'({str_month}) {self.charges[self.__class__.current_date.month]} '
        
    def meter(self, power: numbers.Number)-> decimal:
        """Возвращает стоимость согласно тарифному плану, действующему в текущий момент"""
        dec_power = round(decimal.Decimal(power),2)
        self.power += dec_power
        cost = 0
        current_time = datetime.datetime.now().time()
        if current_time < self.tariff_starts and current_time > self.tariff_ends:
            cost += dec_power * self.tariff1
        else:
            cost += dec_power * self.tariff2
        self.charges[self.__class__.current_date.month] += cost 
        return cost
        
# C:\Users\User\HomeWork\2023.10.06>python -i 2.py
# >>> pm = PowerMeter()
# >>> pm.meter(2)
# Decimal('6.00')
# >>> pm.meter(1.2)
# Decimal('3.60')
# >>> pm
# <PowerMeter: 3.20 кВт/ч>
# >>> print(pm)
# (Oct) 9.60
# >>>  
      
# проверку в разное время делал

# >>> pm.meter(2)
# Decimal('14.00')
# >>> pm.meter(1.2)
# Decimal('8.40')
# >>>