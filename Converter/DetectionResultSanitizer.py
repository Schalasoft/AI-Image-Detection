# Generates sanitized list of detection results: by removing the images in the "bad" image folder that were tagged incorrectly from the detection results csv file

import os
from Converter.ConvertHelper import ConvertHelper
from os import listdir
from os.path import isfile, join

# Get shared global paths from helper
detectionResultBadFolderPath = ConvertHelper.DetectionResultBadFolderPath
detectionResultFolderPath = ConvertHelper.DetectionResultFolderPath
detectionResultFilePath = ConvertHelper.DetectionResultFilePath

# Return a list of the image names in bad result folder
def get_file_names():

    # Make the folder if it doesn't exist, not really necessary as it should exist and if it doesn't this script will do nothing
    if not os.path.exists(detectionResultBadFolderPath):
        os.makedirs(detectionResultBadFolderPath)

    filenames = []

    try:
        files = [f for f in listdir(detectionResultBadFolderPath) if isfile(join(detectionResultBadFolderPath, f))]

        for file in files:
            filename = file.replace('_result','')
            filenames.append(filename)

    finally:
        return filenames

def create_sanitized_detection_results(names):

    try:
        fp = open(detectionResultFilePath)
        fp_sanitized = open(detectionResultFolderPath + 'Detection_Results_Sanitized.csv', 'w+')

        count = 0
        for line in fp:
            # Get file name for checking against compiled list
            name = line.split(',')[0]

            # Ignore CSV header on line 1
            count = count + 1
            if name not in names and count != 1:
                fp_sanitized.write(line)

    finally:
        fp.close()
        fp_sanitized.close()

def main():
    create_sanitized_detection_results(get_file_names())

if __name__ == '__main__':
    main()