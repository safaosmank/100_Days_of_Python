import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

len_names = len(names)

random_name= random.randint(0, len_names - 1)

chosen = names[random_name]

print(chosen + " is going to buy the meal today!")


