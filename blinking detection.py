import numpy as np
import cv2 as cv
from pynput.mouse import Listener
import os

def blink_detection():
    
    count = 0

    face_cascade = cv.CascadeClassifier('venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml') # path to haarcascade_frontalface_default.xml
    eye_cascade = cv.CascadeClassifier('venv\Lib\site-packages\cv2\data\haarcascade_eye.xml') #path to haarcascade_eye.xml
    
    vid = cv.VideoCapture(0)

    while vid:
        count += 1
        _,img = vid.read()
        img = cv.flip(img,1)
        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,3,4)
        
        for (fx,fy,fw,fh) in faces :
            fx2 = fx+fw
            fy2 = fy+fh
            cv.rectangle(img,pt1=(fx,fy),pt2=(fx2,fy2),color=(0,255,55))
            f_gray = gray[fy:fy2,fx:fx2]
            f_color = img[fy:fy2,fx:fx2]
            eyes = eye_cascade.detectMultiScale(f_gray,1.1,3,4)
            
            for (ex,ey,ew,eh) in eyes:
                count = 0
                cv.rectangle(f_color,(ex,ey),(ex+ew,ey+eh),(255,0,255),2)
    
            if count == 600:
                os.system('cls')
                print("Are you not there ?")
                moved = mouse_movement()
                
                if moved:
                    print("yes you are")
                    count = 0 

        cv.namedWindow("img",cv.WINDOW_NORMAL)
        cv.resizeWindow("img",600,450)
        cv.imshow("img",img)
        if cv.waitKey(1) & 0xff == ord('q'):
                break
    vid.release()
    cv.destroyAllWindows()
        
def mouse_movement():
    def on_move(x,y):
        if (x,y):
            listener.stop()
    with Listener(on_move=on_move) as listener:
        listener.join()
    return True

blink_detection()