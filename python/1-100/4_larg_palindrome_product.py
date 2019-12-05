# Задача 4. Наибольшее произведение-палиндром.
#
# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
#
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
#


def is_palindrom(num):
    '''Функция, которая определяет, является ли число палиндромом

    Принимает на вход число, и проверяет каждую цифру с её зеркальным отображением с конца
    Возвращает булевое значение'''
    palindrom = list(str(num)) # преобразуем число в массив цифр
    if palindrom == palindrom[::-1]:
        return True
    return False


def search_palindrom_3_digit():
    '''Функция, которая находит палиндром в произведениях 3-х значных чисел

    На вход ничего не принимает, находит палиндром путем наивного перебериная чисел от 999 до 100
    Возвращает число'''
    max = 0 # обозначаем максимальное число, пока это 0
    a = 999 # обозначаем верхние границы, до скольки нужно перебирать
    b = 999

    for j in range(a, 99, -1): # запускаем алгоритмы перебора для первого и второго числа
        for i in range(b, 99, -1):
            c = j * i # находим их произведение и присваиваем это переменной с
            if c > max and is_palindrom(c): # проверяем, чтобы оно было больше числа которое уже нашли, а также являлось палиндромом
                max = c # если условия соблюдены, то присваиваем новое значение
    return max


print('Самый большой палиндром, полученный умножением двух трехзначных чисел является: {}'.format(search_palindrom_3_digit())) # выводим на экран
