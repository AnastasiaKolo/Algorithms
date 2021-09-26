# не забыть отрезать ненужный первый элемент
# решение упирается в time limit
S = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
set_C = set(C[1:])
ans = []
for i in range(1, A[0] + 1):
    for j in range(1, B[0] + 1):
        x = (S - A[i] - B[j])
        if x in set_C:
            ans.append((i - 1, j - 1, C[1:].index(x)))
ans.sort()
if len(ans) > 0:
    print(' '.join(str(i) for i in ans[0]))
else:
    print(-1)