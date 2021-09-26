# Дано кубическое уравнение ax^3+bx^2+cx+d=0 (a≠0).
# Известно, что у этого уравнения есть ровно один корень.
# Требуется его найти.
#
# Формат ввода
# Во входном файле через пробел записаны четыре целых числа:
# -1000 <=a,b,c,d<=1000
#
# Формат вывода
# Выведите единственный корень уравнения с точностью не менее 5 знаков после десятичной точки.

def check_x3_gt0(x, params):
    a, b, c, d = params
    x3 = a * x ** 3 + b * x ** 2 + c * x + d
    return x3 >= 0

def fbinsearch(l, r, eps, check, checkparams):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, checkparams):
            r = m
        else:
            l = m
    return l

eps= 0.0000001
l = -10000000
r = 10000000
a, b, c, d = map(int, input().split())
# определить возрастает или убывает функция
if a >= 0:
    root3x = fbinsearch(l, r, eps, check_x3_gt0, (a, b, c, d))
else:
    root3x = fbinsearch(l, r, eps, check_x3_gt0, (-a, -b, -c, -d))
print(root3x)

'''
input
1 -3 3 -1
output
1.0000036491

input
-1 -6 -12 -7
output
-1.0000000111


input

output


input

output

'''