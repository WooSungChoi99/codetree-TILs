a, b = tuple(map(int, input().split()))

def complete_num(a, b) :
    count = 0
    for n in range(a, b+1) :
        if n % 2 == 0 :
            continue
        elif n % 10 == 5 :
            continue
        elif n % 3 == 0 and n % 9 != 0 :
            continue
        else :
            count += 1
    return count


print(complete_num(a, b))