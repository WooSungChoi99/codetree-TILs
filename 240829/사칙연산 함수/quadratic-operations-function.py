a, o, c = input().split()
a, c = int(a), int(c)

def plus(a, c) :
    return a + c
def minus(a, c) :
    return a - c
def multiply(a, c) :
    return a * c
def divide(a, c) :
    return int(a / c)

if o == "+" :
    print(f'{a} {o} {c} = {plus(a, c)}')
elif o == "-" :
    print(f'{a} {o} {c} = {minus(a, c)}')
elif o == "*" :
    print(f'{a} {o} {c} = {multiply(a, c)}')
elif o == "/" :
    print(f'{a} {o} {c} = {divide(a, c)}')
else :
    print("False")






# a, o, c = input().split()
# a, c = int(a), int(c)


# def arithmetics(a, o, c) :
#     if o == '+' :
#         print(f'{a} {o} {c} = {a+c}') 
#     elif o == '-' :
#         print(f'{a} {o} {c} = {a-c}') 
#     elif o == '/' :
#         print(f'{a} {o} {c} = {int(a/c)}')
#     elif o == '*' :
#         print(f'{a} {o} {c} = {a*c}')
#     else :
#         print('False')


# arithmetics(a, o, c)