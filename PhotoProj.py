import shutil
import os



def CopyImage(source_address, destination, image_name):

    jpg = image_name + ".JPG"
    raw = image_name + ".NEF" # The NIKON RAW file extension

    srcpath = os.path.join(source_address, jpg)
    dstpath = os.path.join(destination, jpg)

    shutil.copy(srcpath, dstpath)


    srcpath = os.path.join(source_address, raw)
    dstpath = os.path.join(destination, raw)

    shutil.copy(srcpath, dstpath)



source_address = r"PATH_TO_ALL_PICS"
destination = r"PATH_TO_FOLDER_FOR_FILTERED_PICS"



file = open("PicsNames.txt")
arr = file.readlines()
arr = [line.rstrip("\n") for line in arr]


for num in arr:
        picture = "DSC_" + num
        CopyImage(source_address, destination, picture)
file.close()

