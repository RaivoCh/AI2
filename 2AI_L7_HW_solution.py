#AI for Everyone LESSON 7: HOMEWORK SOLUTION, Creating Checkerboard Pattern in OPENCV
#https://www.youtube.com/watch?v=Fpqa5mcHoTE&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=16

##HOMEWORK
#chessboard
#chessboar is square, so same number of rows and colums
#homework solution
#this solution does not work for even number of squares, not solved or mentioned in video

import cv2
print(cv2.__version__)
import numpy as np

boardSize=int(input("what size is your board? "))    #user input
numSquare=int(input("how many squares? "))
squareSize=int(boardSize/numSquare)

darkColor=(0,0,0)
lightColor=(0,0,255)
nowColor=darkColor

while True:
    x=np.zeros([boardSize,boardSize,3],dtype=np.uint8)

    for row in range(0,numSquare):
        for column in range(0,numSquare):
            x[squareSize*row:squareSize*(row+1),squareSize*column:squareSize*(column+1)]=nowColor
            if nowColor==darkColor:
                nowColor=lightColor
            else:
                nowColor=darkColor
        
        if nowColor==darkColor:    #at the end of inner loop we must flip, or result will be stripes
            nowColor=lightColor
        else:
            nowColor=darkColor


    cv2.imshow("my checkerboard" ,x)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break