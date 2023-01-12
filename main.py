import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
player_choice =  int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor\n"))
ascii_art = [rock,paper,scissors]
computer_choice = random.randint(0,2)
print("Player:\n" + ascii_art[player_choice] + "            vs            \nComputer:\n" + ascii_art[computer_choice])


if player_choice == computer_choice:
    print ('TIE')
elif (player_choice ==0 and computer_choice==1) \
        or (player_choice ==1 and computer_choice==2)\
        or (player_choice ==2 and computer_choice==0):
    print ('PLAYER LOSES')
elif (player_choice ==1 and computer_choice==0) \
        or (player_choice ==2 and computer_choice==1)\
        or (player_choice ==0 and computer_choice==2):
    print ('PLAYER WINS')

else:
    print ("Pick a number between 0 and 2 next time.")



