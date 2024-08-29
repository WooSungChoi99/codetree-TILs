a, b = tuple(map(int, input().split()))

def is_prime_number(num) :
    if num == 1 :
        return False

    for i in range(2, num) :
        if num%i==0 :
            return False

    return True

ans = 0
for num in range(a, b+1) :
    if is_prime_number(num) :
        ans += num

print(ans)