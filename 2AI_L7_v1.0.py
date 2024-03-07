#AI for Everyone LESSON 7: Understanding Pictures and Images as Data Arrays
#https://www.youtube.com/watch?v=W43MpRroplA&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=10

##
import cv2
print(cv2.__version__)
import numpy as np

while True:
    frame=np.zeros([1000, 1000,3],dtype=np.uint8)
    frame[:,:]=(0,0,125)
    frame[:,0:125]=(0,255,0)
    cv2.imshow("my window",frame)
    if cv2.waitKey(1) & 0xff==ord("q"):
        break
        