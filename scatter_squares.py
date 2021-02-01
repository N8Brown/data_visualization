import matplotlib.pyplot as plt

x_vals = [1, 2, 3, 4, 5]
y_vals = [1, 4, 9, 16, 25]

plt.scatter(x_vals, y_vals, s=100)

# Set chart title and lable axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis="both", labelsize=14)

plt.show()