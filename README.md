# Python
## 1. tổng quan cho người mới với python
- https://github.com/Pierian-Data/Complete-Python-3-Bootcamp
- **vì là tổng quát lại nên sẽ không nhắc đươc hết các hàm, các phương thức vì vậy còn rất nhiều hàm, phương thức khác nhau (GPT; Google)**
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
**trong python và java khi tổng hợp lí thuyết có thể viết hàm với phương thức lẫn lộn nhau. hiểu đơn giản là hàm chỉ cần gọi trực tiếp còn phương thức là dùng qua đối tượng để gọi như: ten.phuong_thuc()**
**trong python không có { } để nhóm câu lệnh lại như C và Javaa nên ta sử dụng thụt lề (tab) để nhóm câu lệnh**
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
- chú ý: với truy xuất phần tử trong String ở java không dùng truy xuất như python mà dùng: **ten_chuoi.charAt(chi_muc)** =>> tương tác trên chuỗi của java đều thông qua phương thức đa phần sẽ khác với python (vẫn tồn tại 1 số giống nhau giữa 2 ngôn ngữ)
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
- thêm vào cuối list: **ten_list.append(gia_tri_can_them)**.
- lấy phần tử và loại bỏ chính phần tử đó trong list: **ten_list.pop(vi_tri_bo)** nếu không truyền vị trí sẽ auto là vị trí cuối
- sắp xếp các phần tử trong list theo thứ tự tăng dần: **ten_list.sort()**
- sắp xếp các phần tử trong list theo thứ tự giảm dần: **ten_list.reverse()**
- chú ý:<br> ![image](https://github.com/nbn-03/Python/assets/98254107/21113fd2-06c4-404d-bf9c-d40a328116f0)
### f. Dictionary
- là 1 tập hợp các cặp **key-value với key là chỉ mục** không có thứ tự, không thể sắp xếp, có thể thay đổi (key cố định và value được thay đổi).
- trong dictionary sử dụng dấu { } để tập hợp tạo nên dic phân cách các phần tử bằng dấu , còn giữa key và value là dấu :
- ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/a9b3e6e4-1c6a-4303-8115-22e5d8e9864c)
- cách lấy dược value: **ten_dic[ten_key]** <br> ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/a2cfc5a2-eefa-43c6-b81f-f4c28ec70a5e) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/29ef3c3f-6e35-4d00-8ad5-d6e9ba16fa6b)
- thêm 1 cặp vào dic: **ten_dic[key_moi] = value_moi** ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/9620b047-d929-48eb-83f8-4ae4b971e763)
- thay đổi value: **ten_dic[key_can_thay] = value_moi** ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/f3f91c8a-5839-4763-b50a-840e96f1400d)
- xem tên các key: **ten_dic.keys()**
- xem giá trị các value: **ten_dic.values()**
- xem cả tên key và các giá trị value tương ứng: **ten_dic.items()**
- kiểm tra số bộ trong dic: **len(ten_dic)**
### g. tuple
- rất giống với **list** nhưng chúng có tính **bất biến - không thể thay đổi**
- dùng dấu ( ) để nhóm các phần tử và các phần tử ngăn cách nhau bởi dấu ,
- kiểm tra số phần tử: **len(ten_tuple)**
- truy xuất: **tương tự list**
- đếm số lần phần tử có trong tuple: **ten_tuple.count(gia_tri_phan_tu)**
- trả về chỉ mục đầu tiên mà phần tử đó xuất hiện: **ten_tuple.index(gia_tri_phan_tu)**
### h. set
- là 1 bộ không có thứ tự <không có chỉ mục>, không cho phép dữ liệu trùng lặp
- dùng dấu { } để tập hợp các phần tử, các phần tử phân cách nhau bởi dấu ,
- thêm phần tử vào set: **ten_set.add(gia_tri)**
- thường dùng để lọc các giá trị trùng nhau trong list
### i. file
- bắt đầu làm việc đơn giản với file .txt
- với phương pháp đơn giản ở đây sẽ là cơ sở mở rộng hơn nữa để làm việc với các tệp khác như: âm thanh, excel,...
- mở file: **ten_doi_tuong = open("duong_dan_den_file")** ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/6aa06394-27cf-4470-b3b1-1b3ca6d38d53) <br> chú ý: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/f6dbdfe1-244a-4126-9e25-5dc0221cae37) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/1bf1b6d9-1131-47b3-b101-3c3ec1caac58) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/caa72150-2209-4819-a824-e2fe43e479b0)
- đóng file: **ten_doi_tuong.close()**
- các tối ưu thường dùng kết hợp mở và đóng file: **with open("duong_dan_den_file") as ten_doi_tuong** các câu lệnh thao tác với file đều nằm trong with. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/08eb961e-401e-481a-bce6-cf0c3e7f5164)
- để thao tác đọc và ghi file thì cần thêm mode khi mở file: **open("duong_dan","mode")**
- các mode: **giống với C**
  - **r**: chỉ được phép đọc, nếu file không tồn tại sẽ trả về lỗi
  - **w**: chỉ cho phép ghi, nếu file đã tồn tại thì sẽ ghi đè, nếu chưa tồn tại sẽ được tạo tự động
  - **a**: cho ghi thêm dữ liệu vào cuối file (con trỏ ở cuối file), nếu file không tồn tại sẽ được tạo mới
  - **rb, wb, ab**: mode ở chế độ nhị phân
  - **mode thêm dấu +**: cho phép cả đọc và ghi
- đọc file: **ten_doi_tuong.read()** tại đây khi đọc nó sẽ xuất hiện kí tự \n đó chính là xuống dòng trong file
- ghi file: **ten_doi_tuong.write(noi_dung)**
- đọc toàn bộ file và lưu mỗi dòng là 1 phần tử của list: **ten_doi_tuong.readlines()** chú ý lưu cả dấu xuống dòng
- tại trong file cũng sẽ có chỉ mục bắt đầu từ 0 vì vậy các phương thức có thể sử dụng đến chỉ mục
