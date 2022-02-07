# import all the libraries
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# to open the image
image = Image.open("hopper.jpeg")
# this open the photo viewer
# image.show()
# plt.imshow(image)

# image watermark
size = (500, 100)
crop_image = image.copy()
# to keep the aspect ration in intact
crop_image.thumbnail(size)

# add watermark
copied_image = image.copy()
# base image
copied_image.paste(crop_image, (500, 300))
# pasted the crop image onto the base image
copied_image.show()
plt.imshow(copied_image)
