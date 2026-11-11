#For simple and quick plots (e.g., in a Jupyter notebook or simple scripts), the plt.plot() (state-based) approach is often preferable because it's more concise.

#For More complex illustrations, the object-oriented ax.plot() style is preferable, as it provides better flexibility. It's especially useful when you're working with multiple subplots, figures, or want fine-tuned control over the layout and appearance of your plots.


import matplotlib.pyplot as plt
import numpy as np

# Generate some dataset
x = np.linspace(0, 10, 100)
y = np.cos(x)

# The most simple plot with plt. syntax
plt.plot(x, y, label='sin(x)')
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()


data = np.random.randn(1000)  # Generate 1000 random data points

# A simple histogram Plot
plt.hist(data, bins=30, alpha=0.75, color='blue', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# How about a polar plot?
theta = np.linspace(0, 2*np.pi, 100)
r = 1 + np.sin(3*theta)

# Matplotlib says "sure"
plt.polar(theta, r)
plt.title('Maybe this is an orbit?')
plt.show()

# More data!
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Multiple Subplots
fig, axs = plt.subplots(2, 1, figsize=(6, 8))  # 2 rows, 1 column

axs[0].plot(x, y1, color='r', label='sin(x)')
axs[0].set_title('Sinus')
axs[0].set_xlabel('X-axis')
axs[0].set_ylabel('Y-axis')
axs[0].legend()
axs[0].grid(True)

axs[1].plot(x, y2, color='b', label='cos(x)')
axs[1].set_title('Cosinus')
axs[1].set_xlabel('X-axis')
axs[1].set_ylabel('Y-axis')
axs[1].legend()
axs[1].grid(True)
plt.tight_layout() # this command adjusts layout to prevent overlap
plt.show()

# More data!
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y) # note this command; it creates a grid
Z = np.sin(np.sqrt(X**2 + Y**2))


# A bad contour plot (confuse everyone!)
plt.contour(X, Y, Z, levels=5, cmap='gray')  # Gray color, very few contour levels
plt.title('A bad contour plot')
plt.xlabel('X')  # Poor label
plt.ylabel('Y')  # Poor label
plt.show()


# A good contour plot
contour = plt.contourf(X, Y, Z, levels=20, cmap='viridis')  # More levels, better color scheme
plt.colorbar(contour, label='Z value')  # Adding a color bar with a label
plt.contour(X, Y, Z, levels=20, colors='black', linewidths=0.5)  # Adding contour lines for contrast
plt.title('A better contour plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)  # Adding grid for better readability
plt.show()
