import random
#Required names
names = ["Inky","Polly","Pinky"]
z=random.choice(names)
#initialize variables
your_points=0
random_player_points=0

while True:
    z=random.choice(names)
    print('Inky,','Polly,','Pinky')
    x=input("Enter your choice above list :")
    if x not in names:
        print("invalid name try again")
        continue
    if(z==x):
        print("Game is tie select another name")
    elif(x=="Inky" and z=="Polly"):
        print("you win and random player lost")
        your_points+=1
    elif(x=="Pinky" and z=="Inky"):
        print("you win and random player lost")
        your_points+=1
    elif(x=="Polly" and z=="Pinky"):
        print("you win and random player lost")
        your_points+=1
    else:
        print("random player win and you lost")
        random_player_points+=1

    answer=input("Do you want to play again(YES/NO):")
    if answer.upper()=="YES":
        continue

    elif answer.upper()=="NO":
        print("The game is over")
        break
    else:print("your answer is incorrect")
    break

print("your points:",your_points)
print("random player points:",random_player_points)
    
if your_points > random_player_points:
    print("congratulations!,you win the game")
elif random_player_points > your_points:
    print("congratulations!,random player win the game")
else:
    print("The game is tie")
        
