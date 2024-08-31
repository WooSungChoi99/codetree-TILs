n, m = tuple(map(int, input().split()))

def change_value(num1, num2) :
    num1, num2 = num2, num1
    
    return num1, num2

print(change_value(n, m)[0], change_value(n, m)[1])