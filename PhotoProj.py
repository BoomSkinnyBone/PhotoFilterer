import shutil
import os



def CopyImage(source_address, destination, image_name):

    jpg = image_name + ".JPG"
    raw = image_name + ".NEF"

    srcpath = os.path.join(source_address, jpg)
    dstpath = os.path.join(destination, jpg)

    shutil.copy(srcpath, dstpath)


    srcpath = os.path.join(source_address, raw)
    dstpath = os.path.join(destination, raw)

    shutil.copy(srcpath, dstpath)



source_address = r"P:\StreetPhotography\Outings\Away Day Imperial"
destination = r"P:\StreetPhotography\Outings\Away Day Imperial\Best"



#picture = "DSC_" + "7463"# To change the number in the middle to reading from a text file

file = open("PicsNames.txt")
arr = file.readlines()
arr = [line.rstrip("\n") for line in arr]


for num in arr:
        picture = "DSC_" + num
        CopyImage(source_address, destination, picture)
file.close()

#CopyImage(source_address, destination, picture)

