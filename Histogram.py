import matplotlib.pyplot as plt
import numpy as np

# Generating random ages data
np.random.seed(0)
ages = np.random.randint(20, 60, size=100)  # Generating 100 random ages between 20 and 60

# Creating the histogram
plt.hist(ages, bins=10, color='lightblue', edgecolor='black')

# Adding labels and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')

# Display the plot
plt.grid(axis='y')  # Add grid lines to y-axis
plt.show()
