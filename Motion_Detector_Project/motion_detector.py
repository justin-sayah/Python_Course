import cv2,time

#For the first pass of the while loop, nothing happens as we need two frames
# in order to comare deltas for motion 
first_frame = None

#Opens video feed from webcam
video = cv2.VideoCapture(0)

while True:
    #Pulls the first frame from the webcam
    check, frame = video.read()

    #Converts the frame to gray for easier analysis
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Applies Gaussian Blur, which is necessary for motion detection
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    #The check to see if the loop is in the first iteration
    if first_frame is None:
        first_frame = gray
        continue

    #Gets a pixel by pixel difference between the current and previous frame, calculates
    #contours and draws a box defined by the contour count
    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30,255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=5)
    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

    #Displays the frame w/ a drawn rectangle
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)

    #Quits Program on 'Q' keypress
    if key == ord('q'):
        break
#Cleanup
video.release()
cv2.destroyAllWindows()