#!/usr/bin/env python3

import tinify as t
import glob2 as g

# Variables
matching_string = r"C:\Users\monstr99\Desktop\pics\compress-these\*.jpg"
destination = r"C:\Users\monstr99\Desktop\pics\optimized\\"
count = 0

# API Key
t.key = "lBkQw3_IwOIG16mIIfS-4WsJzwxj0rwB"

images = g.glob(matching_string, case_sensitive=False)

no_of_files = len(images)

for image in images:
    # Compression progress
    count += 1

    # To obtain source image name
    _ = image.split("\\")
    img_name = _[-1].split(".")[0]
    comprssd_addr = [destination,img_name,"-comprssd.jpg"]

    # printing on successful compressing
    print(img_name + ".jpg " + " ========compressing=========>  " + ''.join(comprssd_addr[1:]) + "   (" + str(count) + " of " + str(no_of_files) + ")")


    # API calls for compressing
    source = t.from_file(image)

    # API Call for resizing images to 2048px Width
    resized = source.resize(
    method = "cover",  # fit : scale down within given dimesions
    width = 2048,  # scale : scale down to only one dimension (either height or width, not both)
    height = 2048  # cover : scale down proportionately to given dimensions and crop if neccessary
    )
    resized.to_file(''.join(comprssd_addr))

    # Comment out below line and delete above resizing code to prevent resizing

    # source.to_file(''.join(comprssd_addr))
