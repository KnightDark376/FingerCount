import cv2
import time
import os
import HandTrackingModule as htm #chèn module HandTrackingModule vào project

id_camera = 0 #Địa chỉ camera kết nối
wCam, hCam = 400, 600 # Chiều dài và chiều rộng khung ảnh

cap = cv2.VideoCapture(id_camera) #Đọc hình ảnh từ cameraid
cap.set(3,wCam) #Cài đặt chiều rộng khung camera
cap.set(4, hCam) #Cài đặt chiều dài khung camera
'''Đọc file hình ảnh các hình chỉ thị số đếm'''
folderPath = "FingerImages"
myList = os.listdir(folderPath)
print(myList)
overlaylist = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    #print(f'{folderPath}/{imPath}')
    overlaylist.append(image)
'''------------------------------------------------'''
print(len(overlaylist))
pTime = 0

detector = htm.handDetector(detectionCon=0.75) # Khởi tạo

tipIds = [4, 8, 12, 16, 20] #List các vị trí để xác định hoạt động của ngón tay

while True:
    success, img = cap.read()
    detector.findHands(img) #nhận diện bàn tay
    lmList = detector.findPosition(img, draw=False) #Tìm các điểm mốc trên bàn tay
    #print(lmList)

    #cv2.rectangle(img, (20, 425), (425, 810), (0, 255, 0), cv2.FILLED)
    if len(lmList) != 0: #Kiểm tra điều kiện có nhận được điểm mốc nào không
        fingers = []

        #Thumb
        if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 fingers
        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-1][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        #print((fingers))
        totalFinger = fingers.count(1)
        print(totalFinger)

        h, w, c = overlaylist[totalFinger-1].shape
        img[0:h, 0:w] = overlaylist[totalFinger-1]


        if totalFinger == 2:
            cv2.putText(img, 'Keo', (45, 375), cv2.FONT_HERSHEY_PLAIN,
                        10, (255, 0, 0), 25)
        elif totalFinger == 4:
            cv2.putText(img, 'Xeng', (45, 375), cv2.FONT_HERSHEY_PLAIN,
                        10, (255, 0, 0), 25)
        elif totalFinger == 0:
            cv2.putText(img, 'Bua', (45, 375), cv2.FONT_HERSHEY_PLAIN,
                        10, (255, 0, 0), 25)
        elif totalFinger == 5:
            cv2.putText(img, 'Bao', (45, 375), cv2.FONT_HERSHEY_PLAIN,
                        10, (255, 0, 0), 25)
        elif totalFinger == 1:
            cv2.putText(img, 'Kim', (45, 375), cv2.FONT_HERSHEY_PLAIN,
                        10, (255, 0, 0), 25)
        else:
            cv2.putText(img, str(totalFinger), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                        10, (255, 0, 0), 25)
    else:
        cv2.putText(img, 'NoHand', (45, 375), cv2.FONT_ITALIC,
                    3, (255, 0, 0), 4)
    '''Tính tốc độ khung hình'''
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3,(255,0,0), 3)

    cv2.imshow("image", img) #hiển thị video lên màn hình
    if cv2.waitKey(1) & 0xFF = ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
