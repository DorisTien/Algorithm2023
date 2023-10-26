import pandas as pd
import matplotlib.pyplot as plt

sizes = [10, 20, 30, 40, 50, 100, 200, 400, 800, 1600]
values = [177.0, 1931.5, 2550.0, 9617.5, 11998.0, 53287.5, 314298.0, 1014111.5, 3951446.0, 15541535.0]
values2 = [279.0, 1222.5, 3064.5, 4674.0, 6644.5, 41799.5, 181293.0, 800356.5, 2527792.5, 9655031.5]
comparison = [40000, 640000, 3240000, 10240000, 25000000, 400000000, 6400000000, 102400000000, 1638400000000, 26214400000000]
comparison2=[4000, 32000, 108000, 256000, 500000, 4000000, 32000000, 256000000, 2048000000, 16384000000]
# Creating a dictionary from the arrays
data = {'Sizes': sizes, 'Random sort2': values2, 'Upper Bound': comparison2}

# Creating a DataFrame from the dictionary
df = pd.DataFrame(data)

# Printing the DataFrame
print(df)
# Plotting the values, values2, and comparison arrays
plt.plot(sizes, values2, label='Random Sort', marker='o')
plt.plot(sizes, comparison2, label='Upper bound', marker='o')
#plt.plot(sizes, comparison, label='Upper Bound', marker='o')

# Adding title and labels
plt.title('Plot of random sort and upper bound')
plt.xlabel('Input Size')
plt.ylabel('Interations')
plt.legend()

# Display the plot
plt.show()