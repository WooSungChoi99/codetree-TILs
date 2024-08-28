N = int(input())

def make_nums_square(N) :
    num = 1
    for _ in range(N) :
        for _ in range(N) :
            if num == 10 :
                num = 1
            print(num, end = " ")
            num += 1
        print()

make_nums_square(N)