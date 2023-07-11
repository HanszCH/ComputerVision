#Exercise 4
import cv2 as cv

# Load the image
image = cv.imread("images/dog.jfif")

# Upscale the image using linear interpolation
upscaled_linear = cv.resize(image, None, fx=2, fy=2, interpolation=cv.INTER_LINEAR)

# Upscale the image using cubic interpolation
upscaled_cubic = cv.resize(image, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)

# Upscale the image using nearest neighbor interpolation
upscaled_nearest = cv.resize(image, None, fx=2, fy=2, interpolation=cv.INTER_NEAREST)

# Display the original and upscaled images
cv.imshow("Original Image", image)
cv.imshow("Linear Interpolation", upscaled_linear)
cv.imshow("Cubic Interpolation", upscaled_cubic)
cv.imshow("Nearest Neighbor Interpolation", upscaled_nearest)
cv.waitKey(0)
cv.destroyAllWindows()


#Comments
#Nearest neighbour interpolation results blocky images
#Linear interpolation and Cubic interpolation results blurer images but not blocky
#Cubic interpolation has a clearer picture compared to linear interpolation when scale to a larger value
