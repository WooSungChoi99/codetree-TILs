n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def interval_sum(a1, a2) :
    global arr
    sum_val = 0
    for num in range(a1-1, a2) :
        sum_val += arr[num]

    return sum_val

for _ in range(m) :
    a1, a2 = tuple(map(int, input().split()))
    ans = interval_sum(a1, a2)
    
    print(ans)