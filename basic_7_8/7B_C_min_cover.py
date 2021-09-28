# C_min_cover
# На прямой задано некоторое множество отрезков с целочисленными координатами концов [Li, Ri].
# Выберите среди данного множества подмножество отрезков, целиком покрывающее отрезок [0, M],
# (M — натуральное число), содержащее наименьшее число отрезков.
#
# Формат ввода
# В первой строке указана константа M (1 ≤ M ≤ 5000). В каждой последующей строке записана
# пара чисел Li и Ri (Li, Ri ≤ 50000), задающая координаты левого и правого концов отрезков.
# Список завершается парой нулей. Общее число отрезков не превышает 100 000.
#
# Формат вывода
# В первой строке выходного файла выведите минимальное число отрезков, необходимое для
# покрытия отрезка [0; M]. Далее выведите список покрывающего подмножества, упорядоченный по
# возрастанию координат левых концов отрезков. Список отрезков выводится в том же формате,
# что и во входe. Завершающие два нуля выводить не нужно. Если покрытие отрезка [0, M]
# исходным множеством отрезков [Li, Ri] невозможно,
# то следует вывести единственную фразу “No solution”.
