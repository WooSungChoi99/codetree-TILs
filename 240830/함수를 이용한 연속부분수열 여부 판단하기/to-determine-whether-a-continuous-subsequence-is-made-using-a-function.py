n1, n2 = tuple(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def is_partial(n1, A, n2, B) :
    for i in range(n1-n2+1) :
        if A[i:i+n2] == B :
            return True
    return False

if is_partial(n1, A, n2,  B) :
    print("Yes")
else :
    print("No")

# a, b = tuple(map(int, input().split()))
# list_a = list(map(int, input().split()))
# list_b = list(map(int, input().split()))


# def continuous_partial_sequence(a, b, list_a, list_b) :
#     for i in range(a) :
#         if list_b[0] == list_a[i] :
#             if list_b == list_a[i:i+b] :
#                 return True
#     return False


# if continuous_partial_sequence(a, b, list_a, list_b) :
#     print("Yes")
# else :
#     print("No")