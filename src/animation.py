import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Generate some 3D data
x = np.random.normal(size=50)
y = np.random.normal(size=50)
z = np.random.normal(size=50)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the dots using scatter plot
ax.scatter(x, y, z, c='r', marker='o')

# Set the labels for the axes
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Show the plot
plt.show()
