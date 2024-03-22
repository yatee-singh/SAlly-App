import cv2
import numpy as np

# define range of red color in HSV
lower_clr1=np.array([])
upper_clr1=np.array([])
clr1=""
    
# define range of green color in HSV
lower_clr2=np.array([])
upper_clr2=np.array([])
clr2=""
    
# define range of blue color in HSV
lower_clr3=np.array([])
upper_clr3=np.array([])
clr3=""

lang = input("Which Experiment? (1-6)")
print(lang)

match lang:
    case "1":
        lower_clr1=np.array([0, 50, 50])
        upper_clr1=np.array([10, 255, 255])
        clr1="red"
            
        # define range of green color in HSV
        lower_clr2=np.array([0, 0, 0])
        upper_clr2=np.array([0, 0, 0])
        clr2=""
            
        # define range of blue color in HSV
        lower_clr3=np.array([0, 0, 0])
        upper_clr3=np.array([0, 0, 0])
        clr3=""

    case "2":
        lower_clr1=np.array([40, 20, 50])
        upper_clr1=np.array([90, 255, 255])
        clr1="green"
            
        # define range of green color in HSV
        lower_clr2=np.array([0, 0, 0])
        upper_clr2=np.array([0, 0, 0])
        clr2=""
            
        # define range of blue color in HSV
        lower_clr3=np.array([0, 0, 0])
        upper_clr3=np.array([0, 0, 0])
        clr3=""

    case "3":
        lower_clr1=np.array([100, 50, 50])
        upper_clr1=np.array([130, 255, 255])
        clr1="blue"
            
        # define range of green color in HSV
        lower_clr2=np.array([0, 0, 0])
        upper_clr2=np.array([0, 0, 0])
        clr2=""
            
        # define range of blue color in HSV
        lower_clr3=np.array([0, 0, 0])
        upper_clr3=np.array([0, 0, 0])
        clr3=""
    
    case "4":
        lower_clr1=np.array([0, 50, 50])
        upper_clr1=np.array([10, 255, 255])
        clr1="red"
            
        # define range of green color in HSV
        lower_clr2=np.array([0, 0, 0])
        upper_clr2=np.array([0, 0, 0])
        clr2=""
            
        # define range of blue color in HSV
        lower_clr3=np.array([0, 0, 0])
        upper_clr3=np.array([0, 0, 0])
        clr3=""

    case "5":
        lower_clr1=np.array([0, 50, 50])
        upper_clr1=np.array([10, 255, 255])
        clr1="red"
            
        lower_clr2=np.array([0, 0, 0])
        upper_clr2=np.array([0, 0, 0])
        clr2=""
            
        # define range of blue color in HSV
        lower_clr3=np.array([0, 0, 0])
        upper_clr3=np.array([0, 0, 0])
        clr3=""
    case "6":
        lower_clr1=np.array([0, 50, 50])
        upper_clr1=np.array([10, 255, 255])
        clr1="red"
            
        lower_clr2=np.array([0, 0, 0])
        upper_clr2=np.array([0, 0, 0])
        clr2=""
            
        # define range of blue color in HSV
        lower_clr3=np.array([0, 0, 0])
        upper_clr3=np.array([0, 0, 0])
        clr3=""



cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
print(lower_clr1)
while True:
   


    _,img = cap.read()
    img_bcp = img.copy()
  
    img = cv2.resize(img, (640, 480))
    # Make a copy to draw contour outline
    input_image_cpy = img.copy()
 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
    
 
    # create a mask for red color
    mask_red = cv2.inRange(hsv, lower_clr1, upper_clr1)
    # create a mask for green color
    mask_green = cv2.inRange(hsv, lower_clr2, upper_clr2)
    # create a mask for blue color
    mask_blue = cv2.inRange(hsv, lower_clr3, upper_clr3)
 
    # find contours in the red mask
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # find contours in the green mask
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # find contours in the blue mask
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 
    # loop through the red contours and draw a rectangle around them
    for cnt in contours_red:
        contour_area = cv2.contourArea(cnt)
        if contour_area > 1000:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, clr1, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
 
    # loop through the green contours and draw a rectangle around them
    for cnt in contours_green:
        contour_area = cv2.contourArea(cnt)
        if contour_area > 1000:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, clr2, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
 
    # loop through the blue contours and draw a rectangle around them
    for cnt in contours_blue:
        contour_area = cv2.contourArea(cnt)
        if contour_area > 1000:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, clr3, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
  
    cv2.imshow('Color Recognition Output', img)
     
    # Close video window by pressing 'x'
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break