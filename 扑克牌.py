import os
import random as r
suits=[3,4,5,6]
faces=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
deck=[]
for i in range(4):
    for j in range(13):
        deck +=[str(chr(suits[i]))+faces[j]]
r.shuffle(deck)
for i in range(52):
    print(deck[i],end='')
    if (i+1)%13==0:
        print('')


os.system('pause')