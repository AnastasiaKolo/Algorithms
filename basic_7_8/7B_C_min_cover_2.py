def best_section(point, idx_start, sections):
    i = idx_start
    bestsection = (0, 0)
    maxright = 0
    while (i < len(sections)) and (sections[i][0] <= point): #and (sections[i][1] >= point)
        if sections[i][1] - point > maxright:
            bestsection = sections[i]
            maxright = sections[i][1] - point
        i += 1
    return bestsection

def is_covered_multi(m, sections):
    current_point = 0
    ans = []
    i = 0
    while (current_point <= m) and (i < len(sections)):
        max_right_section = best_section(current_point, i, sections)
        if max_right_section != (0, 0):
            ans.append(max_right_section)
            current_point = max_right_section[1]
        elif max_right_section == (0, 0) and (current_point < m):
            return []
        i += 1
    return ans

with open('input.txt') as f:
    m = int(f.readline())
    sections = []
    eof = False
    while not eof:
        l, r = map(int, f.readline().split())
        if (r > 0) and (l < m):
            sections.append((l, r))
        elif (l, r) == (0, 0):
            eof = True
sections.sort(key=lambda x: (x[0], -x[1]))
ans2 = is_covered_multi(m, sections)
if ans2:
    print(len(ans2))
    for rec in ans2:
        print(str(rec[0]) + ' ' + str(rec[1]))
else:
    print('No solution')

'''
input
500
-1000 13
5000 50000
15 499
13 18
18 500
15 18
-5000 5
-8000 -3
0 0

output
3
-1000 13
13 18
18 500


5000
-50000 4999
0 0

'''