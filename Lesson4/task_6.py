x = int(input('Введите целое число: '))
y = int(input('Введите целое число: '))
if x > 10 and y > 10:
    print('Оба числа больше 10')
elif x > 10 or y > 10:
    print('Одно из чисел больше 10')
elif bool(x):
    print('Условие с помощью преобразования типов')

'''
Это
многострочный
комментарий,
который 
не участвует
в коде

'''