# Решил последовать вашему совету и переключился на текущее задание. Постараюсь остальное из этого ДЗ выполнить как можно быстрее. 
# Скорее всего это задание мне надо будет переделать и есть пара вопросов: 
# 1) Символы прочих категорий их же оч много! Тут наверно надо проверять что символ пароля не равен буквам и цифрам, чтоб не выписывать символы как я это сделал!? 
# 2) Вот код вроде работает, НО если я пишу и латинские буквы и наши родненькие то в result попадает True хотя должен быть False. Я пытался это исправить и что то ничего не получилось, я думаю что условие надо менять. А на что менять не пойму. Намекните пожалуйста в какую сторону смотреть чтоб это всё исправить!?

def strong_password (password: str) -> bool:
    """Проверяет пароль на корректность"""
    result = False
    low = 0
    up = 0
    dig = 0
    char = 0
    digit_in_pass = [dig for dig in password if dig in '0123456789']
    other_valid_char = '!@#$%^&*()_№-+=/.,<>:;"\'[]{}?`~\n\t '
    if len(password) >= 8:
        for el in password:
            if ord(el) in range(65, 91):
                up = 1  
            if ord(el) in range(97, 123):    
                low = 1
            if len(digit_in_pass) >= 2:
                dig = 1
            if el in other_valid_char:
                char = 1
    if low + up + dig + char == 4:
        result = True
    return result
    
# >>> strong_password('Fasdfs1:')
# False
# >>> strong_password('Fasdfs12')
# False
# >>>
# >>> strong_password('asdasdfs')
# False
# >>> strong_password('ф1ыввААЫф2:')
# False
# >>> strong_password('Fgs1asd2:')
# True
# >>> strong_password('asdFR1ЫЦап3!')
# True