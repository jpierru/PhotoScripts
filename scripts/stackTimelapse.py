from PIL import ImageChops, Image
import os
import sys

# the range of image we want to stack
first_image = int(sys.argv[1]) # 197
last_image = int(sys.argv[2])  # 360

# create the output folder if it does not already exist
if not os.path.isdir("stacked"):
    os.makedirs("stacked")

# stack all of the image and save the intermediary images for the timelapse
finalimage = Image.open('DSC_'+str(first_image).zfill(4)+'.jpg')
for i in range(first_image+1,last_image+1):
    currentimage = Image.open('DSC_'+str(i).zfill(4)+'.jpg')
    finalimage = ImageChops.lighter(finalimage, currentimage)
    finalimage.save('stacked/stack_'+str(i).zfill(4)+'.jpg',"JPEG")

# create the timelapse
os.system('~/Downloads/SnowLeopard_Lion_Mountain_Lion_Mavericks_Yosemite_06/ffmpeg -f image2 -start_number '+str(first_image)+' -i stacked/stack_\%04d.jpg -vcodec libx264 -y -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -pix_fmt yuv420p stacked/stack_timelapse.mp4')
