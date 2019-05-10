
import cv2  
import time
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
cap = cv2.VideoCapture(0) 

arr=0;
counter=0;
X_list=[3,30,60,90,120,150,180,200,220,240,260,290,310,340,350,370,390,410,430,470]
Y_list=[10,40,70,120,140,160,220,250,280,320,350,370,400,420,440,480,510,540,600,625]
checker_len=20
prev_frame=np.zeros((480,640))
curr_frame=np.zeros((480,640))
counter=0
thresh_hold=100
while 1:
    #time.sleep(0.5) 
   
    ret, img = cap.read()
    
   
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    curr_frame=gray

    j=0
    f=0
    curr_sum=0
    #print curr_sum
    while j<checker_len:
    	temp=np.int64(curr_frame[X_list[j]][Y_list[j]])-np.int64(prev_frame[X_list[j]][Y_list[j]])
    	if temp < 0:
    		temp=temp*-1
    	curr_sum=curr_sum+temp
    		
    	j=j+1
    print curr_sum

    prev_frame=curr_frame

    if curr_sum>50:
    	print "cloud called"

    # Detects faces of different sizes in the input image 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #print type(gray)
  
    for (x,y,w,h) in faces: 
        # To draw a rectangle in a face  
        #counter=counter+1;
        #print counter
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 
   
   
    cv2.imshow('img',img) 
  
    # Wait for Esc key to stop 
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
  
# Close the window 
cap.release() 
  
# De-allocate any associated memory usage 
cv2.destroyAllWindows()
print arr
