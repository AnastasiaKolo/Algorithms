# задача про кондиционер

troom, tcond = map(int, input().split())
mode = input()
result = troom
if mode == 'freeze':
    result = min(troom, tcond)
elif mode == 'heat':
    result = max(troom, tcond)
elif mode == 'fan':
    result = troom
elif mode == 'auto':
    result = tcond

print(result)
