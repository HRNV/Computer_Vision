import numpy as np
import cv2
import matplotlib.pyplot as plt

# read the input image
imag = cv2.imread("CR7.jpg")
#convert BGR to RGB
imag = cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)


# switch off the axis
plt.axis('off')
# show the image
plt.imshow(imag)
plt.show()

# the dimensions. 
r, c, dim = img.shape
# for x axis
Mr = np.float32([[1,  0, 0   ],
                [0, -1, r],
                [0,  0, 1   ]])
# for y-axis reflection
# Mr = np.float32([[-1, 0, c],
#                 [ 0, 1, 0   ],
#                 [ 0, 0, 1   ]])
# apply a perspective transformation to the image
reflected_imag = cv2.warpPerspective(imag,Mr,(int(c),int(r)))

# switch off
plt.axis('off')

# show the resulting image
plt.imshow(reflected_img)
plt.show()

# save the resulting image to disk
plt.imsave("CR7.jpg", reflected_img)
