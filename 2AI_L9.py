# AI for Everyone LESSON 9: Understanding Region of Interest (ROI) in OpenCV
# https://www.youtube.com/watch?v=E46B7NPWK38&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=14

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
    frameROI = frame[150:210,250:390]    #region fo interest si now box in the middle 80x140 
    frameROIGray = cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)     #if I cut out part of the original BRG image, I make GRAY
    frameROIBGR = cv2.cvtColor(frameROIGray,cv2.COLOR_GRAY2BGR) #  if I want to insert back into the original, I have to
                                                                #  convert back to BRG or it'll throw an error:
                                                                #  "ValueError: could not broadcast input array 
                                                                #  from shape (60,140) into shape (60,140,3)"
                                                                #  because BRG has three color values, but GRAY has only one
    cv2.imshow("my BRG ROI", frameROIBGR)    #show my new gray frame, that has three colour values
    cv2.moveWindow("my BRG ROI", 650,180)

    frame[150:210,250:390] = frameROIBGR    #little gray spot in the middle of the original frame
    cv2.imshow("my ROI", frameROI)    #show my new frame
    cv2.moveWindow("my ROI", 650,0)    # and move it away from original frame

    cv2.imshow("my Gray ROI", frameROIGray)    #show my new gray frame
    cv2.moveWindow("my Gray ROI", 650,90)    # and move it away from original frame


    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release() 