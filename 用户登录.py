a=input()
c=3
dic={'aaa':'123456','bbb':'888888','ccc':'333333'}
if a in dic.keys():
    for i in range(3):
        b=input()
        if b==dic.get(a):
            print('Success')
            break
        else:
            c -= 1
            if c != 0:
                print("Fail,{:} Times Left".format(c))
            
        if c==0:
            print('Login Denied')
            break
else:
    print('Wrong User')