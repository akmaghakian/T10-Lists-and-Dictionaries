#This code establishes a menu list with four food and drink items, a stock dictionary with the stock price for each item, and a price dictionary with the price for each item. 
#It then loops through the menu list, and calculates the value of each item by multiplying the stock value by the price. It adds up all of the item values to get the total stock worth, and then prints the result.

# Firstly we define the menu
menu = ['coffee', 'tea', 'croissant', 'sandwich']

# Secondly we define the stock for each item
stock = {'coffee': 300, 'tea': 58, 'croissant': 52, 'sandwich': 43}

# Thirdly we define the price for each item
price = {'coffee': 2.60, 'tea': 2.40, 'croissant': 2.80, 'sandwich': 4.50}

# Fourthly we calculate the total stock worth applying the loop function on the lists.
total_stock_worth = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value

# Fifthly and finally we print the result
print("The total stock worth in the cafe is: $", total_stock_worth)