import random
rock='''
    _______
---'   ____
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
 _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
 
combos=[rock,paper,scissors]
user_choice=int(input("Input  \n0 for Rock\n1 for papers\n2 for scessiors  : "))
print(combos[user_choice])
computer_choice=random.randint(0,2)#rock<paper,,paper<scisers,,scissor<rock
print(combos[computer_choice])
if user_choice!=computer_choice:
        if computer_choice==0:
            if user_choice==2:
                print("You lost the Game ")
            if user_choice==1:
                print("You won the game")
        elif computer_choice==1:
            if user_choice==0:
                print("You lost the Game")
            if user_choice==2:
                print("You won the game")

        elif computer_choice==2:
            if user_choice==1:
                print("You lost the Game")
            if user_choice==0:
                print("You won the game")
        else:
            print("Unexpected error happened")
else:

    print("Try Again")
    # rok wins when paper is in
