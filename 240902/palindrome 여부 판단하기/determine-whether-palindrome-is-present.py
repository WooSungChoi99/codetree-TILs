str1 = input()

def change_order(any_string) :
    str2 = ""
    for i in range(-1, -(len(any_string)+1), -1) :
        str2 += any_string[i]

    return str2

print("Yes") if str1 == change_order(str1) else print("No")