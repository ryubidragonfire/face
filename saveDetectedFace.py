# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 17:44:41 2016
Purpose: Detect face using Haar Cascade from camera, save detected face region only.

@author: chyam
"""

import cv2

# find faces in a frame using Haar Cascade
def detectFace(frame):
    found = False
    rect_frame = None
    crop_frame = None
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    
    # Draw a rectangle around the faces
    if(len(faces) > 0):
        found = True
        rect_frame = frame.copy()
        for (x, y, w, h) in faces:
            cv2.rectangle(rect_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            crop_frame = frame[y:y+h, x:x+w];

    return found, rect_frame, crop_frame

    
def main():
    cv2.namedWindow("camera")
    cv2.namedWindow("detect face")
    vc = cv2.VideoCapture(0)
    
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False
    
    counter = 0
    
    while rval:
        cv2.imshow("camera", frame)
        rval, frame = vc.read()
    
        found, rect_frame, crop_frame = detectFace(frame)
        
        if cv2.waitKey(1) == 27: # exit on ESC
            break
        
        elif found:
            cv2.imshow("detect face", rect_frame)
            if cv2.waitKey(1) == 32: # save frame on Spaceba
                filename = "face"+str(counter)+".jpg"; print(filename)
                cv2.imwrite(filename, crop_frame) # save detected face region only
                counter = counter + 1
           
    vc.release()
    cv2.destroyWindow("camera")
    cv2.destroyWindow("detect face")

################################
if __name__ == "__main__":
	main()

    