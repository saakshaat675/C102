import cv2
import random

# number = random.randint(0,100)

# print(number)


def snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result=True
    while (result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
     

        
        cv2.imwrite(img_name,frame)
        result=False    

    videoCaptureObject.release()
    cv2.destroyAllWindows()

snapshot()
