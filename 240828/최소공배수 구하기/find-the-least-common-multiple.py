n, m = tuple(map(int, input().split()))

def max_corr(n, m) :
    for num in range (max(n, m), (n*m)+1) :
        if num % min(n, m) == 0 and num % max(n, m) == 0 :
            max_corr_num = num
            break

    print(max_corr_num)

max_corr(n, m)

# def min_mult_num(n, m) :
#     min_mult_num = n*m
#     for num in range(1, max(n, m)) :
#         if (min(n, m)*num)%max(n, m)==0 :
#             min_mult_num = min(n, m)*num
#             return min_mult_num
#     return min_mult_num

# n, m = tuple(map(int, input().split()))

# print(min_mult_num(n, m))