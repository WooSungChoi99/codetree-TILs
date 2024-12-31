import sys
INT_MAX = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

min_val = INT_MAX
for i in range(n):
    val = 0
    for j in range(n):
        val += arr[j]*abs(j-i)
    if val < min_val:
        min_val = val

print(min_val)