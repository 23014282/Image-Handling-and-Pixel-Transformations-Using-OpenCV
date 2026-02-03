#!/usr/bin/env python
# coding: utf-8

# ## EXP-1 Image Handling and Pixel Transformations Using OpenCV ##
# ## NAME : JEEVITH A ##
# ## REG NO : 212223240059 ##

# 
# 

# In[16]:


import numpy
import matplotlib.pyplot as plt
import cv2

print(numpy.__version__)
print("Imports successful")


# In[15]:


import cv2
import matplotlib.pyplot as plt

img = cv2.imread("123.JPG")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.axis('off')
plt.title("Original")
plt.show()


# In[3]:


import cv2
import matplotlib.pyplot as plt

img = cv2.imread("123.JPG")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(gray, cmap='gray')
plt.axis('off')
plt.title("Grayscale Image")
plt.show()


# In[4]:


import cv2
import matplotlib.pyplot as plt

img = cv2.imread("123.JPG")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale")
plt.axis('off')

plt.show()


# In[5]:


import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("123.JPG")

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Draw a line on the image
# (x1, y1) to (x2, y2), color = red, thickness = 3
cv2.line(img_rgb, (50, 50), (300, 300), (255, 0, 0), 3)

# Display the image
plt.imshow(img_rgb)
plt.title("Image with Line")
plt.axis('off')
plt.show()

# Save the output image
cv2.imwrite("image_with_line.jpg", cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))
print("Image saved as image_with_line.jpg")


# In[6]:


import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("123.JPG")

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Draw a circle on the image
# center = (x, y), radius = 80, color = blue, thickness = 3
cv2.circle(img_rgb, (200, 200), 80, (0, 0, 255), 3)

# Display the image
plt.imshow(img_rgb)
plt.title("Image with Circle")
plt.axis('off')
plt.show()

# Save the output image
cv2.imwrite("image_with_circle.jpg", cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))
print("Image saved as image_with_circle.jpg")


# In[7]:


import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("123.JPG")

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Draw a rectangle on the image
# top-left corner = (x1, y1), bottom-right corner = (x2, y2)
# color = green, thickness = 3
cv2.rectangle(img_rgb, (100, 100), (350, 300), (0, 255, 0), 3)

# Display the image
plt.imshow(img_rgb)
plt.title("Image with Rectangle")
plt.axis('off')
plt.show()

# Save the output image
cv2.imwrite("image_with_rectangle.jpg", cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))
print("Image saved as image_with_rectangle.jpg")


# In[8]:


import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("123.JPG")

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Add text on the image
# text = "@jeeviii"
# position = (x, y)
# font = cv2.FONT_HERSHEY_SIMPLEX
# font scale = 1
# color = red
# thickness = 2
cv2.putText(img_rgb, "@jeeviii", (100, 100),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# Display the image
plt.imshow(img_rgb)
plt.title("Image with Text")
plt.axis('off')
plt.show()

# Save the output image
cv2.imwrite("image_with_text.jpg", cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))
print("Image saved as image_with_text.jpg")


# In[9]:


import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("123.JPG")

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Display the HSV image
plt.imshow(hsv)
plt.title("HSV Image")
plt.axis('off')
plt.show()

# Save the HSV image
cv2.imwrite("hsv_image.jpg", hsv)
print("HSV image saved as hsv_image.jpg")


# In[10]:


import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("123.JPG")

# Convert BGR to YCrCb
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# Split channels
y, cr, cb = cv2.split(ycrcb)

# Display channels
plt.subplot(1,3,1)
plt.imshow(y, cmap='gray')
plt.title("Y (Luminance)")
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(cr, cmap='gray')
plt.title("Cr (Red Chroma)")
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(cb, cmap='gray')
plt.title("Cb (Blue Chroma)")
plt.axis('off')

plt.show()

# Save YCrCb image
cv2.imwrite("ycrcb_image.jpg", ycrcb)
print("YCrCb image saved as ycrcb_image.jpg")



# In[11]:


import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("123.JPG")

# Get original size
h, w = img.shape[:2]

# Resize to half size
resized = cv2.resize(img, (w//2, h//2))

# Convert BGR to RGB for display
resized_rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

# Display resized image
plt.imshow(resized_rgb)
plt.title("Resized Image (Half Size)")
plt.axis('off')
plt.show()

# Save resized image
cv2.imwrite("resized_half.jpg", resized)
print("Resized image saved as resized_half.jpg")


# In[12]:


import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("123.JPG")

# Flip horizontally
flip_h = cv2.flip(img, 1)

# Flip vertically
flip_v = cv2.flip(img, 0)

# Convert BGR to RGB for display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
flip_h_rgb = cv2.cvtColor(flip_h, cv2.COLOR_BGR2RGB)
flip_v_rgb = cv2.cvtColor(flip_v, cv2.COLOR_BGR2RGB)

# Display images
plt.subplot(1,3,1)
plt.imshow(img_rgb)
plt.title("Original")
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(flip_h_rgb)
plt.title("Horizontal Flip")
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(flip_v_rgb)
plt.title("Vertical Flip")
plt.axis('off')

plt.show()

# Save flipped images
cv2.imwrite("flip_horizontal.jpg", flip_h)
cv2.imwrite("flip_vertical.jpg", flip_v)

print("Images saved as flip_horizontal.jpg and flip_vertical.jpg")


# In[13]:





# In[14]:





# In[ ]:




