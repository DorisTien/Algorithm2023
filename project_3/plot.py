import matplotlib.pyplot as plt

bt = 0.061541080474853516
greedy = 0.015014171600341797

# Creating lists for plotting
algorithms = ['backtrack', 'greedy']
values = [bt, greedy]

# Plotting the values
plt.figure(figsize=(6, 6))
plt.bar(algorithms, values, color=['blue', 'orange'])
plt.xlabel('Algorithms')
plt.ylabel('Processing Time')
plt.title('Comparison of Processing Times')
plt.show()
