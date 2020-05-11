from imageai.Detection import ObjectDetection
import os

def CustomDetection(detector, inputpath, execution_path):
    imagestoprocess = 10

    custom_objects = detector.CustomObjects(cannon=True, mask=True)
    x = 0
    for image in range(imagestoprocess):
        x = x + 1
        detections = detector.detectCustomObjectsFromImage(custom_objects=custom_objects, input_image=os.path.join(execution_path ,
        f'..\locus\image ({x}).jpg'), output_image_path=os.path.join(execution_path , f'rendered\imagenew{x}.jpg'), minimum_percentage_probability=30)

    for eachObject in detections:
        print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
        print("--------------------------------")

def Detection(detector, inputpath, execution_path):
    imagestoprocess = 10

    x = 0
    for image in range(imagestoprocess):
        x = x + 1
        detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , f'..\locus\image ({x}).jpg'), output_image_path=os.path.join(execution_path , f'rendered\imagenew{x}.jpg'))

    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )

#inputpath = 'inputitems.h5'
inputpath = 'resnet50_coco_best_v2.0.1.h5'

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , inputpath))
detector.loadModel()

CustomDetection(detector, inputpath, execution_path)
#Detection(detector, inputpath, execution_path)
