a, b = tuple(map(int, input().split()))

def follow_order(a, b) :
    if a > b :
        a += 25
        b *= 2
    else :
        a *= 2
        b += 25
    
    return a, b

print(follow_order(a, b)[0], follow_order(a, b)[1])