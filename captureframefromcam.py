# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 17:44:41 2016

@author: chyam
"""

import cv2

def main():
    cv2.namedWindow("camera")
    vc = cv2.VideoCapture(0)
    
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False
    
    counter = 0
    
    while rval:
        cv2.imshow("camera", frame)
        rval, frame = vc.read()
    
        if cv2.waitKey(1) == 27: # exit on ESC
            break
        
        elif cv2.waitKey(1) == 32: # save frame on Spacebar
            # save the frame to an image file
            filename = "face"+str(counter)+".jpg"
            print(filename)
            cv2.imwrite(filename, frame)
            counter = counter + 1
        
    vc.release()
    cv2.destroyWindow("camera")
    
    return
    
################################
if __name__ == "__main__":
	main()
