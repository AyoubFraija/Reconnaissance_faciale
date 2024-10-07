import cv2
import numpy as np
import os
from PIL import Image

def train_fct():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path="Data"
    def getFacesId(path):
        imagePath = [os.path.join(path, f) for f in os.listdir(path)]
        faces=[]
        id=[]
        for imagePaths in imagePath:
            faceImage = Image.open(imagePaths).convert('L')
            faceNP = np.array(faceImage)
            Id= (os.path.split(imagePaths)[-1].split(".")[0])
            Id=int(Id)
            faces.append(faceNP)
            id.append(Id)
            cv2.imshow("Training",faceNP)
            cv2.waitKey(1)
        return id, faces

    IDs, facedata = getFacesId(path)
    recognizer.train(facedata, np.array(IDs))
    recognizer.write("Trainer.yml")
    cv2.destroyAllWindows()
