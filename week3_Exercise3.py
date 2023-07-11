import sys
#at least python 3.7
assert sys.version_info >= (3, 7)

import numpy as np
import cv2 as cv
cap = cv.VideoCapture('videos/img_pexels.mp4')

# Check if the object has been created successfully
if not cap.isOpened():
    sys.exit("No such file")
    
#parameters: filepath, fourcc, fps, frame width and height
fourcc = cv.VideoWriter_fourcc("M", "J", "P", "G")#fourcc is an identifier for the algorithm which compress and decompress the video
fps = 15
w, h = int(resized_frame.shape[1]), int(resized_frame.shape[0])
out = cv.VideoWriter("smaller_img_pexels.avi", fourcc, fps, (w,h))


# Read the frames with loop
while True:
    ret, frame = cap.read()#ret is the status, frame is the image
    
    if not ret:
        print("No frame detected")
        break
    resized_frame = cv.resize(frame, None,fx=0.5, fy=0.5)
    
    out.write(resized_frame)
    cv.imshow("frame", resized_frame)
    k = cv.waitKey(1) &0xFF
    if k == 27:
        break
        
cap.release()
out.release()
cv.destroyAllWindows()
