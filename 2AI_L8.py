# AI for Everyone LESSON 8: Putting Text, Rectangles and Circles on Images in OpenCV
# https://www.youtube.com/watch?v=97HA3NeYjus&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=12

import cv2
print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)    #0 for USB cam, CAP_DSHOW - capturing frame and dirrect show
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)   #set frames per second
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))    #codec
while True:
    ignore,  frame = cam.read()
    #row column
    #frame[140:220,250:390]=(0,0,0)     #there is easier way. manipulating with these pixels, this case creates black square in the middle
    cv2.rectange(frame,(250,140),(390,220))    #upper left lower right position
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()