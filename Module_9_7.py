# Домашнее задание по теме "Генераторы"
# ***************************************************************************************
# Задача:
# Напишите функцию-генератор all_variants(text), которая принимает строку text
# и возвращает объект-генератор, при каждой итерации которого будет возвращаться
# подпоследовательности переданной строки.
#
# Пункты задачи:
#   -Напишите функцию-генератор all_variants(text).
#   -Опишите логику работы внутри функции all_variants.
#   -Вызовите функцию all_variants и выполните итерации.
# ****************************************************************************************


def sum_three(a, b, c):
    return a + b + c

def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result <= 1:
            print("Составное")
            return result
        for i in range(2, int(result**0.5) + 1):
            if result % i == 0:
                print("Составное")
                return result
        print("Простое")
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


def start():
    result = sum_three(2, 3, 6)
    print(result)  # выведет: Простое

if __name__ == '__main__':
    start()