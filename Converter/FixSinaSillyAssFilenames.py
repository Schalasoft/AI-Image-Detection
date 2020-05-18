import os
from os import listdir
from os.path import isfile, join

try:
    image_path = "../Data/Source_Images/Test_Image_Detection_Results/"

    files = [f for f in listdir(image_path) if isfile(join(image_path, f))]

    for file in files:
        fixed_name = file.replace(' (', '%20(')
        fixed_name = file.replace('result', '')
        os.rename(image_path + file, image_path + fixed_name)

finally:
    print("wubbalubbadubdub")