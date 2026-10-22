n=int(input())
l=int(input())
r=int(input())
arr=[]
dopamine=0
dop=[]
for i in range(n):
    ele=int(input())
    arr.append(ele)

for i in arr:
    if i in range(l,r+1):
        dopamine+=1
        dop.append(dopamine)
    else:
        dopamine-=1
        dop.append(dopamine)
print(max(dop),min(dop))
        
    
