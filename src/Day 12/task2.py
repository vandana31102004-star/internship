import matplotlib.pyplot as plt

# Bar chart data
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# Line chart data
months = [1, 2, 3, 4, 5]
monthly_sales = [200, 300, 400, 350, 500]

# Subplot 1 - Bar Chart
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

# Subplot 2 - Line Chart
plt.subplot(1, 2, 2)
plt.plot(months, monthly_sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

# Adjust layout
plt.tight_layout()

# Display
plt.show()
