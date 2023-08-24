list_user_inp = []
while True:
    user_inp = input('Введите число и текст через пробел: ')
    if not user_inp:
        break
    # ИСПОЛЬЗОВАТЬ везде: PEP 8 не рекомендует записывать тело блока в одну строчку с заголовком блока
    else:
        list_user_inp += [user_inp.split(' ')]

dict_inp = {key: val for key, val in list_user_inp}
user_inp = input('Введите текст: ')
result = '! value error !'
for key, val in dict_inp.items():
    if user_inp == val:
        result = key
print(result)


# Введите число и текст через пробел: 1022 ER_DUP_KEY
# Введите число и текст через пробел: 1016 ER_CANT_OPEN_FILE
# Введите число и текст через пробел: 1010 ER_DB_DROP_RMDIR
# Введите число и текст через пробел: 1008 ER_DB_DROP_EXISTS
# Введите число и текст через пробел: 1007 ER_DB_CREATE_EXISTS
# Введите число и текст через пробел: 1006 ER_CANT_CREATE_DB
# Введите число и текст через пробел: 1005 ER_CANT_CREATE_TABLE
# Введите число и текст через пробел: 1004 ER_CANT_CREATE_FILE
# Введите число и текст через пробел:
# Введите текст: ER_CANT_CREATE_DB
# 1006   

# Введите число и текст через пробел: 4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
# Введите число и текст через пробел: 4108 ER_GIPK_COLUMN_EXISTS
# Введите число и текст через пробел: 4111 ER_DROP_PK_COLUMN_TO_DROP_GIPK
# Введите число и текст через пробел: 4113 ER_DA_EXPIRE_LOGS_DAYS_IGNORED
# Введите число и текст через пробел: 4114 ER_CTE_RECURSIVE_NOT_UNION
# Введите число и текст через пробел:
# Введите текст: ER_CANT_OPEN_FILE
# ! value error !

