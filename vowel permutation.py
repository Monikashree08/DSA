s=input()
vowel='aeiouAEIOU'
count=0
fact=1
for ch in s:
    if ch not in vowel:
        count+=1
if count==0:
    print('0')
else:
    for i in range(1,count+1):
       fact*=i
print(fact)
