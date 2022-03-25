import random
a=1
while a<100: 
    人=int(input('请选择：[0:石头 1:剪刀 2:布]'))
    计算机=random.randint(0,2)
    if 人==0 or 人==1 or 人==2:
        print(计算机)
    else:
         print('please input 0,1 or 2')
    if 人==0 and 计算机==1:
        print('you win!')
    elif 人==0 and 计算机==0:
        print('you win but not overall')
    elif 人==0 and 计算机==2:
        print('you are the loser')
    elif 人==1 and 计算机==0:    
        print('you are the loser')
    elif 人==1 and 计算机==1:
        print('you win but not overall')
    elif 人==1 and 计算机==2:
        print('you win!')
    elif 人==2 and 计算机==0:    
        print('you win!')
    elif 人==2 and 计算机==1:    
        print('you are the loser')
    elif 人==2 and 计算机==2:
        print('you win but not overall')
    else:
        continue
    你=input('go on？')
    if 你=='no!': 
            break   