# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.


def fill_array(array, txt):
    x_len = int(input(f'Введите кол-во элементов {txt} множества: '))
    while len(array) != x_len:
        array = input(f'Введите {x_len} элемента(-ов) множества через пробел: ').split()
        array = [int(i) for i in array]
    return array

def arange_arrays(array_x, array_y, array_z):
    for i in array_x:
        for j in array_y:
            if i == j:
                array_z.append(i)
    array_z.sort()
    return array_z

list_n = []
list_m = []
list_nm = []
list_n = fill_array(list_n, 'первого')
list_m = fill_array(list_m, 'второго')
list_nm = arange_arrays(list_n, list_m, list_nm)
print(list_nm)
