
#Write Code Of Game Rock , Paper , Scisssor

import random
userchoice = input("What Do You Choose ? Type 1 For The Rock , 2 For The Paper , 3 For The Scissors \n")
if(userchoice=='1'):
    print("Rock")
if(userchoice=='2'):
    print("Paper")
if(userchoice=='3'):
    print("Scissor")
print("\n")
item=['Rock','Paper','Scissor']
print("\n")
computerchoice=random.choice(item)
print("\n")
print("Computer Choice is : ",computerchoice)
if(userchoice=='1' and computerchoice=='Paper'):
    print("Paper Win!!")
elif(userchoice=='1' and computerchoice=='Scissor'):
    print("Rock Win!!")
elif(userchoice=='2' and computerchoice=='Rock'):
    print("Paper Win!!")
elif(userchoice=='2' and computerchoice=='Scissor'):
    print("Scissor Win!!")
elif(userchoice=='3' and computerchoice=='Rock'):
    print("Rock Win!!")
elif(userchoice=='3' and computerchoice=='Paper'):
    print("Scissor Win!!")
else:
    print("Tie")