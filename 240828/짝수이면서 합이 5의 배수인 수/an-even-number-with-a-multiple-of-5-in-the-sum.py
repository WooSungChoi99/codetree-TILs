def is_magic_number(n) :
    first_digit = n // 10
    second_digit = n % 10
    if n%2==0 and (first_digit+second_digit)%5==0 :
        return True
    return False

n = int(input())

if is_magic_number(n) :
    print("Yes")
else :
    print("No")

# n = int(input())

# def dist_num(n) :
#     if n % 2 == 0 :
#         a = str(n)[0]
#         b = str(n)[1]
#         if (int(a) + int(b)) % 5 == 0 :
#             return True


# if dist_num(n) :
#     print("Yes")
# else :
#     print("No")