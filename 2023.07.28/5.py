scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

user_word = input('Напишите слово: ').upper()
result = 0
for key, val in scores_letters.items():
    for letter in user_word:
        if letter == 'Ё':
            letter = 'Е'
        if letter in val:
            result += key
print(result)


# Напишите слово: Параллелепипед
# 21

# Напишите слово: синхрофазотрон
# 29

# Напишите слово: елка
# 6

# Напишите слово: ёлка
# 6

