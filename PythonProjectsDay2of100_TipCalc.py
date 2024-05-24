print("Welcome to the Tip Calculator!/n")
coststr = input("Please enter your meal cost: $")
cost_fl = float(coststr);

tip = input("What percentage tip would you like to give? ")
tip = float(tip);
tip = tip / 100
costplustip = cost_fl + (cost_fl * tip);

split = input("How many people to split the bill? ")
split = float(split);
indcost = costplustip / split;
indcost = round(indcost, 2);

print(f"Each person should pay: ${indcost}")
