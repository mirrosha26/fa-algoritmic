# задаем список
mas = ['Привет', 'Пока', 'И ты?', 'И я', 'О, да']
min_len = len(mas[0])
for i in range(1, len(mas)):
    check_len = len(mas[i])
    if check_len < min_len:
        min_len= check_len
print(list(map(lambda x:x[:min_len] , mas )))a
