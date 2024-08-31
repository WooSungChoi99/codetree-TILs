n = int(input())
_list = list(map(int, input().split()))

def change_list(n, _list) :
    for i in range(n) :
        if _list[i]%2==0 :
            _list[i]//=2

change_list(n, _list)

for elem in _list :
    print(elem, end = " ")