n=int(input())
lst=[]
for i in range(n):
    ele=int(input())
    lst.append(ele)
total=sum(lst)
prefix=0
count=0
for i in range(n-1):
    prefix+=lst[i]
    sufix=total-prefix
    diff=abs(sufix-prefix)
    if (diff%2==0):
        count+=1
print(count)
