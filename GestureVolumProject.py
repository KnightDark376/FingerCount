import cv2
import time
import numpy as np
import HandTrackingModule as htm #import thư viên HandTrackingModule
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume #import thư viện điều khiển volum

################################
wCam, hCam = 840, 680
################################
Camera_id = 0
cap = cv2.VideoCapture(Camera_id)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)

devices = AudioUtilities.GetSpeakers() #kết nối với loa
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
# print(volRange)
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 100
volPer = 0
while True:
    success, farme = cap.read()
    farme = detector.findHands(farme)
    lmList = detector.findPosition(farme, draw=False)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(farme, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(farme, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(farme, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(farme, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        # print(length)

        # Hand range 50 - 300
        # Volume Range -65 - 0

        vol = np.interp(length, [20, 200], [minVol, maxVol]) #Scale VolBar
        volBar = np.interp(length, [20, 200], [400, 150])
        print(volBar)
        volPer = np.interp(length, [20, 200], [0, 100]) #Scale VolPer
        # print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length < 20:
            cv2.circle(farme, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(farme, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(farme, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED) #Vẽ VolBar
    cv2.putText(farme, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                1, (0, 0, 255), 3) #Hiển thi VolPer

    ######tính FPS#############################################################
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(farme, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)
    ###########################################################################
    cv2.imshow("Video", farme)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cap.release()
cv2.destroyAllWindows()
