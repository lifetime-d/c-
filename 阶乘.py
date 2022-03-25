def jie(n):
    if n == 1:
        return 1
    else:
        return n*jie(n-1)
n = int(input())
sum = 0
if n < 1 or n > 40:
    print("请重新输入数据")
else:
    for i in range(1,n+1):
        sum = sum + jie(i)
    print(sum)