def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


# Take user input
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Call the function
area, perimeter = calc_rectangle(length, width)

# Print the result
print(f"Area: {area}, Perimeter: {perimeter}")

