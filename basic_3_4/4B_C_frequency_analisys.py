# Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
# Слова должны быть отсортированы по убыванию их количества появления в тексте, а при
# одинаковой частоте появления — в лексикографическом порядке.
# Указание.
# После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте
# встречаемости слова. Желаемого можно добиться, если создать список, элементами которого
# будут кортежи из двух элементов: частота встречаемости слова и само слово. Например,
# [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет сортировать
# список кортежей, при этом кортежи сравниваются по первому элементу, а если они равны —
# то по второму. Это почти то, что требуется в задаче.
# Формат ввода
# Вводится текст.
# Формат вывода
# Выведите ответ на задачу.

def dict_from_text(filename='input.txt'):
    words = {}
    with open(filename) as f:
        for line in f:
            line_words = line.strip().split()
            for word in line_words:
                if word not in words:
                    words[word] = 0
                words[word] += 1
    return words

def list_from_dict(words):
    ans = []
    for word in words:
        ans.append((words[word], word))
    return sorted(ans, reverse=True)

frequency_dict = dict_from_text()
sorted_list = list_from_dict(frequency_dict)

for word in sorted_list:
    print(str(word[0]) + ' ' + word[1])

'''
input----------------------------
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme
output-----------------------------

damme
is
name
van
bond
claude
hi
my
james
jean
what
your


input---------------------------------
oh you touch my tralala
mmm my ding ding dong

output--------------------------------
ding
my
dong
mmm
oh
touch
tralala
you

input--------------------------------
ai ai ai ai ai ai ai ai ai ai

output-------------------------------
ai

'''