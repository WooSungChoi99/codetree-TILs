max_digit = 10
max_k = 6

n =  int(input())
arr = list(map(int, input().split()))

def radix_sort():
    global arr

    p = 1
    for pos in range(max_k):
        arr_new = [[] for _ in range(max_digit)]
        for elem in arr:
            digit = (elem // p) % 10
            arr_new[digit].append(elem)

        arr = []
        for i in range(max_digit):
            for elem in arr_new[i]:
                arr.append(elem)

        p *= 10

radix_sort()

for elem in arr:
    print(elem, end=" ")