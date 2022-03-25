f=input('What is the temperature?')
n=eval(f[0:-1])
if 'C'in f:
    print('The converted temperature is {}F'.format(int(n*1.8+32)))
elif 'F'in f:
    print('The converted temperature is {}C'.format(int((n-32)/1.8)))