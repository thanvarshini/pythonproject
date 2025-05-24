import cv2
import time


def minimizeWindow():
    import win32gui,win32con
    window =win32gui.GetForegroundWindow()
    win32gui.ShowWindow(window,win32con.SW_MINIMIZE)


def cctv():
    video = cv2.VideoCapture(0)
    video.set(3,640)
    video.set(4,480)
    width=video.get(3)
    height=video.get(4)
    print("video is getting started",width,'x',height)
    print("help-- \n1. Press esc key to exit. \n2. Press m to minimize.")
    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    date_time=time.strftime("recording %H-%M-%d-%m,%y")
    output=cv2.VideoWriter('footages'+date_time+'.mp4',fourcc,20.0,(640,480))
    while video.isOpened():
        check,frame1=video.read()
        check,frame2=video.read()
        diff=cv2.absdiff(frame1,frame2)
        gray=cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
        blur=cv2.GaussianBlur(gray,(5,5),0)
        _, thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
        dilated=cv2.dilate(thresh,None, iterations=3)
        contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(frame1,contours,-1,(0,255,0),2)
        for c in contours:
            if cv2.contourArea(c)<5000:
                continue
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame1
                          ,(x,y),(x+w,y+h),(0,255,0),2)
        if check==True:
            frame=cv2.flip(frame1,1)

            t=time.ctime()
            cv2.rectangle(frame,(5,5,100,20),(255,255,255),cv2.FILLED)
            cv2.putText(frame,"camera 1",(20,20),cv2.FONT_HERSHEY_DUPLEX,0.5,(5,5,5),1)
            cv2.putText(frame,t,(420,460),cv2.FONT_HERSHEY_DUPLEX,0.5,(5,5,5),1)
            cv2.imshow('CCTV camera',frame1)
            output.write(frame)
            if cv2.waitKey(10)==27:
                print(" video footage is stored in current directory")
                break
            elif cv2.waitKey(10) == ord('m'):
                minimizeWindow()
        else:
            print("cctv isn't recording , check configuration")
            break
    video.release()
    output.release()
    cv2.destroyAllWindows()
    
def fun(a):
    print("******************************************************")
    a()
    print("******************************************************")

@fun
def msg():
     print("welcome to cctv software")

a= int(input("do you want to open the cctv? \n1.Yes \n2.No\n>>>"))

if a==1:
    cctv()
elif a==2:
    print("required your access to start the cctv camera")
    exit


























    
        
                
                
                
                

    

    
    
    
    
