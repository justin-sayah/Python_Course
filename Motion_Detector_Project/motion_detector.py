import cv2,time, pandas
from datetime import datetime

#For the first pass of the while loop, nothing happens as we need two frames
# in order to comare deltas for motion 
first_frame = None

#Creates a list of timestamps where there is motion vs no motion, 0 = no motion, 1 = motion
status_list = [None, None]
times = []

#Create Dataframe to hold start and end times for motion objects
df = pandas.DataFrame(columns=["Start", "End"])

#Opens video feed from webcam
video = cv2.VideoCapture(0)

while True:
    #Pulls the first frame from the webcam
    check, frame = video.read()

    #status: 0 = no motion in the frames, 1 = motion in frames
    status = 0
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

    #If the environment status changes, then the entry and exit times are logged in the list
    status = 1

    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    #Displays the frame w/ a drawn rectangle
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)

    #Quits Program on 'Q' keypress
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

#Places all start and end times for objects into a csv
for i in range(0,len(times),2):
    df = df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")

#Cleanup
video.release()
cv2.destroyAllWindows()