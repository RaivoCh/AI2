#AI for Everyone LESSON 6: Faster Launch of WEBcam and Smoother Video in OpenCV on Windows
#https://www.youtube.com/watch?v=bJIzOniUaAw&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=8

#starting code
import cv2
print(cv2.__version__)
cam=cv2.VideoCapture(1)
while True:
    ignore,  frame = cam.read()
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()