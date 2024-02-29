import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
temperatures = [23, 25, 24, 26, 22]  # Temperature values for each day

# Plotting the data
plt.plot(days, temperatures, marker='o', linestyle='-')

# Adding labels and title
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')
plt.title('Weekly Temperature Variation')

# Display the plot
plt.grid(True)  # Add grid lines
plt.show()
