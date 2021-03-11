import cv2
import numpy as np
def hsv():
    cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
    def nothing(x):
        pass

#Create trackbar to adjust HSV range
    cv2.namedWindow("trackbar")
    cv2.createTrackbar("L-H","trackbar",0,179,nothing)
    cv2.createTrackbar("L-S","trackbar",0,255,nothing)
    cv2.createTrackbar("L-V","trackbar",0,255,nothing)
    cv2.createTrackbar("U-H","trackbar",179,179,nothing)
    cv2.createTrackbar("U-S","trackbar",255,255,nothing)
    cv2.createTrackbar("U-V","trackbar",255,255,nothing)

    while True:
        ret,frame =cap.read()
        frame = cv2.flip(frame, 1 )
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)    
    
        l_h=cv2.getTrackbarPos("L-H","trackbar")
        l_s=cv2.getTrackbarPos("L-S","trackbar")
        l_v=cv2.getTrackbarPos("L-V","trackbar")
        h_h=cv2.getTrackbarPos("U-H","trackbar")
        h_s=cv2.getTrackbarPos("U-S","trackbar")
        h_v=cv2.getTrackbarPos("U-V","trackbar")
   
        low=np.array([l_h,l_s,l_v])
        high=np.array([h_h,h_s,h_v])

        mask=cv2.inRange(hsv,low,high) 
        result=cv2.bitwise_and(frame,frame,mask=mask)    
        cv2.imshow("result",result)# If the user presses ESC then exit the program
    
        key = cv2.waitKey(1)
    # If the user presses `s` then print and save this array.
        if key == ord('s'):
            cap.release()
            cv2.destroyAllWindows()
            return (low,high)
            #return 'done'
    #if esc pressed exit
        if key == 27:      
            cap.release()
            cv2.destroyAllWindows()
            return ((0,0),(0,0))
            
