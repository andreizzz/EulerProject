# Задача 3.Наибольший простой делитель
#
# Простые делители числа 13195 - это 5, 7, 13 и 29.
#
# Каков самый большой делитель числа 600851475143, являющийся простым числом?
#

def isPrime(num):
    if num % 2 == 0:
        return num == 2
   d = 3
   while d * d <= num and num % d != 0:
       d += 2
   return d * d > num


def larg_prime_fact(num):
    factors = [] #массив множителй пока пуст
    product = 1 #произведение чисел равно 1
    while product == num:
        for i in range(1, num):
            if i:
                pass
