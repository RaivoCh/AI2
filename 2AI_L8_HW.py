# AI for Everyone LESSON 8: Putting Text, Rectangles and Circles on Images in OpenCV
# https://www.youtube.com/watch?v=97HA3NeYjus&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=12

#homework - make framerate counter (frames per second) and display it in frame
#hint: one whole loop is one processed frame

#works

import cv2
import time

print(cv2.__version__)
width=640
height=360
fontH=1
fontT=1
myFont=cv2.FONT_HERSHEY_DUPLEX
myText = str("BAF")
fps = int()
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)    #0 for USB cam, CAP_DSHOW - capturing frame and dirrect show
#cam=cv2.VideoCapture(1,cv2.CAP_DSHOW)    #0 for USB cam, CAP_DSHOW - capturing frame and dirrect show
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)   #set frames per second
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))    #codec
while True:
    start_time=time.time()
    ignore,  frame = cam.read()    
    cv2.putText(frame,str(fps),(580,40),myFont,fontH,(0,0,255),fontT)
    cv2.imshow('my WEBcam', frame)   #this must be at the end, to say what all should show
    cv2.moveWindow('my WEBcam',0,0)
    end_time = time.time()
    if start_time != end_time:
        fps = round(1/(end_time-start_time))
    print("FPS: ",fps)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()

