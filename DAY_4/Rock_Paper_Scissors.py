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

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:" )

print("Your choice: \n")

if choice == "0" :
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif choice == "1" :
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

else:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')


Computer_choice = random.randint(0,2)

print("Computer's choice: \n")
if Computer_choice == 0 :
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

elif Computer_choice == 1 :
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

else :
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

if choice == "0" :
    if Computer_choice == 0 :
        print("draw")
    elif Computer_choice == 1 :
        print("You lose")
    else:
        print("You win")
elif choice == "1" :
    if Computer_choice == 0:
        print("You win")
    elif Computer_choice == 1:
        print("draw")
    else:
        print("You lose")
else:
    if Computer_choice == 0:
        print("You lose")
    elif Computer_choice == 1 :
        print("You win")
    else:
        print("draw")


