import cv2
import time

def detecter(name_list, username):
    
    # Initialise l'objet de capture vidéo pour capturer la vidéo de la webcam en direct (0 pour la webcam intégrée)
    video=cv2.VideoCapture(0)
    #Chargement du classificateur en cascade Haar pour la detection de visage 
    facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("Trainer.yml")

    starting_time=None

    #Boucle pour capturer la vidéo en direct
    while True:
        ret,frame=video.read()
        #Conversion de l'image en niveaux de gris
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #Detection des visages [Renvoie une liste de rectangles où les visages sont détectés]
        faces=facedetect.detectMultiScale(gray,1.3,5)
        #Dessine un rectangle autour de chaque visage détecté
        for x,y,w,h in faces:
            serial, conf = recognizer.predict(gray[y:y+h, x:x+w])
            if conf<50 :
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
                cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
                cv2.putText(frame,name_list[serial],(x+1, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
                if name_list[serial] == username:
                    if starting_time is None:
                        starting_time = time.time()  
                    elapsed_time = time.time() - starting_time
                    cv2.putText(frame, "{} seconds".format(int(elapsed_time)), (10, 50), cv2.FONT_HERSHEY_SIMPLEX,0.8, (50,50,255), 2)
                    if elapsed_time > 5:
                        video.release()
                        cv2.destroyAllWindows()
                        return True, name_list[serial]
            else:
                starting_time=None
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
                cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
                cv2.putText(frame, "Unknown", (x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
        frame=cv2.resize(frame, (640, 480))
        cv2.imshow('Video',frame)
        k=cv2.waitKey(1)

        if k==ord('o') and conf>50:
            time.sleep(10)
        if k==ord('q'):
            break
  
    video.release()
    cv2.destroyAllWindows()
    return False, None

