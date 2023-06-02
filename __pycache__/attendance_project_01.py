import cv2
import numpy as np
import face_recognition



#ww are gating image as bgr but libary understand it as rgb (convert)

imgElon=face_recognition.load_image_file("images/elon musk.jpg")
#imgElon=cv2.resize(imgElon,(500,500))
imgElon=cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)

imgTest=face_recognition.load_image_file("images/elon musk test.jpg")
#imgTest=cv2.resize(imgTest,(500,500))
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceloc=face_recognition.face_locations(imgElon)[0]
encodeElon=face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon,(faceloc[3],faceloc[0],faceloc[1],faceloc[2]),(255,0,255),2)
#print(faceloc) (top ,,right bottam left) (255,0,255= purple)thickness

facelocTest=face_recognition.face_locations(imgTest)[0]
encodeTest=face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(facelocTest[3],facelocTest[0],facelocTest[1],facelocTest[2]),(255,0,255),2)

results= face_recognition.compare_faces([encodeElon],encodeTest)
faceDis=face_recognition.face_distance([encodeElon],encodeTest)
print(results,faceDis)
#to see where we detect the faces (0,0,255 =
cv2.putText(imgTest,f'{results}{round(faceDis[0],2)}',(30,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
#(0,0,255=red)

cv2.imshow('Elon Musk',imgElon)
cv2.imshow('Elon Musk',imgTest)
cv2.waitKey(0)

