import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Creating the scatter plot
plt.scatter(x, y, color='blue', marker='o', label='Data Points')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')

# Adding legend
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
