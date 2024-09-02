absolute_string = input()
partial_string = input()

def does_contain_partial() :
    a, b = len(absolute_string), len(partial_string)
    for i in range(0, a-b+1) :
        if absolute_string[i:i+b] == partial_string :
            return i

    return -1

ans = does_contain_partial()

print(ans)