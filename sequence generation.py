n=int(input())
initial=list(map(int,input().split()))
count=len(initial)
if(count<n):
    for i in range(count,n):
        initial.append(initial[i-2]+initial[i-1])
print(initial)

