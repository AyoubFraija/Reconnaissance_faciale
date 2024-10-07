import cv2
import pickle 
import numpy as np
import os

def scanner(id):
    # Initialise l'objet de capture vidéo pour capturer la vidéo de la webcam en direct (0 pour la webcam intégrée)
    video=cv2.VideoCapture(0)
    #Chargement du classificateur en cascade Haar pour la detection de visage 
    facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    i=0
    #Boucle pour capturer la vidéo en direct
    while True:
        ret,frame=video.read()
        #Conversion de l'image en niveaux de gris
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #Detection des visages [Renvoie une liste de rectangles où les visages sont détectés]
        faces=facedetect.detectMultiScale(gray,1.3,5)
        #Dessine un rectangle autour de chaque visage détecté
        for x,y,w,h in faces:
            i+=1
            cv2.imwrite('Data/'+str(id)+"."+str(i)+".jpg", gray[y:y+h, x:x+w])
            cv2.putText(frame,str(i),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(218,247,166),1) 
            cv2.rectangle(frame,(x,y),(x+w,y+h),(218,247,166),1) #(x,y) est le coin supérieur gauche du rectangle et (x+w,y+h) est le coin inférieur droit du rectangle

        cv2.imshow('Video',frame)
        k=cv2.waitKey(1)
        if i > 500 :
            break
    video.release()
    cv2.destroyAllWindows()

