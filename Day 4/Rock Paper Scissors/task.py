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

game_images= [rock,paper, scissors]

user_choice = int(input('0 == rock, 1 == paper, 2 == scissors'))
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print(f'{computer_choice}')
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print('lose')
elif user_choice == 0 and computer_choice == 2:
    print('user wins')
elif computer_choice == 0 and user_choice == 2:
    print('lose')
elif computer_choice > user_choice:
    print('computer wins')
elif user_choice > computer_choice:
    print('win')
elif computer_choice == user_choice:
    print('draw')
else:
    print('error')