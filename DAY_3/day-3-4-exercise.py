# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == "S": 
  amount= 15
  if add_pepperoni == "Y":
    amount += 2
elif size == "M":
  amount =20
  if add_pepperoni == "Y":
    amount += 3
else:
  amount = 25
  if add_pepperoni == "Y":
    amount +=3

if extra_cheese == "Y":
  bill = amount + 1

else:
  bill = amount

print(f"Your final bill is: {bill}.")



