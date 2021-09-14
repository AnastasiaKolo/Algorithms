# Последовательность состоит из натуральных чисел и завершается
# числом 0. Всего вводится не более 10000 чисел (не считая
# завершающего числа 0). Определите, сколько элементов этой
# последовательности равны ее наибольшему элементу.
#
# Числа, следующие за числом 0, считывать не нужно.
#
# Формат ввода
# Вводится последовательность целых чисел, оканчивающаяся числом 0
# (само число 0 в последовательность не входит).
# Формат вывода
# Выведите ответ на задачу.
finished = False
curr_max = 0
count_max = 0
while not finished:
    curr = int(input())
    if curr > 0:
        if curr_max < curr:
            curr_max = curr
            count_max = 1
        elif curr_max == curr:
            count_max += 1
    else:
        finished = True
print(count_max)