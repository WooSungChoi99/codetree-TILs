a, b = tuple(map(int, input().split()))

def power_num(a, b) :
    cnt = 1
    for _ in range(b) :
        cnt *= a
    return cnt


print(power_num(a, b))