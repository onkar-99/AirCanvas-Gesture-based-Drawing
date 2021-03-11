import numpy as np
from matplotlib import pyplot as plt
import glob
import os
import matplotlib.figure
import cv2
from PIL import Image
def score(image):
   #img=Image.open('imagedoodle.png')
   img=Image.fromarray(image.astype(np.uint8))
   height, width = img.size
   left = 152
   top = 132
   width = 246
   height = 166
   box = (left, top, left+width, top+height)
   
#resizing the image to find spaces better
   cropped = img.crop(box)
    #image = cv2.resize(image, dsize=(28,28), interpolation=cv2.INTER_CUBIC)
    #cv2.imshow("Frame", img)
   img=cropped.resize((64, 64), Image.ANTIALIAS)
   black = (0,0,0)
   white = (255,255,255)
   threshold = (200,200,200)
# Open input image in grayscale mode and get its pixels.
   pixels = img.getdata()
   newPixels = []

# Compare each pixel 
   for pixel in pixels:
       if pixel < threshold:
           newPixels.append(black)
       else:
           newPixels.append(white)

# Create and save new image.
   newImg = Image.new("RGB",img.size)
   newImg.putdata(newPixels)
   newImg = cv2.cvtColor(np.float32(newImg), cv2.COLOR_BGR2GRAY).reshape(64,64,1)

   #plt.imshow(newImg)
   #newImg.save("imagedoodle_cropped.png", quality=100)
   plot=np.asarray(newImg).reshape(64,64,1)
   return plot
