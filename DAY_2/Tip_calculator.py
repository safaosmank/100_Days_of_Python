#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")

bill_total=float(input("What was your total bill? $"))

tip= int(input("What percentage tip would you like to give? 10, 12, or 15? "))

no_people=int(input("How many people to split the bill? "))

each_bill = (bill_total)/(no_people)

tip_per_person = each_bill*(tip/100)

bill_per_person = round(each_bill + tip_per_person ,2)

print(f"Each person should pay: ${bill_per_person}")