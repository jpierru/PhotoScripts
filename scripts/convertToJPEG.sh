#! /bin/bash

# range of the photos that will be used for the timelapse
MIN_RANGE=$1
MAX_RANGE=$2

# size of the resized image
MAX_SIZE=1600

# the location of the JPEG output images and the final timelapse
OUTPUT_FOLDER="./output_timelapse_${MIN_RANGE}_${MAX_RANGE}_${MAX_SIZE}"

# create the output folder if it does not exist
if [ ! -d $OUTPUT_FOLDER ]; then
  mkdir $OUTPUT_FOLDER
fi

# convert RAW (.NEF) to JPEG
padtowidth=4
for i in `seq ${MIN_RANGE} ${MAX_RANGE}`; do
  i=`printf "%0*d\n" $padtowidth $i`
  f="DSC_${i}.NEF"
  jpg="${f%NEF}jpg"
  sips -s format jpeg -s formatOptions best -Z $MAX_SIZE $f -o "${OUTPUT_FOLDER}/${jpg}"
  touch -r $f "${OUTPUT_FOLDER}/${jpg}"
done
