N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = ''
for i in A:
    if i < X:
        ans += f"{i} "
print(ans)