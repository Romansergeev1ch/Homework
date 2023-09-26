# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

splitted_line = (my_favorite_songs).split(',')
print(splitted_line[0] + splitted_line[4] + splitted_line[1] + splitted_line[3])

# result = Waste a Moment New Salvation Staying Alive Start Me Up
