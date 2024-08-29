def is_prime_number(num) :
    for i in range(2, num) :
        if num%i==0 :
            return False
    return True

a, b = tuple(map(int, input().split()))

ans = 0
for num in range(a, b+1) :
    if num == 1 :
        continue
    if is_prime_number(num) :
        ans += num

print(ans)