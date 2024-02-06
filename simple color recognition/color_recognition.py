#https://pysource.com/2021/10/19/simple-color-recognition-with-opencv-and-python/
import cv2
print(cv2.__version__)

cap=cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,1200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
while True:

    _,frame=cap.read()
    h,w,_=frame.shape
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cx=int(w/2)
    cy=int(h/2)
    pixelCenter=hsv_frame[cy,cx]
    
    hue_value = pixelCenter[0]

    color = "Undefined"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "RED"
    
    pixel_center_bgr = frame[cy, cx]
    
   
    cv2.putText(frame, color, (cx - 200, 100), 0, 3, (0, 0, 0), 5)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
    
    cv2.imshow("Frame", frame)
    key=cv2.waitKey(1)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()