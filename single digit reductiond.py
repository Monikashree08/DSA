def sum(num):
    strnum=str(num)
    if len(strnum)==1:
        print(num)
    else:
        add=0
        for digit in strnum:
            add+=int(digit)
        sum(add)
num=int(input())
sum(num)
