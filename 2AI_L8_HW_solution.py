# AI for Everyone LESSON 8: HOMEWORK SOLUTION Calculating Frames Per Second (FPS) in OpenCV
# https://www.youtube.com/watch?v=k7sfK8hdWOA&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=13

import cv2
import time
print(cv2.__version__)
width=640
height=360
myRadius=30
myColor=(0,0,0)
myThick=2
fontH=2
fontT=2
myText='Paul is Boss'
myFont=cv2.FONT_HERSHEY_DUPLEX
upperLeft=(250,140)
lowerRight=(390,220)
lineW=4
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)    #0 for USB cam, CAP_DSHOW - capturing frame and dirrect show
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

tLast=time.time()
fpsFiltred=30    #starting value
time.sleep(.1)    #delay after start to avoid dividing by zero

while True:
    dT=time.time()-tLast
    #print(dT)
    fps=1/dT
    fpsFiltred=fpsFiltred*.97+fps*.03    #low pass filter - .97 is how much i trust the trend and .03 how much i trust measurment
    print(fps)
    tLast=time.time()
    ignore,  frame = cam.read()
    frame[140:220,250:390]=(255,0,0)
    cv2.rectangle(frame,upperLeft,lowerRight,(0,255,0),lineW)
    cv2.circle(frame,(int(width/2),int(height/2)),myRadius,myColor,myThick)
    #cv2.putText(frame,myText,(120,60),myFont,fontH,(0,0,255),fontT)
    cv2.rectangle(frame,(0,0),(120,40),(255,0,255),-1)    #-1 for solid box
    cv2.putText(frame,str(int(fpsFiltred))+" fps",(5,30),myFont,1, (0,255,255), 2)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
