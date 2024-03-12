# AI for Everyone LESSON 8: Putting Text, Rectangles and Circles on Images in OpenCV
# https://www.youtube.com/watch?v=97HA3NeYjus&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=12

import cv2
print(cv2.__version__)
width=640
height=360
myRadius=30
myColor=(0,0,0)
myThick=2
fontH=1
fontT=1
myText="Paul is Boss"
myFont=cv2.FONT_HERSHEY_DUPLEX
upperLeft=(240,140)
lowerRight=(390,220)
lineW=4

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)    #0 for USB cam, CAP_DSHOW - capturing frame and dirrect show
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)   #set frames per second
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))    #codec
while True:
    ignore,  frame = cam.read()
    #row column
    frame[140:220,250:390]=(255,0,0)     #solid box
    #there is easier way. manipulating with these pixels, this case creates black square in the middle
    cv2.rectangle(frame,upperLeft,lowerRight,(0,255,0),lineW)    #upper left lower right position, color, thickness
    #cv2.rectangle(frame,(250,140),(390,220),(0,255,0),-1)    #-1 for solid box
    cv2.circle(frame,(int(width/2),int(height/2)),myRadius,myColor,myThick)    #circle position in XY!, radius
    cv2.putText(frame,myText,(120,60),myFont,fontH,(0,0,255),fontT)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()