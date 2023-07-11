
#Exercise 4
import numpy as np
import matplotlib.pyplot as plt

# Set the dimensions of the image
image_width = 200
image_height = 200

# Create a blank image with black background
image = np.zeros((image_height, image_width))

# Set the coordinates of the center of the circle
center_x = image_width // 2
center_y = image_height // 2

# Set the radius of the circle
radius = 50

# Create a grid of coordinates
y_coords, x_coords = np.ogrid[:image_height, :image_width]

# Create a mask for the circular spot
mask = (x_coords - center_x) ** 2 + (y_coords - center_y) ** 2 <= radius ** 2

# Set the circular spot to white
image[mask] = 255

# Display the image
plt.imshow(image, cmap='gray')
plt.axis('off')
plt.show()
