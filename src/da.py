import math
import bisect
prime = [1]

def simpleSieve(limit):
    list1 = [True for i in range(limit + 1)]
    p = 2
    while(p*p<=limit):
        if(list1[p]==True):
            for i in range(p*p, limit+1,p):
                list1[i]=False     
        p+=1
    for p in range(2,limit):
        if list1[p]:
            prime.append(p)

def segmentedSieve(n):
    limit=int(math.floor(math.sqrt(n)) + 1)
    simpleSieve(limit)
    low=limit
    high=limit*2
    while low<n:
        if high>=n:
            high=n
        list1=[True for i in range(limit + 1)]
        for i in range(len(prime)):
            loLim=int(math.floor(low/prime[i])*prime[i])
            if loLim<low:
                loLim+=prime[i]
            
            for j in range(loLim,high,prime[i]):
                list1[j-low]=False
        low=low+limit
        high=high+limit
segmentedSieve(10**7)
m=[]

for i in range(len(prime)-1):
    m.append(prime[i]*prime[i+1])
for j in range(int(input())):
    z=int(input())
    print("Case #",end="")
    print(j+1,end="")
    print(": ",end="")
    k=bisect.bisect_right(m,z)
    if(k>=len(m)):
        print(m[len(m)-1])
        continue
    if(m[k]==z):
        print(m[k])
    else:
        print(m[k-1])
    