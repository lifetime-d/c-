a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)
d=b**2-4*a*c
if d>=0:
    result1=(-b+pow(b**2-4*a*c, 1/2))/(2*a)
    result2=(-b-pow(b**2-4*a*c, 1/2))/(2*a)
    print('{:0.2f} {:0.2f}'.format(result1,result2))
else:
    print('No')