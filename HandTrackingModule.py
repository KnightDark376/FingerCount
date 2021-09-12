import cv2
import mediapipe as mp
import time


class handDetector():
    '''
        Khởi tạo các thông số ban đầu:
        mode : Nếu là False thì hình ảnh đầu vào được coi như là một luồng  , nếu là True thì coi đầu vào như một loạt hình ảnh
        maxHands : là một số để chỉ thị số bàn tay có thể phát hiện ra. Nếu đã nhận diện đủ thì sẽ không nhận thêm bày tay khác nữa trừ khi bàn tay trước đó mất đi
        detectionCon : Giá trị độ tin cậy tối thiểu từ các mô hình được xác nhận là thành công.
        trackCon : Giá trị độ tin cậy tối thiểu từ mô hình theo dõi mốc bàn tay. Đặt thành giá trị cao hơn để tăng đọ chắc chắn
    '''
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        # Tạo một biến thuộc module mediapipe để phát hiện bàn tay
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        # đò thị con hiển thị mốc bàn tay
        self.mpDraw = mp.solutions.drawing_utils

    '''
        Tìm các ngón tay trên lòng bày tay
        img : luồng video hoặc hình ảnh đầu vào
        draw : True  thực hiện nối các mốc bàn tay lại với nhau
    '''
    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #Xử lý ảnh đen trắng để phát hiện các mốc bàn tay
        self.results = self.hands.process(imgRGB)
        #print(self.results.multi_hand_landmarks)
        
        #Nếu kết quả trả về là phát hiện ra các mốc trên lòng bàn tay thì tiến hành vẽ các đường nối nếu Draw == True
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img
    '''
        Tìm vị trí của các mốc bàn tay đã phát hiện được
        img : Hình ảnh hoặc luồn video đầu vào
        handNo : Số thứ tự của bàn tay đã phát hiện được
        draw : Nếu là True thì vẽ một hộp xung quanh tay phát hiện được
    '''
    def findPosition(self, img, handNo=0, draw=True):

        lmList = []
        if self.results.multi_hand_landmarks:  #Kiểm tra xem có nhận diện được bàn tay hay chưa
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

        return lmList


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img,True)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
