a, b = tuple(map(int, input().split()))

def change_num(a, b) :
    if a > b :
        a *= 2
        b += 10
    else :
        a += 10
        b *= 2

    return a, b


a, b = change_num(a, b)
print(a, b)