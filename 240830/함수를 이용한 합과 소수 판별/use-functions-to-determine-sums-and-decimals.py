a, b = tuple(map(int, input().split()))

def is_prime_number(num) :
    if num == 1 :
        return False
    for i in range(2, num) :
        if num%i == 0 :
            return False
    return True

def is_sum_even(num) :
    digit_sum = 0
    while num > 0 :
        digit_sum += (num % 10)
        num //= 10
    if digit_sum % 2 == 1 :
        return False
    return True

cnt = 0
for i in range(a, b+1) :
    if is_prime_number(i) and is_sum_even(i) :
        cnt += 1

print(cnt)


# a, b = tuple(map(int, input().split()))


# def prime_number(n) :
#     for i in range(2, n) :
#         if n % i == 0 :
#             return False
#     return True


# def even_sum(n) :
#     if ((n // 10) + (n % 10)) % 2 != 0 :
#         return False
#     return True


# count = 0

# for i in range(a, b+1) :
#     if prime_number(i) and even_sum(i) :
#         count += 1

# print(count)