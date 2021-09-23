# Статья 83 закона “О выборах депутатов Государственной Думы Федерального Собрания Российской Федерации”
# определяет следующий алгоритм пропорционального распределения мест в парламенте.
#
# Необходимо распределить 450 мест между партиями, участвовавших в выборах.
# Сначала подсчитывается сумма голосов избирателей, поданных за каждую партию и
# подсчитывается сумма голосов, поданных за все партии. Эта сумма делится на 450,
# получается величина, называемая “первое избирательное частное” (смысл первого
# избирательного частного - это количество голосов избирателей, которое необходимо
# набрать для получения одного места в парламенте).
#
# Далее каждая партия получает столько мест в парламенте, чему равна целая часть от деления
# числа голосов за данную партию на первое избирательное частное.
#
# Если после первого раунда распределения мест сумма количества мест, отданных партиям, меньше
# 450, то оставшиеся места передаются по одному партиям, в порядке убывания дробной части
# частного от деления числа голосов за данную партию на первое избирательное частное.
# Если же для двух партий эти дробные части равны, то преимущество отдается той партии,
# которая получила большее число голосов.
#
# Формат ввода
# На вход программе подается список партий, участвовавших в выборах. Каждая строка входного
# файла содержит название партии (строка, возможно, содержащая пробелы), затем, через пробел,
# количество голосов, полученных данной партией – число, не превосходящее 108.
#
# Формат вывода
# Программа должна вывести названия всех партий и количество голосов в парламенте, полученных
# данной партией. Названия необходимо выводить в том же порядке, в котором они шли во входных данных.

### я не поняла условие, как рассчитывается в крайних случаях (например сумма голосов меньше 450) ###
# не учла изначально что деление вещественное
def elections_from_text(filename='input.txt'):
    votes = {}
    with open(filename) as f:
        for line in f:
            party, _, line_votes = line.strip().rpartition(' ')
            if party not in votes:
                votes[party] = 0
            votes[party] += int(line_votes)
    return votes

def count_seats(votes):
    parliament_seats_remainder = []
    parliament_seats_dict = {}
    sum_votes = sum(votes.values())
    quotient = sum_votes / 450
    free_seats = 450
    for vote in votes.keys():
        remainder = votes[vote] % quotient
        current_seats = votes[vote] // quotient
        parliament_seats_remainder.append((vote, remainder, votes[vote]))
        parliament_seats_dict[vote] = int(current_seats)
        free_seats -= current_seats
    parliament_seats_remainder.sort(key=lambda x: (-x[1], -x[2]))
    for i in range(int(free_seats)):
        parliament_seats_dict[parliament_seats_remainder[i][0]] += 1
    return parliament_seats_dict


votes = elections_from_text()
parliament_seats = count_seats(votes)
for party in votes.keys():
    print(party, str(parliament_seats[party]))

'''
WA
Party number one 1
Partytwo 500


input
Party One 100000
Party Two 200000
Party Three 400000

output
Party One 64
Party Two 129
Party Three 257

input
Party number one 100
Partytwo 100

output
Party number one 225
Partytwo 225

input
Party number one 449
Partytwo 1

output
Party number one 449
Partytwo 1


не хватает теста на проверку условия "Если же для двух партий эти дробные части равны, 
то преимущество отдается той партии, которая получила большее число голосов".
Я нашёл подходящие входные данные, например ['a 12', 'b 5', 'c 43'], результатом 
должно быть ['a 90', 'b 37', 'c 323']


test 7
Party 1 34523
Party 2 65434
Party 3 453
Party 4 65784
Party 5 5253
Party 6 3568
Party 7 0
Party 8 1
Party 9 4592
Party 10 90389
'''