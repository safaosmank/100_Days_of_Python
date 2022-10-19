from Menu import Menu_list

from Menu import resources

total_money = 0
machine_running = True


def is_resources_sufficient(order_ingredients):
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
        return True


# one penny = 1 cent
# one nickel = 5 cents
# one dime = 10 cents
# one quarter = 25 cents

def total_amount():
    print("PLease insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    quarters_total = quarters * 0.25
    dimes_total = dimes * 0.1
    nickel_total = nickles * 0.05
    pennies_total = pennies * 0.01
    total = float(quarters_total + dimes_total + nickel_total + pennies_total)
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global total_money
        total_money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def makeCoffee(drink_name, order_ingredients):
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
        print(f"Here is your {drink_name} ☕. Enjoy!")
        return


while machine_running:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        machine_running = False

    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"money: {total_money}")

    else:
        drink = Menu_list[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = total_amount()
            if is_transaction_successful(payment, drink["cost"]):
                makeCoffee(choice, drink["ingredients"])
