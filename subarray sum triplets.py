n=int(input())
arr=[]
for i in range(n):
    ele=int(input())
    arr.append(ele)

count=0
for i in range(n-2):
    if(arr[i]+arr[i+2]==arr[i+1]):
        count+=1

print(count)
