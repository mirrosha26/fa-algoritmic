# Правки: нужно поменть на функцию
def  min_reduction(mas):
    min_len = len(mas[0])
    for i in range(1, len(mas)):
        check_len = len(mas[i])
        if check_len < min_len:
            min_len= check_len
    return list(map(lambda x:x[:min_len] , mas ))

# тест
mas = ['Привет', 'Пока', 'И ты?', 'И я', 'О, да']
print(min_reduction(mas))
