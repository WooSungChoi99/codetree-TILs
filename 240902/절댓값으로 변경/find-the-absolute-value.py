n = int(input())
list1 = list(map(int, input().split()))

def change_list(any_list) :
    for i in range(len(any_list)) :
        if any_list[i] < 0 :
            any_list[i] = -any_list[i]

change_list(list1)

for elem in list1 :
    print(elem, end = " ")