n=int(input())
arr=[]
for i in range(n):
    ele=int(input())
    arr.append(ele)
result=[]
for i in range(n):
    if (arr[(i-1+n)%n] > arr[i] and arr[(i+1)%n] > arr[i]):
        result.append(2)
    elif(arr[(i-1+n)%n] > arr[i] or arr[(i+1)%n] > arr[i]):
        result.append(1)
    else:
        result.append(0)
print(result)
