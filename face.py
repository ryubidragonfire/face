# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 17:44:41 2016

@author: chyam
"""

import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    if cv2.waitKey(20) == 27: # exit on ESC
        break
cv2.destroyWindow("preview")