# FingerCount
Count Fingers with opencv , mediapipe

# Medipipe Hand
https://google.github.io/mediapipe/solutions/hands.html
# module HandTracking
> Sử dụng thư viện mediapipe để nhận biết hình dạng và khả năng chuyển động của bàn tay.  
> MediaPipe Hands là giải pháp theo dõi ngón tay và bàn tay có độ trung thực cao. Nó sử dụng công nghệ máy học (ML) để suy ra 21 điểm mốc 3D của bàn tay chỉ từ một khung hình duy nhất.
![21 hand landmarks](https://google.github.io/mediapipe/images/mobile/hand_landmarks.png)
> **MediaPipe Hands** sử dụng một pipeline ML bao gồm nhiều mô hình hoạt động cùng nhau:  
>   Một mô hình phát hiện lòng bàn tay hoạt động trên hình ảnh đầy đủ và trả về một hộp giới hạn bàn tay có định hướng. Mô hình điểm mốc bàn tay hoạt động trên vùng hình ảnh đã cắt được xác định bởi máy dò lòng bàn tay và trả về khớp  bàn tay 3D có độ trung thực cao. Chiến lược này tương tự như chiến lược được sử dụng trong giải pháp MediaPipe Face Mesh sử dụng máy dò khuôn mặt cùng với mô hình mốc khuôn mặt.  
>   Việc cung cấp hình ảnh bàn tay được cắt chính xác cho mô hình mốc bàn tay giúp giảm đáng kể nhu cầu tăng dữ liệu (ví dụ: phép quay, dịch và tỷ lệ) và thay vào đó cho phép mạng dành phần lớn năng lực của mình cho độ chính xác của dự đoán tọa độ. Ngoài ra, trong pipeline của chúng tôi, các điểm cắt (khớp) cũng có thể được tạo dựa trên các mốc bàn tay được xác định trong khung trước đó và chỉ khi mô hình mốc không còn có thể xác định sự hiện diện của bàn tay thì tính năng phát hiện lòng bàn tay mới được gọi để điều chỉnh bàn tay vào đúng khung hình để nhận dạng.  
>  Pipeline được triển khai dưới dạng biểu đồ MediaPipe sử dụng đồ thị con theo dõi các điểm cắt (khớp)  bàn tay từ mô-đun mốc bàn tay và hiển thị bằng cách sử dụng đồ thị con trình kết hình ảnh bàn tay chuyên dụng.  
> **Mô hình phát hiện bàn tay**
> Thiết kế mô hình diện ngay lần đầu tiên (**Singed-shot**) được tối ưu hóa cho việc sử dụng thời gian thực trên thiết bị di động theo cách tương tự như mô hình nhận diện khuôn mặt trong MediaPipe Face Mesh.  
> Phát hiện bàn tay là một nhiệm vụ phức tạp: mô hình của chúng tôi phải làm việc trên nhiều kích cỡ bàn tay khác nhau với khoảng tỷ lệ lớn (~ 20x) so với khung hình ảnh và có thể phát hiện bàn tay bị khuất  và tự khớp với nhau. Đầu tiện nhận đào tạo một máy dò lòng bàn tay thay vì nhận diện các khớp trên bàn tay. Vì khi tay cầm một vật thể cứng các khớp tay sẽ bị khuất.Thứ hai, trình trích xuất tính năng bộ mã hóa-giải mã được sử dụng để nhận biết ngữ cảnh cảnh lớn hơn ngay cả đối với các đối tượng nhỏ (tương tự như cách tiếp cận RetinaNet). Sau đó giảm thiểu mất các tiều điểm để hỗ trọ nhận diện các ,ốc tìm được do phương sai tỷ lệ cao.
> Sau khi phát hiện lòng bàn tay mô hình hand_landmark tiếp tục hỗ trờ để đánh dấu 21 điểm trên bàn tay trong vùng phát hiện được thông qua hồi quy đó là dự đoán tọa độ trực tiêp.
> Mô hình học thể hiện tư thế bên trong lòng bàn tay một cách nhất quán và chính xác ngay cả khi ta chỉ nhìn thấy một phần hoặc các khớp tay trùng vào nhau.

# FingerCountProject
> Đếm số ngón tay từ bàn tay nhận diện được
> Sử dụng vị trí của các điểm mốc trên lòng bàn tay để xác định hoạt động của các ngón tay. Từ các vị trí nhận diện được đem các kết quá đo so sánh với nhau để xác định vị trí tương đối của các điểm mộc từ đó xác định số ngón tay muốn chỉ. Hiển thị số lên màn hình.
# GestureVolumProject
> Điều chỉnh volum của laptop bằng cử chỉ của ngón tay






