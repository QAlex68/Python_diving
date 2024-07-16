# Задание №6
# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


def my_func(some_list:list[int | float], i_first:int, i_last:int)->int | float:
    """
    :param some_list:
    :param i_first:
    :param i_last:
    :return:
    """
    i_first, i_last = sorted([i_first, i_last])
    i_first = 0 if i_first < 0 else i_first
    i_last = len(some_list) if i_last > len(some_list) else i_last
    my_sum = sum(some_list[i_first:i_last])
    return my_sum


lst = [3, 4, 5, 2, 3, 1, 7, 9, 3]
print(my_func(lst, -5, 3))
#
# lst = [3, 4, 5, 2, 3, 1, 7, 9, 3]
# indeces = [-2, 1]
#
# def sum_by_ind(lst, lst_ind):
#     if lst_ind[0] > lst_ind[1]:
#         lst_ind[0], lst_ind[1] = lst_ind[1], lst_ind[0]
#     sum_ = 0
#     for i, item in enumerate(lst):
#         if lst_ind[0] <= i < lst_ind[1] + 1:
#             sum_ += item
#
#     return sum_
#
# print(*enumerate(lst))
# print(sum(lst))
# print(sum_by_ind(lst, indeces))
