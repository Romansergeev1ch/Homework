# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

months_day_count = {'1':  31,
                    '2':  28,
                    '3':  31,
                    '4':  30,
                    '5':  31,
                    '6':  30,
                    '7':  31,
                    '8':  31,
                    '9':  30,
                    '10': 31,
                    '11': 30,
                    '12': 31,
                    }


user_input = input("Введите, пожалуйста, номер месяца: ")
if user_input.isdigit():
    month = int(user_input)

    if 1 <= month <= 12:
        day_count = months_day_count[user_input]
        print('Вы ввели', month)
        print('Кол-во дней в месяце:', day_count)
    else:
        print('Такого месяца нет!')
else:
    print('Необходимо ввести число.')