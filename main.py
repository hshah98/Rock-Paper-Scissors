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

images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if (user_choice >= 0) and (user_choice < 3):
  print(images[user_choice])
  computer_choice = random.randint(0, 2)
  print(f"Computer chose:\n{images[computer_choice]}")

  if user_choice == computer_choice:
    print("It's a draw.")
  elif (computer_choice - user_choice == 1) or (computer_choice - user_choice == -2):
    print("You lose!")
  else:
    print("You win!")
else:
  print("Invalid choice. Please try again.")
