#! /bin/bash

# range of the photos that will be used for the timelapse
MIN_RANGE=$1
MAX_RANGE=$2

# build the time lapse movie
~/Downloads/SnowLeopard_Lion_Mountain_Lion_Mavericks_Yosemite_06/ffmpeg -f image2 -start_number ${MIN_RANGE} -i DSC_%04d.jpg -vcodec libx264 -y -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -pix_fmt yuv420p timelapse.mp4
