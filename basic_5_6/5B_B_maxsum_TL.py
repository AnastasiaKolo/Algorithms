def countmaxrangesum_nn(nums, n):
    maxrangesum = nums[0]
    for i in range(n):
        rangesum = 0
        for j in range(i, n):
            rangesum += nums[j]
            if rangesum > maxrangesum:
                maxrangesum = rangesum
    return maxrangesum
with open('input.txt') as f:
    print('reading file')
    n = int(f.readline())
    nums = list(map(int, f.readline().split()))
    print('file read successfully')
import time
start_time = time.time()
m = countmaxrangesum_nn(nums, n)

print(m)
print("time elapsed: {:.9f}s".format(time.time() - start_time))

# # подготовка тестового файла с макс кол-вом элементов
# with open('input_long.txt', 'w') as f:
#     line = str(3 * (10 ** 5))
#     f.write(line + '\n')
#     nums = [10 ** 9] * 3 * (10 ** 5)
#     line = ' '.join(str(i) for i in nums)
#     f.write(line + '\n')
