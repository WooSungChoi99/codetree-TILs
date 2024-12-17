# n = int(input())
# arr = list(map(int, input().split()))

# for i in range(n-1):
#     min_idx = i
#     for j in range(i+1, n):
#         if arr[min_idx] > arr[j]:
#             min_idx = j
#     # arr[min_idx], arr[i] = arr[i], arr[min_idx]
#     tmp = arr[min_idx]
#     arr[min_idx] = arr[i]
#     arr[i] = tmp

# for num in arr:
#     print(num, end=" ")

n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)-1):
    min = i
    for j in range(i, len(arr)-1):
        if arr[j+1]<arr[min]:
            min = j+1
    
    tmp = arr[i]
    arr[i] = arr[min]
    arr[min] = tmp

for num in arr:
    print(num, end=" ")