#Function with default 'discount' arguement
def apply_discount (price, discount=0.05):
    return price * (1 - discount)

#Function where 'tax' has a default Value 
def apply_tax (price, tax=0.07):
    return price * (1 + tax)

#Function using custom 'discount' + calculate_total (price, discount=0.05, tax=0.07):
def calculate_total(price, discount=0.05, tax=0.07): 
    discounted = apply_discount(price, discount)
    total = apply_tax(discounted, tax)
    return total

#Calling function using keyword arguements
total_price_default = calculate_total(price=120, discount=0.05, tax=0.07)
print(f"Total cost with default discount and tax: ${total_price_default}")

#Calling function using custom values and keyword arguements
total_price_custom = calculate_total(price=100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")
