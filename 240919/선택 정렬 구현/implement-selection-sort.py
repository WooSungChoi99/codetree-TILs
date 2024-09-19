n = int(input())
arr = list(map(int, input().split()))

for i in range(n-1):
    min_idx = i
    for j in range(i, n-1):
        if arr[min_idx] > arr[j]:
            min_idx = j
    # arr[min_idx], arr[i] = arr[i], arr[min_idx]
    tmp = arr[min_idx]
    arr[min_idx] = arr[i]
    arr[i] = tmp

for num in arr:
    print(num, end=" ")