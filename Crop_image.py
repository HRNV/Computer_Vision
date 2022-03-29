import numpy as np   // importing the numpy for matrix 
import cv2	          
import matplotlib.pyplot as plt

# read the input image
imag = cv2.imread("CR7.jpg")
# convert from BGR to RGB (the inherent space is BGR for cv2
imag = cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
#the dimensions of the image
print(imag.shape) 
# axes to be invisible
plt.axis('off')
# show the image
plt.imshow(imag)
plt.show()

500 pixels from 100 to 600 on both x-axis & y-axis

crop_imag = imag[100:600, 100:600]
#compre the two dimensions
print(imag.shape) 
print(crop_imag.shape)

# axes to be invisible
plt.axis('off')
# show the transofrmed image

plt.imshow(crop_imag)
plt.show()

# save the transofrmed image
plt.imsave("CR7.jpg_cropped.jpg", crop_imag)
