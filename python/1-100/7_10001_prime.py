# Задача 7. 10001-ое простое число
#
# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
#
# Какое число является 10001-ым простым числом?
#


def is_prime(num):
    '''Функция определения простого числа

    Принимает на вход число, и проверяя его нечетность, путем перебора проверят все значени до квадратного корня этого числа. Скорость алгоритма О(n ** 0.5).
    Возвращает булевое значение.'''
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num


def prime_numb(num):
    '''Функция поиска n-го простого числа

    Путем перебора и проверки ищет простое n-ое число
    Возвращает число.'''
    count = 0 # счетчик простых чисел
    prime_num = 1 # стартовое простое число
    while count != num: # цикл поиска n-го числа по нечетным числам
        if is_prime(prime_num):
            count += 1
            prime_num += 2
        else:
            prime_num += 2
    return prime_num - 2 #возвращаем предыдуще число


num = 10001

print('{0}-ым простым число являеться: {1}'.format(num, prime_numb(num)))
