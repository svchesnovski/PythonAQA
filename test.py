# Урок №5 Условные операторы и циклы
# numbers = []
#
# for i in range(10):
#     if i % 2 == 0:
#         numbers.append(i)
#
# print (numbers)
#
# items = [1, 2, 5, 6, [1, 2, 3], "ABC", 1, True]
# numbers = []
#
# # for i in range(100):
# #     if i % 2:
# #         numbers.append(i)
# #
# # print(numbers)
#
# for item in items:
#     if isinstance(item, int):
#         numbers.append(item)
#
# print(numbers)
#
# numbers_2 = [i for i in range(100) if i % 2 == 0]
#
# print(numbers_2)
#
#
# data = [{"name": "Oksana", "age": 29}, {"name": "Mike", "age": 15}, {"name": "Slava", "age": 30}]
# find_name = input('Введите имя для поиска: ')
# # print(data[0])
#
#
# found = False
#
# for info in data:
#     if info['name'] == find_name:
#         value = input('Введите возраст: ')
#         info['age'] = int(value)
#         print(info)
#         found = True
#         break  # Останавливаем цикл, если нашли
#
# if not found:
#     print('Значение не найдено!')

# Урок №6 Функции
def my_args(*args):
    total = 0
    for i in args:
        total += i

    print(total)

my_args(1, 2, 3, 4, 5, 6, 7, 8, 9)


def my_sum(numbers):
    """
    Функция my_sum принимает список и находит сумму всех элементов списка
    :param numbers: принимает список, например [1, 2, 3, 4, 5]
    :type numbers: list
    :return: возвращает сумму всех элементов списка, в нашем случае 15
    """
    if not isinstance(numbers, list):
        print('Введен некорректный тип данных')
        return None
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
result = my_sum(numbers)
print(result)


def sum_num(a, b):
    return a + b

result = sum_num(1, 4)

print(result)