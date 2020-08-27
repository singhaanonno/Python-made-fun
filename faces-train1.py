# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 03:19:41 2020

@author: Anonno
"""


import cv2
import os
from PIL import Image
import numpy as np
import pickle


BASE_DIR=os.path.dirname(os.path.abspath(__file__)) #It actually gives us the path of this python file,where is it located 
image_dir=os.path.join(BASE_DIR,'project')          # our image dir should be in that path

face_cascade=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

recognizer=cv2.face.LBPHFaceRecognizer_create()
current_id=0
label_ids={}
y_labels=[]
x_train=[]

#print(BASE_DIR)
#print(image_dir)

for root,dirs,files in os.walk(image_dir):     # os.path.dirname(path)=root
    for file in files:
        if file.endswith('png') or file.endswith('jpg'):
            path=os.path.join(root,file)
            label=os.path.basename(os.path.dirname(path)).replace(' ',',').lower() #Lebels from directories # We wanna get the lebel name means the folder name
           #print(label)                                 # we wanna ommit any type of space in our folder name and name it with all small letters
           #print(path)
            
            if not label in label_ids:
                label_ids[label]=current_id
                current_id+=1
            id_=label_ids[label]
           #print(label_ids)
            print(id_)
            
           #y_labels.append(label)  #some number
           #x_train.append(path)    # verify this image,turn into a NUMPY array,GRAY
            pil_image=Image.open(path).convert('L') # Turn into grayscale
            
                # Now we have to resize the images
            
            size=(400,400)
            final_image=pil_image.resize(size,Image.ANTIALIAS)
            image_array=np.array(final_image,"uint8") # Turning into a numpy array
           #print(image_array)  # We basically converted images into numbers
            
           #Region of interest in training data
           
            faces=face_cascade.detectMultiScale(image_array,scaleFactor=1.5,minNeighbors=5)
            
            for(x,y,w,h) in faces:
                roi=image_array[y:y+h,x:x+h] # here roi=region of interest
                x_train.append(roi)
                y_labels.append(id_)
                
#Creating traing labels
#print(y_labels)
#print(x_train)

    
# using picle to label ids         

with open("labels.pickle",'wb') as f:
    pickle.dump(label_ids,f)
    
#Train the OpenCV Recognizer
recognizer.train(x_train,np.array(y_labels))
recognizer.save('trainner.yml')
        
          
#print(dir(cv2.face))          
            
# You may have problem with cv2.cv2 has no attribute face
# To slove this problem,open powershell
# Then write this following command-
''' pip uninstall opencv-python
    pip install opencv-contrib-python'''
# make sure to close your IDE before writting those commands
# Else you will notice winerror 5 access is denied error           
       

            
            
            
            
            
            