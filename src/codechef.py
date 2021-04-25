n, k = map(int, input().split()) 
a = list(map(int, input().split())) 
a.sort(reverse=True) 
prime = int(1e9 + 7) 
d = {} 
for i in a: 
    if i in d: 
        d[i] += 1 
    else: 
        d[i] = 1 
ans = 1 
for i in d: 
    ans = (ans * d[i]) % prime 
print(ans)