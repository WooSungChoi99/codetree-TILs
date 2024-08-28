def make_ones_square(n, m) :
    for _ in range(n) :
        print("1" * m)


n, m = tuple(map(int, input().split()))
make_ones_square(n, m)