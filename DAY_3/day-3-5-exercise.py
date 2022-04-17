# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bothnames = name1 + name2

Both_names =bothnames.upper()

T = Both_names.count("T")
R = Both_names.count("R")
U = Both_names.count("U")
E = Both_names.count("E")

TRUE = T + R + U + E

L = Both_names.count("L")
O = Both_names.count("O")
V = Both_names.count("V")
E = Both_names.count("E")

LOVE = L + O + V + E

score =int(f"{TRUE}{LOVE}")

if score < 10 or score > 90 :
  print(f"Your score is {score}, you go together like coke and mentos")

elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.") 

else:
  print(f"Your score is {score}.")

