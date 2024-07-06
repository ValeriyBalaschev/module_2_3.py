# module_2_3.py Домашняя работа по уроку "Стиль кода часть II. Цикл While."
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_index = 0
my_list_of_positive_numbers = []
while list_index < len(my_list):
    if my_list[list_index] == 0:
        list_index = list_index + 1
        continue
    if my_list[list_index] > 0:
        my_list_of_positive_numbers.append(my_list[list_index])
        list_index = list_index + 1
        continue
    if my_list[list_index] < 0:
        break
    list_index = list_index + 1
print(my_list_of_positive_numbers)
