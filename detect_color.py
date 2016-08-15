# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

# define the list of boundaries
boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
]

def red(image):
    boundaries = [([0, 0, 110], [50, 50, 255]),]
    lower, upper = boundaries[0]
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)
    return output
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    #image = cv2.imread(frame)
    frame =cv2.blur(frame, (11,11)) 
    frame =cv2.medianBlur(frame, 41) 

    cv2.imshow('keypoints',  red(frame))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
