import numpy as np
import time
import matplotlib.pyplot as plt

t1 = time.time()

R_Range = 10
i_max = 10**8  # High count for accurate Pi calculation

center_x, center_y = 0, 0
radius = R_Range

rng = np.random.default_rng()
x = rng.uniform(-R_Range, R_Range, i_max)
y = rng.uniform(-R_Range, R_Range, i_max)

r = np.sqrt(x**2 + y**2)

r_1 = 0
for value in r:
    if value <= R_Range:
        r_1 += 1
# find the ratio between the area of a circle pi*R2 and the area of the square 2R*2R that surrounds it
# probability of a point landing inside the circle is the area of the circle divided by the area of the square
pi_app = (4 * r_1) / i_max

t2 = time.time()

print("pi=", pi_app)
delta = t2 - t1
print("time = ", delta)

# --- Only plot a safe subset of points (first 10,000) ---
plot_limit = 10_000

# Use a scatter plot instead of a line plot, coloring points inside vs outside
# boolean array called inside which contains True for points inside the circle and False for points outside.
inside = r[:plot_limit] <= R_Range

fig, ax = plt.subplots(figsize=(8, 8))

# Plot points inside the circle as green, outside as red
ax.scatter(x[:plot_limit][inside], y[:plot_limit][inside], color='green', s=1, label='Inside')
ax.scatter(x[:plot_limit][~inside], y[:plot_limit][~inside], color='red', s=1, label='Outside')

# Draw the boundary circle for clarity
circle = plt.Circle((0, 0), radius, color='blue', fill=False, linewidth=2)
ax.add_patch(circle)

ax.set_aspect('equal')
ax.set_xlim(-R_Range, R_Range)
ax.set_ylim(-R_Range, R_Range)
plt.title(f"Monte Carlo Pi Estimation (Plotting {plot_limit:,} of {i_max:,} points)")
plt.legend()
plt.show()
