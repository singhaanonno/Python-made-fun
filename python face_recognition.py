import face_recognition
import cv2

imgarpi=face_recognition.load_image_file('divai2.jpg')
imgarpi=cv2.cvtColor(imgarpi,cv2.COLOR_BGR2RGB)  # Convert into RGB color

imgtest=face_recognition.load_image_file('divai.jpg')
imgtest=cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)  # Convert into RGB color
#.......................................................................................................................
#Finding the faces in our images and finding their encoadings as well
faceloc=face_recognition.face_locations(imgarpi)[0]
encodearpi=face_recognition.face_encodings(imgarpi)[0]
print(faceloc)
cv2.rectangle(imgarpi,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),4)

faceloctest=face_recognition.face_locations(imgtest)[0]
encodetest=face_recognition.face_encodings(imgtest)[0]
print(faceloctest)
cv2.rectangle(imgtest,(faceloctest[3],faceloctest[0]),(faceloctest[1],faceloctest[2]),(255,0,255),4)
#.......................................................................................................................

results=face_recognition.compare_faces([encodearpi],encodetest)
print(results)
facedis=face_recognition.face_distance([encodearpi],encodetest)  # to see how much dissimilarity lies between the images
print(facedis)                                                   # the lower the distance the better the similarity is




cv2.putText(imgtest,f'{results} {round(facedis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.imshow('Arpita1',imgarpi)
cv2.imshow('Arpita2',imgtest)

cv2.waitKey(0)

