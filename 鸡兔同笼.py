a,b=map(int,input().split(' '))
flag=1
for i in range(a+1):
    x = a - i
    if 4*i+2*x==b:
        print(x,i)
        flag=0
if flag:
    print("Data Error!")