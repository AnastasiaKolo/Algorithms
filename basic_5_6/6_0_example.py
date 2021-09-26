# Бинарный поиск
# левый бин поиск - первое подходящее значение (все плохо -> все хорошо)
# правый бин поиск - последнее подходящее значение (все хорошо -> все плохо)
# Важно
# функция которую проверяем, на нашем интервале только один раз меняет состояние!
#
# Сложность бинпоиска = O(log N)
#
# Проверяем на 2-х элементах, сходится ли поиск. Чтобы не случился вечный цикл
#

def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l


def rbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    return l

# Задача 1
# (есть математическое решение по формуле, но мы решим методом бин поиска)
# В совет школы входят родители, ученики, и учителя. Родителей должно быть не менее 1/3
# от общего числа членов совета. В настоящий момент в совет входит N чел, из
# них К родителей.
# Сколько родителей (М) нужно дополнительно ввести в совет? Деление не использовать
#
# Решим методом бин поиска. L = 0, R = N (если добавим столько же родителей,
# сколько уже есть членов совета, родителей будет >= 1/2)
def checkendowment(m, params):
    n, k = params
    return (k + m) * 3 >= n + m # меняем деление на умножение
# проверка
# n, k = map(int, input().split())
# params = n, k
# m = lbinsearch(0, n, checkendowment, params)
# print(m)

# Задача 2
# Юра готовится к собеседованию. Надо решить N задач
# В 1-й день Юра решил K задач, а затем каждый день на 1 задачу больше
# Определите, сколько дней ушло у Юры на подготовку
def checkproblemcount(days, params):
    n, k = params
    return (k + (k + days - 1)) * days // 2 >= n

## проверка
# n, k = map(int, input().split())
# params = n, k
# m = lbinsearch(0, n, checkproblemcount, params)
# print(m)

# Задача 3
# Доска W * H см. Нужно разместить N квадратных стикеров
# При этом длина стороны стикера в см должна быть целым числом
# Найти максимальную длину стороны стикера

def checkstickercount(side, params):
    n, w, h = params
    return (w // side) * (h // side) >= n
## проверка
# n, w, h = map(int, input().split())
# params = n, w, h
# side = rbinsearch(0, min(w, h), checkstickercount, params)
# print(side)

# Задача 4
# Задана отсортированная по неубыванию последовательность
# из N чисел и число X
# Нужно найти индекс первого числа в последовательности,
# которое больше или равно Х. Если не найдено, вернуть N

def checkisge(index, params):
    seq, x = params
    return seq[index] >= x

def findfirstge(seq, x):
    ans = lbinsearch(0, len(seq) - 1, checkisge, (seq, x))
    if seq[ans] < x:
        return len(seq)
    return ans
# Задача 5
# Задана отсортированная по неубыванию последовательность
# из N чисел и число X
# Нужно сколько раз число Х входит в последовательность.
#
# Решаем двумя бинарными поисками первый >= x, второй > x
def checkisgt(index, params):
    seq, x = params
    return seq[index] > x

def checkisge(index, params):
    seq, x = params
    return seq[index] >= x

def findfirst(seq, x, check):
    ans = lbinsearch(0, len(seq) - 1, check, (seq, x))
    if not check(ans, (seq, x)):
        return len(seq)
    return ans

def countx(seq, x):
    indexgt = findfirst(seq, x, checkisgt)
    indexge = findfirst(seq, x, checkisge)
    return indexgt - indexge

# Задача 6
# Задана % ставка по кредиту (Х% годовых)
# срок кредитования N мес. M - сумма кредита
# Рассчитать размер аннуитетного ежемесячного платежа
#
# У нас две подзадачи
# - рассчитать ежемесячный процент (он не равен X/12!)
#

def checkmonthlyperc(mperc, yperc):
    msum = 1 + mperc / 100
    ysum = 1 + yperc / 100
    return msum ** 12 >= ysum

def fbinsearch(l, r, eps, check, checkparams):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, checkparams):
            r = m
        else:
            l = m
    return l
# Далее перебираем сумму платежа бинпоиском
# в качестве проверки моделировать процесс ежемесячной выплаты
# уменьшая тело кредита на разницу между суммой платежа и ежемесячным процентом
def checkcredit(mpay, params):
    periods, creditsum, mperc = params
    for i in range(periods):
        percpay = creditsum * (mperc / 100)
        creditsum -= mpay - percpay
    return  creditsum <= 0


# # проверка
# x = 6
# eps1 = 0.0001
# eps2 = 0.01
# m = 10000000
# n = 300
# mperc = fbinsearch(0, x, eps1, checkmonthlyperc, x)
# monthlypay = fbinsearch(0, m, eps2, checkcredit, (n, m, mperc))
# print(mperc)
# print(monthlypay)
# print(n / 12)

# Тернарный поиск
# N велосипедистов, участвующие в шоссейной гонке, в нек. момент времени оказались в точках
# удаленных от места старта на x1 x2 ..xn метров
# Каждый велосипедист двигается с постоянной скоростью v1, v2,... vn м/с
# Определить момент времени в гонке в которой расстояние между первым и последним
# станет минимальным
#
# Решение
# Определим ф-ю dist(t) которая будет за O(N) определять
# расст между лидером и замыкающим в момент времени t.
# Если dist(t + eps) > dist(t), то ф-я растет и надо сдвинуть
# левую груницу поиска. Иначе - правую

def dist(t, params):
    x, v = params
    minpos = maxpos = x[0] + v[0] * t
    for i in range(1, len(x)):
        nowpos = x[i] + v[i] * t
        minpos = min(minpos, nowpos)
        maxpos = max(maxpos, nowpos)
    val = maxpos - minpos
    return val

def checkasc(t, eps, params):
    return dist(t + eps, params) >= dist(t, params)

def fbinsearch1(l, r, eps, check, params):
    while l + eps < r:
        m = (l + r) / 2
        if checkasc(m, eps, params):
            r = m
        else:
            l = m
    return l