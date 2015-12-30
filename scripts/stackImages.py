from PIL import ImageChops, Image
import os
import sys

# the range of image we want to stack
first_image = int(sys.argv[1]) # 197
last_image = int(sys.argv[2])  # 360

finalimage = Image.open('DSC_'+str(first_image).zfill(4)+'.jpg')
for i in range(first_image+1,last_image):
    currentimage = Image.open('DSC_'+str(i).zfill(4)+'.jpg')
    finalimage = ImageChops.lighter(finalimage, currentimage)
finalimage.save("all_stacked.jpg","JPEG")
