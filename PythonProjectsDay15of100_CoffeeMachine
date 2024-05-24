menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
      },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
      },
    "cappucinno": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

profit = 0;
resources = {
  "water" : 300,
  "milk" : 200,
  "coffee" : 100,
}

def check_resources(order_ing):
  for item in order_ing:
    if order_ing[item] > resources[item]:
      print("Sorry! Not enough " + item + "!\n")
      return False
  return True

def process_coins(order_price):
  print(f"The cost of your order is ${round(order_price,3)}")
  print("Please insert coins:")
  total = int(input("Insert Quarters: ")) * 0.25
  total += int(input("Insert Dimes: ")) * 0.1
  total += int(input("Insert Nickles: ")) * 0.05
  total += int(input("Insert Pennies: ")) * 0.01
  return total

def transaction_check(money_recieved, order_price):
  if(money_recieved >= order_price):
    change = round((money_recieved - order_price), 2)
    print(f"Here is your change: ${change}")
    global profit
    profit += order_price;
    return True
  else:
    print("Sorry! Thats not enough!")
    return False

def make_coffee(drink_name, order_ing):
  for item in order_ing:
    resources[item] -= order_ing[item]
  print(f"Here is your {drink_name}")

def add_resource():
  print(f"Water: {resources['water']}ml")
  print(f"Milk: {resources['milk']}ml")
  print(f"Coffee: {resources['coffee']}ml")
  adding_resource = input("Which resource would you like to add? ")
  amount_adding = int(input("How much would you like to add? "))
  new_amount = int(resources[adding_resource]) + amount_adding;
  resources[adding_resource] = new_amount;

is_on = True;

while(is_on):
  print("Welcome to the coffee machine!")
  coffee_type = input("What would you like? (espresso/latte/cappuccino) (type 'off' to turn off and 'r' to report resources or 'add' to add resource): ")
  if coffee_type == "off":
    is_on = False
  elif coffee_type == "r":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Profit: ${profit}")
  elif coffee_type == "add":
    add_resource()
  else:
    drink = menu[coffee_type];
    if (check_resources(drink["ingredients"])):
      payment = process_coins(drink["cost"])
      if transaction_check(payment, drink["cost"]):
        make_coffee(coffee_type, drink["ingredients"])

  print("\n\n")
