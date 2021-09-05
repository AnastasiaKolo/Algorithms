# Как известно, два наиболее распространённых формата записи
# даты — это европейский (сначала день, потом месяц, потом год)
# и американски (сначала месяц, потом день, потом год).
# Системный администратор поменял дату на одном из бэкапов
# и сейчас хочет вернуть дату обратно. Но он не проверил,
# в каком формате дата используется в системе.
# Может ли он обойтись без этой информации?
# Иначе говоря, вам даётся запись некоторой корректной даты.
# Требуется выяснить, однозначно ли по этой записи определяется
# дата даже без дополнительной информации о формате.
#
# Формат ввода
# Первая строка входных данных содержит три целых числа —
# x, y и z (1≤x≤31, 1≤y≤31, 1970≤z≤2069.
# Гарантируется, что хотя бы в одном формате запись x y z
#  задаёт корректную дату.
# Формат вывода
# Выведите 1, если дата определяется однозначно,
# и 0 в противном случае.

from datetime import datetime, timedelta


def date_range(str_date, numdays, date_format="%m-%d-%Y"):
    start_date = datetime.strptime(str(str_date), date_format)
    date_list = []
    for x in range(numdays):
        date_list.append((start_date + timedelta(days=x)).strftime("%m %d %Y"))
    return date_list

def convert_date(str_date, date_format="%d %m %Y"):
#     "%m %d %Y" => "%d %m %Y"
    try:
        converted = datetime.strptime(str(str_date), date_format)
    except ValueError:
        return 'not converted', 1
    return converted.strftime("%d %m %Y"), 0

def check_date(date_str):
    x, y, z = map(int, date_str.split())
    if (x > 12) or (y > 12) or (x == y):
        return 1
    else:
        return 0


a = date_range('1-1-1980', 366, date_format="%m-%d-%Y")
for i in range(len(a)):
    b = check_date(a[i])
    d, c = convert_date(a[i])
    if b != c:
        print('{}: {} : {}, {}'.format(a[i], b, c, d))

# Сначала не учла что даты типа 1 1 1980 дают однозначачную дату при перестановке d m


