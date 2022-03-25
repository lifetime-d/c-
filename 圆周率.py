import random as r
r.seed(123)
count=0
a = eval(input())
for i in range(a):
    x,y=r.random(),r.random()
    if pow(x**2+y**2,0.5)<=1:
       count+=1
pi=count/a*4
print('{:.6f}'.format(pi))       
