str1 = input()

def diff_alphabet_num(str1) :
    diff_num = 0
    for i in range(len(str1)) :
        cnt = 0
        for j in range(len(str1)) :
            if str1[i] == str1[j] :
                cnt += 1
        if cnt == 1 :
            diff_num += 1

    return diff_num

if diff_alphabet_num(str1) >= 2 :
    print("Yes")
else :
    print("No")