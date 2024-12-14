n = int(input())

arr = []

def push_back(n):
    arr.append(n)

def pop_back():
    del arr[-1]

def size():
    print(len(arr))

def get(k):
    print(arr[k-1])

for _ in range(n):
    cmd = input()
    
    if cmd.startswith("push_back"):
        num = int(cmd.split()[1])
        push_back(num)

    elif cmd.startswith("get"):
        num = int(cmd.split()[1])
        get(num)

    elif cmd.startswith("pop_back"):
        pop_back()

    elif cmd.startswith("size"):
        size()
