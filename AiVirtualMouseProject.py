import cv2
import numpy as np
import hand_tracking_module as htm
import time
import autopy

#######################

wCam, hCam = 640, 480
frameR = 100 #framereduction
smoothening = 8

#######################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
print(wScr, hScr)

while True:
    #1.find hand landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    #2.get the tip of undex and middle fingers
    if len(lmList)!=0:
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]

        # print(x1,y1,x2,y2)

        #3.check whether fingers are up
        fingers = detector.fingersUp()
        # print(fingers)

        cv2.rectangle(img,(frameR, frameR),(wCam-frameR, hCam-frameR),
                        (255,0,255), 2)

        #4.only index finger:moving mode
        if fingers[1] == 1 and fingers[2] == 0:
        
          
          #5. convert coordinates
          x3 = np.interp(x1, (0, wCam), (0, wScr))
          y3 = np.interp(y1, (0, wCam), (0, hScr))

          #6. smoothen values
          clocX = plocX +(x3-plocX)/smoothening
          clocY = plocY +(y3-plocY)/smoothening


          #7. move mouse
          autopy.mouse.move(wScr- clocX, clocY)
          cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
          plocX,plocY = clocX, clocY

        # 8.both index and middle fingers are up:clicking mode
        if fingers[1] == 1 and fingers[2] == 1:
            # 9. find distance between fingers
           length,img, lineInfo = detector.findDistance(8,12,img)
           print(length)
           #10.click mouse if distance short
           if length <40:
              cv2.circle(img,(lineInfo[4],lineInfo[5]),
                         15,(0,255,0),cv2.FILLED)
              autopy.mouse.click()
        
           
    #11.framerate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)),(20,50), cv2.FONT_HERSHEY_PLAIN,3,
                (255,0,0), 3)
                
    #12.Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    