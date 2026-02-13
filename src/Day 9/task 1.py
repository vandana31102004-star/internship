import pandas as pd
products = pd.Series(
    data=[700, 150, 300],                  # Prices
    index=['Laptop', 'Mouse', 'Keyboard']  # Product names as labels
)

laptop_price = products['Laptop']

first_two_products = products[:2]
print("Full Series:")
print(products)

print("\nPrice of Laptop:")
print(laptop_price)

print("\nFirst two products:")
print(first_two_products)
