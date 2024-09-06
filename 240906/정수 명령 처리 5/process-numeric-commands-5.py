n = int(input())

arr = []

for _ in range(n) :
    order = input()

    if order != "size" and order != "pop_back" :
        order, num = order.split()
        num = int(num)

    if order == "push_back" :
        arr.append(num)
    elif order == "pop_back" :
        arr.pop()
    elif order == "size" :
        print(len(arr))
    elif order == "get" :
        print(arr[num-1])