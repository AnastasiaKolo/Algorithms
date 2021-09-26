

def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

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

def getidx(seq, x):
    indexgt = findfirst(seq, x, checkisgt)
    indexge = findfirst(seq, x, checkisge)
    return indexgt, indexge

## проверка
with open('input.txt') as f:
    n = int(f.readline())
    nums = list(map(int, f.readline().split()))
    m = int(f.readline())
    reqs = list(map(int, f.readline().split()))

ans = []
for req in reqs:
    l, r = getidx(nums, req)
    if l == len(nums):
        ans.append((0, 0))
    else:
        ans.append((l + 1, r))
print('\n'.join(str(x) + ' ' + str(y) for (x, y) in ans))

'''
input
4
1 2 2 3
4
4 3 2 1

output
0 0
4 4
2 3
1 1

input
10
1 2 3 4 5 6 7 7 8 9
10
7 3 3 1 3 7 9 7 7 10

output
7 8
3 3
3 3
1 1
3 3
7 8
10 10
7 8
7 8
0 0

input
10
1 3 3 3 3 6 8 8 9 10
10
2 9 6 4 2 9 3 7 9 7
x     x 
output
0 0
9 9
6 6
0 0
0 0
9 9
2 5
0 0
9 9
0 0

'''