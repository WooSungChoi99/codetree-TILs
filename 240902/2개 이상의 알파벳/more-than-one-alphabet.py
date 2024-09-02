str1 = input()

def diff_alphabet_num(str1) :
    arr = []
    for i in range(len(str1)) :
        if str1[i] not in arr :
            arr.append(str1[i])

    return len(arr)

if diff_alphabet_num(str1) >= 2 :
    print("Yes")
else :
    print("No")