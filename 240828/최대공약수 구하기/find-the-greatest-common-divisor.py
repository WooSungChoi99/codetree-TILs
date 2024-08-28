def max_corr(n, m) :
    max_corr = 1
    for num in range(1, min(n, m)+1) :
        if n%num == 0 and m%num == 0 :
            max_corr = num
    return max_corr

n, m = tuple(map(int, input().split()))

print(max_corr(n, m))