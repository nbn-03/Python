# Python
## 1. tổng quan cho người mới với python
- https://github.com/Pierian-Data/Complete-Python-3-Bootcamp
- windows command line:
  - hiển thị các thư mục và file trong đường dẫn: dir
  - xóa màn hình: cls
  - chuyển đường dẫn: cd
  - xem đường dẫn hiện tại: cd
- linux command line:
  - hiển thị các file và thư mục: ls -a
  - xóa màn hình: clear
  - chuyển đường dẫn: cd
  - xem đường dẫn hiện tại: pwd
- tải Python: youtube.
- cách chạy trên terminal: cd đến đường dẫn đó sau đó => python ten_file.py
## 2. Python object and data structure basics
- ![image](https://github.com/nbn-03/Python/assets/98254107/d2a250f1-ab95-464d-9e04-74733103a6c6)
### a.Numbers
- có 2 loại số chính mà ta sẽ làm việc là int - integer và float - số thâp phân
- ** trong python là phép toán mũ
- chú ý: trong python với số thập phân không thể biểu diễn chính xác trong hệ thống nhị phân của máy tính vì vậy kết quả sẽ không chính xác đến 1 số rất nhỏ. ví dụ:<br>![image](https://github.com/nbn-03/Python/assets/98254107/313942cb-8255-4868-9d27-b239ed3decbb)<br>cách fix:<br>![image](https://github.com/nbn-03/Python/assets/98254107/5f1a3185-0644-418c-aae2-94079a86c02b)
### b.gán biến
- gán biến: a = 5 | a = 46 | a = 4.5 các quy tắc đặt tên: không bắt đầu bằng số; không có space; không có ' " , < > / ? | \ ( ) ! @ # $ % ^ & * ~ - + và tránh tên những từ có nghĩa trong python
- trong python sử dụng tính năng Dynamic Typing. nghĩa là có thể gán lại biến cho các loại kiểu dữ liệu khác nhau hay không cần khai báo kiểu dữ liệu cho biến. điều này làm cho việc gán kiểu dữ liệu rất linh hoạt so với các ngôn ngữ khác. ưu điểm: dễ làm việc; thời gian nhanh. nhược điểm: có thể gây ra lỗi đối với kiểu dữ liệu dữ liệu không mong muốn. để xác định kiểu dữ liệu ta dùng hàm: **type()**
### c.String
- là chuỗi kí tự đặt trong " " hoặc ' '
- chú ý: để in ra dấu ' hoặc " <br>
![image](https://github.com/nbn-03/Python/assets/98254107/fb0db2cf-6bb9-43d9-a900-ef342dc12264)
- chú ý: với truy xuất phần tử trong String ở java không dùng truy xuất như python mà dùng: **ten_chuoi.charAt(chi_muc)**
- trong các chuỗi có số thứ tự gọi là chỉ mục chúng ta có thể sử dụng chỉ mục (mỗi phần tử trong chuỗi đều có 1 số thứ tự bắt đầu từ 0) để lấy hoặc cắt các phần con của chuỗi
- ví dụ: <br>![image](https://github.com/nbn-03/Python/assets/98254107/338e4117-5c62-4997-b3d6-b64ecee92cd3)
- chỉ mục được đặt trong [ ]
- ví dụ: <br>![image](https://github.com/nbn-03/Python/assets/98254107/aa1c8be9-1471-4ac9-90d1-fe7db1f5c530)<br>![image](https://github.com/nbn-03/Python/assets/98254107/a36583f0-6f36-4c55-aef2-b8e0b12fe409)
- slicing cho phép bạn lấy 1 phần gồm nhiều kí tự. lệnh: **ten_chuoi[start:stop:step]**. nếu không truyền đối số cho stop và step và start nó sẽ tự động stop: vị trí cuối của chuỗi, step: 1, start: vị trí bắt đầu. đảo ngược chuỗi thì step là số âm.
- câu lệnh để in ra màn hình: **print()**. print sẽ tự động xuống dòng khi thực hiện câu lệnh. \n - xuống dòng. \t sử dụng tab
- câu lệnh đo độ dài của chuỗi: **len(ten_chuoi)**
- xử lí chuỗi trong python khác java là với java có thể dùng dấu cộng "+" để nối các kiểu dữ liệu với nhau để tạo thành 1 chuỗi. với python để nối chuỗi cần phải ép kiểu thành KDL String để nối chuỗi. ngoài ra trong python còn có phép nhân "*" => để nhân các chuỗi giống nhau; phép so sánh "< > <= >= ==" để so sánh chuỗi (với java so sánh chuỗi cần phương thức hỗ trợ).
- ép kiểu: (KDL)ten_bien <br> ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/3cf9b24f-8994-46a1-82f5-6d771b352245)
- chuyển thành chũ hoa: **ten_chuoi.upper()**
- chuyển thành chữ thường: **ten_chuoi.lower()**
- tách 1 chuỗi thành 1 list: **ten_chuoi.split("vi_tri_tach")**. chú ý đối số của hàm split không có gì sẽ auto là dấu cách.
- comment 1 câu trong python dùng #; comment 1 đoạn trong python """ """
- để nối chuỗi ngoài cách ép kiểu ta có thể dùng format <br> ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/9b446db2-3d00-4c7b-8772-66bae10647ff) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/85b6d7e5-f625-471f-a4b5-b47ca7ad3947) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/71d55a13-dccd-4cf9-b7b4-ba4a771f5c33) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/fe157ed4-7bf2-462f-8e2b-48e7ed0ec256) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/1d84f5b3-d13e-44a5-a650-9b642fedaac7) <br> **cách dùng cho python 3.6 trở lên** <br>![image](https://github.com/nbn-03/Python/assets/98254107/ff0bcaf5-748a-465d-8d26-4cf13093ef80)
### d. bool -boolean: tương tự java nhưng tại đây boolean là KDL nguyên thủy nên có thể in ra màn hình trực tiếp true hoặc false
- với C thì không phải kiểu dữ liệu nguyên thủy nên cần thêm #include<stdbool.h> vì vậy không in ra màn hình trực tiếp như Python và Java
### e. list
- list là 1 tập hợp có thứ tự có thể chứa nhiều loại đối tượng khác nhau. các loại đối tượng đấy được gọi là phần tử
- dùng dấu [ ] để nhóm các phần tử thành 1 list và dấu phẩy "," để ngăn cách loại các phần tử. ví dụ:  ![image](https://github.com/nbn-03/Python/assets/98254107/28068893-90ab-414a-9fd5-6c15202f6cca)
- số phần tử của list: **len(ten_list)**
- **truy xuất phần tử trong list sẽ giống với các phần tử trong chuỗi**
- nối list sư dụng phép công "+". ví dụ:  ![image](https://github.com/nbn-03/Python/assets/98254107/116b3167-5512-4872-a447-32aa265a4548)
- có sự khác biệt là với chuỗi không thể thay đổi được phần tử trong chuỗi nhưng tại list thì có tể thay đối các phần tử. ví dụ: ![image](https://github.com/nbn-03/Python/assets/98254107/6741ca7f-c82f-46e8-aa6c-169b82a4471c)
- thêm vào cuối list: **ten_list.append(gia_tri_can_them)**
- loại bỏ phần tử trong
