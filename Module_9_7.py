# Домашнее задание по теме "Декораторы"
# ***************************************************************************************
# Задание:
# Напишите 2 функции:
#   - Функция, которая складывает 3 числа (sum_three)
#   - Функция декоратор (is_prime), которая распечатывает "Простое", если результат
#     1ой функции будет простым числом и "Составное" в противном случае.
#
#   Пример:
#       result = sum_three(2, 3, 6)
#       print(result)
# ****************************************************************************************

def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 1:
            print("Единица")
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