#AI for Everyone LESSON 7: Understanding Pictures and Images as Data Arrays
#https://www.youtube.com/watch?v=W43MpRroplA&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=10

##HOMEWORK
#chessboard
#chessboar is squere, so same number of rows and colums


import cv2
print(cv2.__version__)
import numpy as np

sizeB = 250    #size of board (pixels)
row_col = 8    #number of rows/columns of chessboard

rowSize = int(sizeB//row_col)    #size of one square

if sizeB%row_col != 0:
    sizeB=row_col * rowSize


while True:
    frame=np.zeros([sizeB, sizeB,3],dtype=np.uint8)

    for i in range(0,row_col,2):
        
    #    frame[2*i*rowSize:rowSize+i*2*rowSize,2*i*rowSize:rowSize+i*2*rowSize]=(0,0,125)
        frame[i*rowSize:i+1*rowSize,rowSize:]=(0,0,125)
    #    frame[:,2*i*rowSize:rowSize+i*2*rowSize]=(0,0,125)
        print(i)
    
    cv2.imshow("my window",frame)
    if cv2.waitKey(1) & 0xff==ord("q"):
        break
        