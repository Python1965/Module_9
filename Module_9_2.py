# Домашнее задание по теме "Списковые, словарные сборки"
# ***************************************************************************************
# Задача:
# Даны несколько списков, состоящих из строк
#   first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
#   second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
#
# В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк
#   списка first_strings, при условии, что длина строк не менее 5 символов.
#
# В переменную second_result запишите список созданный при помощи сборки состоящий из
#   пар слов(кортежей) одинаковой длины. Каждое слово из списка first_strings должно сравниваться
#   с каждым из second_strings. (два цикла)
#
# В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение
#   будет строка-длина строки. Значения строк будут перебираться из объединённых вместе
#   списков first_strings и second_strings. Условие записи пары в словарь - чётная длина строки.
# ****************************************************************************************

def start():
    first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
    second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

    first_result = [len(item) for item in first_strings if len(item) >= 5]
    print(first_result)

    second_result = [(first, second)
                     for first in first_strings
                     for second in second_strings
                     if len(first) == len(second)]
    print(second_result)

    third_result = [(string, len(string))
                    for string in first_strings + second_strings
                    if len(string) % 2 == 0]
    print(third_result)


if __name__ == '__main__':
    start()