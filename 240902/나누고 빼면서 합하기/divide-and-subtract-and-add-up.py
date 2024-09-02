n, m = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

def add_num(n, m, arr) :
    ans = 0
    while m >= 1 :
        ans += arr[m-1]
        if m % 2 == 0:
            m //= 2
        else :
            m -= 1
    
    return ans

answer = add_num(n, m, arr)

print(answer)