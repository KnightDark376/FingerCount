# FingerCount
Count Fingers with opencv , mediapipe

# Medipipe Hand
https://google.github.io/mediapipe/solutions/hands.html
# module HandTracking
> Sử dụng thư viện mediapipe để nhận biết hình dạng và khả năng chuyển động của bàn tay.  
> MediaPipe Hands là giải pháp theo dõi ngón tay và bàn tay có độ trung thực cao. Nó sử dụng công nghệ máy học (ML) để suy ra 21 điểm mốc 3D của bàn tay chỉ từ một khung hình duy nhất.
![21 hand landmarks](https://google.github.io/mediapipe/images/mobile/hand_landmarks.png)
> **MediaPipe Hands** sử dụng một pipeline ML bao gồm nhiều mô hình hoạt động cùng nhau:  
> Một mô hình phát hiện lòng bàn tay hoạt động trên hình ảnh đầy đủ và trả về một hộp giới hạn bàn tay có định hướng. Mô hình điểm mốc bàn tay hoạt động trên vùng hình ảnh đã cắt được xác định bởi máy dò lòng bàn tay và trả về khớp  bàn tay 3D có độ trung thực cao. Chiến lược này tương tự như chiến lược được sử dụng trong giải pháp MediaPipe Face Mesh sử dụng máy dò khuôn mặt cùng với mô hình mốc khuôn mặt.  
> Việc cung cấp hình ảnh bàn tay được cắt chính xác cho mô hình mốc bàn tay giúp giảm đáng kể nhu cầu tăng dữ liệu (ví dụ: phép quay, dịch và tỷ lệ) và thay vào đó cho phép mạng dành phần lớn năng lực của mình cho độ chính xác của dự đoán tọa độ. Ngoài ra, trong pipeline của chúng tôi, các điểm cắt (khớp) cũng có thể được tạo dựa trên các mốc bàn tay được xác định trong khung trước đó và chỉ khi mô hình mốc không còn có thể xác định sự hiện diện của bàn tay thì tính năng phát hiện lòng bàn tay mới được gọi để điều chỉnh bàn tay vào đúng khung hình để nhận dạng.  
> Pipeline được triển khai dưới dạng biểu đồ MediaPipe sử dụng đồ thị con theo dõi các điểm cắt (khớp)  bàn tay từ mô-đun mốc bàn tay và hiển thị bằng cách sử dụng đồ thị con trình kết hình ảnh bàn tay chuyên dụng.  
> **Mô hình phát hiện bàn tay**
> 






