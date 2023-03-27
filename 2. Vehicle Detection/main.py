import cv2
import imutils
src='cars.xml' #intitalize file name
car_cascade=cv2.CascadeClassifier(src) #Loading model from xml file cascade classifier
cam=cv2.VideoCapture(1) #Camera initialization
while (1):
    num=0
    flag,frame=cam.read()#read frame
    frame=imutils.resize(frame,width=300)
    #preprocessing(converting to gray)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cars=car_cascade.detectMultiScale(gray,1.1,1) #get coordinate usingdetectMultiScale
    for(x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Frame",frame)
    b=str(len(cars))
    a=int(b)
    num=a
    den=num
    print("________________________")
    print("North : %d "%(den))
    if den>=2:
        print("North More Traffic")
    else:
        print("No Traffic")
    if cv2.waitKey(33)==27:
        break

cam.release()
cv2.destroyAllWindows()



