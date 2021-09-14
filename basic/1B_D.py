# В деревне Интернетовка все дома расположены вдоль одной улицы
# по одну сторону от нее. По другую сторону от этой улицы пока
# ничего нет, но скоро все будет – школы, магазины, кинотеатры и т.д.
# Для начала в этой деревне решили построить школу. Место для
# строительства школы решили выбрать так, чтобы суммарное
# расстояние, которое проезжают ученики от своих домов до школы,
# было минимально.
# План деревни можно представить в виде прямой, в некоторых
# целочисленных точках которой находятся дома учеников. Школу также
# разрешается строить только в целочисленной точке этой прямой
# (в том числе разрешается строить школу в точке, где расположен
# один из домов – ведь школа будет расположена с другой стороны улицы).
#
# Напишите программу, которая по известным координатам домов
# учеников поможет определить координаты места строительства школы.
#
# Формат ввода
# Сначала вводится число N — количество учеников (0 < N < 100001).
# Далее идут в строго возрастающем порядке координаты домов учеников
# — целые числа, не превосходящие 2x10^9 по модулю.
#
# Формат вывода
# Выведите одно целое число — координату точки, в которой лучше
# всего построить школу. Если ответов несколько, выведите любой
# из них.

N = int(input())
a = list(map(int, input().strip().split()))[:N]
# мое решение:
if N <= 2:
    print(a[0])
else:
    print(a[N // 2])
# Сложно было составить решение в голове


