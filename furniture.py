# Define the description and price of the Lovely Loveseat.
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

# Define the description and price of the Stylish Settee.
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

# Define the description and price of the Luxurious Lamp.
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

# Define the sales tax rate.
sales_tax = .088

# Define the total cost and itemization for the first customer.
customer_one_total = 0
customer_one_itemization = ""

# Add the price of the Lovely Loveseat to the first customer's total cost.
customer_one_total += lovely_loveseat_price

# Add the description of the Lovely Loveseat to the first customer's itemization.
customer_one_itemization += lovely_loveseat_description

# Add the price of the Luxurious Lamp to the first customer's total cost.
customer_one_total += luxurious_lamp_price

# Add the description of the Luxurious Lamp to the first customer's itemization.
customer_one_itemization += luxurious_lamp_description

# Calculate the sales tax for the first customer's order.
customer_one_tax = customer_one_total * sales_tax

# Add the sales tax to the first customer's total cost.
customer_one_total += customer_one_tax

# Print the items and total cost for the first customer.
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)

# Define the total cost and itemization for the second customer.
customer_two_total = 0
customer_two_itemization = ""

# Add the price of the Stylish Settee to the second customer's total cost.
customer_two_total += stylish_settee_price

# Add the description of the Stylish Settee to the second customer's itemization.
customer_two_itemization += stylish_settee_description

# Add the price of the Luxurious Lamp to the second customer's total cost.
customer_two_total += luxurious_lamp_price

# Add the description of the Luxurious Lamp to the second customer's itemization.
customer_two_itemization += luxurious_lamp_description

# Calculate the sales tax for the second customer's order.
customer_two_tax = customer_two_total * sales_tax

# Add the sales tax to the second customer's total cost.
customer_two_total += customer_two_tax

# Print the items and total cost for the second customer.
print("Customer Two Items:")
print(customer_two_itemization)
print("Customer Two Total:")
print(customer_two_total)
