a=0
b=0
c=0
d=1
sum=0
while d==1:
    e=int(input())
    if e>0:
        a+=1
    elif e<0:
        b+=1
    else:
        break
    sum+=e
print(sum/(a+b))
print(a)
print(b)    