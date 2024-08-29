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
user_choice = int(input("Hello, welcome to my game. What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"
))

choice = [rock, paper, scissors]
print(choice[user_choice])

computer_choice = random.randint(0, len(choice)-1)

print("Computer chose")

print(choice[computer_choice])
if user_choice == computer_choice:
  print("It's a draw!")
if user_choice == 0 and computer_choice == 2:
  print("You won")
elif user_choice == 1 and computer_choice == 0:
  print("You won")
elif user_choice == 2 and computer_choice == 1:
  print("You won")
else:
  print("You lost")
