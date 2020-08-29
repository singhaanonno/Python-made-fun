# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:55:57 2020

@author: Anonno
"""

import numpy as np
import cv2
import pyautogui

cap=cv2.VideoCapture(0)

yellow_lower=np.array([22,93,0])
yellow_upper=np.array([45,255,255])
prev_y=0

while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv, yellow_lower, yellow_upper)
    contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contours, -1, (0,255,0),2)
    
    for c in contours:
        area=cv2.contourArea(c)
        if area >300:
          #qprint(area)
            #cv2.drawContours(frame, c, -1, (0,255,0),2)
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
            if y< prev_y:
          #     print('moving down')
                pyautogui.press('space')
          # else:
          #     print('doing nothing')
            prev_y=y
    
    #cv2.imshow('mask',mask)
    cv2.imshow('frame', frame)
    if cv2.waitKey(10)==ord('q'): # If we press q , our webcam will be closed
        break
    
cap.release()
cv2.destroyAllWindows()
    