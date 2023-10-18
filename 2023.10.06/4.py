from pathlib import Path
from sys import path
from csv import writer, reader 
 # {class} в данном контексте указывает на необходимость определения классового метода - Не совсем понял что это значит, вернее совсем не понял.
class CountableNouns:
    """Предоставляет интерфейс для работы с файловой базой существительных"""
    db_path = Path(path[0]) / 'words.csv'
    words = dict()
    with open(db_path, encoding='utf-8') as csvfile:
        words_csv = reader(csvfile)
        for str_ in words_csv:
            words[str_[0]] = str_[1], str_[2]
  
    def pick(number: int, word: str)-> str:
        """Возвращает согласованное с переданным числом существительное"""
        if number % 100 in [11, 12, 13, 14]:
            return CountableNouns.words[word][1]
        elif  number % 10 == 1:
            return word
        elif number % 10 in [2, 3, 4]:
            if word not in CountableNouns.words:
                print(f'существительное {word} отсутствует в базе')
                CountableNouns.save_words(word)
            return CountableNouns.words[word][0]
        else:
            return CountableNouns.words[word][1]

    def save_words(word1: str=None)-> None:
        """Добавляет полученные значения в поле класса words и дописывает их в файл с базой существительных"""
        key = ''
        val = ()
        if word1:
            CountableNouns.words[word1] = input('введите слово, согласующееся с числительным "два":'), input('введите слово, согласующееся с числительным "пять":'),
        else:
            key = input('введите слово, согласующееся с числительным "один":')
            val = input('введите слово, согласующееся с числительным "два":'), input('введите слово, согласующееся с числительным "пять":'),
            CountableNouns.words[key] = val
        with open(CountableNouns.db_path, 'w',encoding='utf-8') as csvfile:
            str_csv = writer(csvfile, lineterminator='\n')
            for key,val in CountableNouns.words.items():
                str_csv.writerow([key, val[0],val[1]])

# C:\Users\User\HomeWork\2023.10.06>python -i 4.py
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней')}
# >>> CountableNouns.pick(22,'год')
# 'года'
# >>> CountableNouns.pick(365,'день')
# 'дней'
# >>> CountableNouns.pick(31,'попугай')
# 'попугай'
# >>> CountableNouns.pick(22,'попугай')
# существительное попугай отсутствует в базе
# введите слово, согласующееся с числительным "два":попугая
# введите слово, согласующееся с числительным "пять":попугаев
# 'попугая'
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'попугай': ('попугая', 'попугаев')}
# >>> CountableNouns.save_words()
# введите слово, согласующееся с числительным "один":капля
# введите слово, согласующееся с числительным "два":капли
# введите слово, согласующееся с числительным "пять":капель
# >>> print(CountableNouns.db_path.read_text(encoding='utf-8'))
# год,года,лет
# месяц,месяца,месяцев
# день,дня,дней
# попугай,попугая,попугаев
# капля,капли,капель