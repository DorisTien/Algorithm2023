import pandas as pd
import matplotlib.pyplot as plt

sizes = [10, 20, 30, 40, 50, 100, 200, 400, 800, 1600]
values = [177.0, 1931.5, 2550.0, 9617.5, 11998.0, 53287.5, 314298.0, 1014111.5, 3951446.0, 15541535.0]
values2 = [279.0, 1222.5, 3064.5, 4674.0, 6644.5, 41799.5, 181293.0, 800356.5, 2527792.5, 9655031.5]
comparison = [50.0, 200.0, 450.0, 800.0, 1250.0, 5000.0, 20000.0, 80000.0, 320000.0, 1280000.0]
comparison2=[25.0, 100.0, 225.0, 400.0, 625.0, 2500.0, 10000.0, 40000.0, 160000.0, 640000.0]
# Creating a dictionary from the arrays
data = {'Sizes': sizes, 'Random sort': values, 'Upper Bound': comparison}

# Creating a DataFrame from the dictionary
df = pd.DataFrame(data)

# Printing the DataFrame
print(df)
# Plotting the values, values2, and comparison arrays
plt.plot(sizes, values, label='Random Sort', marker='o')
plt.plot(sizes, comparison, label='Upper bound', marker='o')
#plt.plot(sizes, comparison, label='Upper Bound', marker='o')

# Adding title and labels
plt.title('Plot of random sort and upper bound')
plt.xlabel('Input Size')
plt.ylabel('Interations')
plt.legend()

# Display the plot
plt.show()