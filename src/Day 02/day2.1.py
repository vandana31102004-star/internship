# Simple Calculator Program
"""
print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", num1 + num2)

elif choice == '2':
    print("Result:", num1 - num2)

elif choice == '3':
    print("Result:", num1 * num2)

elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")

else:
    print("Invalid choice")
"""
"""
name=input("enter your name:")
print("welcome",name,"!")
print("welcome"+name+"!")
print(f"welcome{name}!")
#typecasting
b=5.2
print(complex(b))
"""
"""
name=input("Enter your name:")
age=input("Enter your age:")
print(f"Age in 2030={int(age)+}")
"""
"""
# Ask for user's name
name = input("Enter your name: ")

# Ask for user's current age
age = input("Enter your current age: ")

# Convert age to integer
age = int(age)

# Calculate age in 2030 (current year is 2026)
new_age = age + 4

# Output result
print(f"Hey {name}, you will be {new_age} years old in 2030!")
"""
"""
# Ask for total bill amount
bill = float(input("Enter total bill amount: "))

# Ask for number of people
people = int(input("Enter number of people: "))

# Calculate share per person
share = bill / people

# Print result
print("Total Bill:", bill, ". Each person pays:", share)

# Bonus: check data types
print(type(bill))
print(type(people))
print(type(share))
"""
"""
# Hardcoded values
item_name = "Laptop"
quantity = 2
price = 499.99
in_stock = True

# Print formatted receipt
print("Item:", item_name, ", Qty:", quantity, ", Price:", price, ", Available:", in_stock)

# Calculate and print total cost
total_cost = quantity * price
print("Total Cost:", total_cost)
"""
total_bill=float(input("Enter the total bill amount : "))
total_num=int(input("Enter the total no of people : "))

each_bill=total_bill/total_num
print(f"Total bill is {total_bill}. Each person should pay {each_bill:.2f}  ")
