import matplotlib.pyplot as plt

# Data
sizes = [10, 20, 30, 40, 50, 100, 200, 400, 800, 1600]
values = [11.0, 38.0, 79.0, 124.0, 160.0, 366.0, 871.0, 1976.0, 4211.0, 8784.0]

# Plotting
plt.plot(sizes, values, marker='o', linestyle='-')

# Adding title and labels
plt.title('Plot of average number of iterations against Sizes')
plt.xlabel('Sizes')
plt.ylabel('Average number of iterations')

# Display the plot
plt.show()
