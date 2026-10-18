'''
1 for snake 
-1 for water
0 for gun
'''
import random

computer = random.choice([-1, 0, 1])
yourstr = input("Enter your choice:")
yourDic = {"s":1 , "w":-1 , "g":0}

you = yourDic[yourstr]
reverseDic = {1:"snake", 0:"gun", -1:"water"}

print(f"you chose {reverseDic[you]} \ncomputer chose {reverseDic[computer]}")

if(computer == you):
    print("tie")

else:
    if(computer == -1 and you == 0):
        print("you lose")

    elif(computer == -1 and you == 1):
        print("you win")

    elif(computer == 1 and you == -1):
        print("you lose")

    elif(computer == 1 and you == 0):
        print("you win")

    elif(computer == 0 and you == 1):
        print("you lose")

    elif(computer == 0 and you == -1):
        print("you win")
    


   

    

    
     




