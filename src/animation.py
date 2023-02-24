import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from ListDot import * 

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate the dots randomly
dotList = ListDot(3, 100) 
dotList.generateRandom()

# Generate some 3D data
# x = ax.set_xticks(dotList.)
# y = ax.set_yticks(dotList.dimension)
# z = ax.set_zticks(dotList.dimension)
x = np.random.normal(size=50)
y = np.random.normal(size=50)
z = np.random.normal(size=50)

# Creating the title
ax.set_title("Pasangan Titik Terdekat 3D")

# Plot the dots using scatter plot
ax.scatter(x, y, z, c='blue', marker='o')

# Plot the nearest dots using scatter plot
ax.scatter(2, 3, 4, c='red', marker='x')
ax.scatter(2, 3, 5, c='red', marker='x')

# Set the labels name for the axes
ax.set_xlabel('Sumbu X')
ax.set_ylabel('Sumbu Y')
ax.set_zlabel('Sumbu Z')

# Show the plot
plt.show()
