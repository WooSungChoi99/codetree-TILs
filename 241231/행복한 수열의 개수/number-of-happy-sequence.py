m, n = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(m)
]

ans = 0
for i in range(m):
    cnt = 1
    for j in range(m-1):
        if arr[i][j] == arr[i][j+1]:
            cnt +=1
        else:
            cnt = 1
        if cnt == n:
            cnt = 1
            ans += 1
            break
    
    for k in range(m-1):
        if arr[k][i] == arr[k+1][i]:
            cnt +=1
        else:
            cnt = 1
        if cnt == n:
            ans += 1
            break

print(ans)