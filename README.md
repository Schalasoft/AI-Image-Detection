Tagging Images (for multiple users)

1) Put this folder in C drive so its like (C:/VoTT/sourcesimages)
2) run vott-2.1.0-win32.exe
3) open vott app after installed
4) Setup security key in settings : SECURITY_KEY
5) open 'Yolo.vott' in 'targetimages' folder using vott app
6) label
7) share the 'sourceimages' with each other so we have unified tagged images

Setup Tagging Images for Training
1) Tag images
2) export VoTT
3) Put CSV and images into Data/Source_Images/Training_Images/vott-csv-export, and copy of images into Data/Source_Images/Training_Images/
4) Run 'Convert_to_YOLO_format.py' (this generates the "train.txt" in vott-csv-export)
5) Run 'Download_and_Convert_YOLO_weights.py' (unnecessary I think but do to be sure, get from https://pjreddie.com/media/files/yolov3.weights)

Training
1) Run 'Train_YOLO.py'
2) Wait a LONG time...

Analysis
1) Run 'Detector.py'
2) Check 'TrainYourOwnYOLO/Data/Source_Images/Test_Images/Test_Image_Detection_Results' for analysis results

Post Analysis
1) Check for valid images, moving "bad" ones to a seperate folder for inspection as to what is failing (that might require more tagged images)
2) Run "DetectionResultSanitizer.py" to create "Detection_Results_Sanitized.csv"
Optionally: Run "FixSinaSillyAssFilename.py" for cleaning up incorrect file names, edit as required but it will remove "result" and convert spaces to %20 as expected
3) Run "" to create "exported.csv" to re-train AI using the correctly tagged images from analysis (see step 3 of "Setup Tagging Images for Training")
