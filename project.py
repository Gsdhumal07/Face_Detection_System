import numpy as np
import face_recognition
import os
from datetime import  datetime

class student:
    path="ImageAttendance"
    images=[]
    classNames=[]
    mylist = os.listdir(path)
    print(mylist)


    

    for cl in mylist:
        curImg=cv2.imread(f"{path}/{cl}")

    
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    def findEncodings(images):
        encodeList=[]
        for img in images:
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            encode=face_recognition.face_encodings(img)[0]
            encode=face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    
    
       
        
        
    

    def markattendance(name):
        with open('Attendance.csv','r') as f:
            myDataList= f.readline()
            nameList = []
            for line in myDataList:
                entry=line.split(',')
                nameList.append(entry[0])

           
            
            if name not in nameList:
                now = datetime.now()
                dtstrings= now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtstrings}')


    encodeListKnown=findEncodings(images)
    print("Encoding Complect")

    cap=cv2.VideoCapture(0)

    while True:
        success , img= cap.read()
        imgS= cv2.resize(img,(0,0),None,0.25,0.25)
        imgS= cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame=face_recognition.face_locations(imgS)
        encodesCurframe = face_recognition.face_encodings(imgS,facesCurFrame)

        for encodeFace,faceloc in zip(encodesCurframe,facesCurFrame):
            matches=face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)
            #print(faceDis)
            matchIndex=np.argmin(faceDis)

            if matches[matchIndex]:
                name= classNames[matchIndex].upper()
                print(name)
                y1,x2,y2,x1=faceloc
                y1, x2, y2, x1= y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y1-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

                markattendance(name)

        cv2.imshow("Webcam",img)
        cv2.waitKey(1)


