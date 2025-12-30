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

list_item = [rock, paper, scissors]
choices = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
random_choice = random.randint(0, 2)

if choices >= 0 and choices <= 2:
    print(list_item[choices])
print("Computer chose:")
print(list_item[random_choice])

if choices >= 3 or choices < 0:
    print("Invalid number. You lose!")
elif choices == 0:
    if random_choice == 0:
        print("Tie")
    elif random_choice == 1:
        print("You lose")
    else:
        print("You win")
elif choices == 1:
    if random_choice == 0:
        print("You win")
    elif random_choice == 1:
        print("Tie")
    else:
        print("You lose")
else:
    if random_choice == 0:
        print("You lose")
    elif random_choice == 1:
        print("You win")
    else:
        print("Tie")
