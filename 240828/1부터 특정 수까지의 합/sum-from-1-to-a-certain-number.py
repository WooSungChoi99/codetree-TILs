def sum_and_div(N) :
    sum = 0
    for num in range(1, N+1) :
        sum += num
    ans = sum // 10
    return ans

N = int(input())

print(sum_and_div(N))

# def num_sum_div(N) :
#     num_sum = 0
#     for i in range(1, N+1) :
#         num_sum += i
#     return num_sum // 10


# N = int(input())

# print(num_sum_div(N))