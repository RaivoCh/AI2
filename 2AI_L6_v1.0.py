#AI for Everyone LESSON 6: Faster Launch of WEBcam and Smoother Video in OpenCV on Windows
#https://www.youtube.com/watch?v=bJIzOniUaAw&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=8

#starting code
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
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release() 