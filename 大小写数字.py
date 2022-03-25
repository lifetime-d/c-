a=input()
upper,lower,n=0,0,0
for i in a:
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1
    elif i.isdigit():
        n+=1
print(upper)
print(lower)
print(n)