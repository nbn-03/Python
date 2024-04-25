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
-  **trong python và java khi tổng hợp lí thuyết có thể viết hàm với phương thức lẫn lộn nhau. hiểu đơn giản là hàm chỉ cần gọi trực tiếp còn phương thức là dùng qua đối tượng để gọi như: ten.phuong_thuc()**  
- **trong python không có { } để nhóm câu lệnh lại như C và Java nên ta sử dụng thụt lề (tab) để nhóm câu lệnh**
## 2. Python object and data structure basics
- ![image](https://github.com/nbn-03/Python/assets/98254107/d2a250f1-ab95-464d-9e04-74733103a6c6)
### a.Numbers
- có 2 loại số chính mà ta sẽ làm việc là int - integer và float - số thâp phân
- ** trong python là phép toán mũ
- chú ý: trong python với số thập phân không thể biểu diễn chính xác trong hệ thống nhị phân của máy tính vì vậy kết quả sẽ không chính xác đến 1 số rất nhỏ. ví dụ:<br>![image](https://github.com/nbn-03/Python/assets/98254107/313942cb-8255-4868-9d27-b239ed3decbb)<br>cách fix:<br>![image](https://github.com/nbn-03/Python/assets/98254107/5f1a3185-0644-418c-aae2-94079a86c02b)
### b.gán biến
- gán biến: a = 5 | a = 46 | a = 4.5 các quy tắc đặt tên: không bắt đầu bằng số; không có space; không có ' " , < > / ? | \ ( ) ! @ # $ % ^ & * ~ - + và tránh tên những từ có nghĩa trong python
- trong python sử dụng tính năng Dynamic Typing. nghĩa là có thể gán lại biến cho các loại kiểu dữ liệu khác nhau hay không cần khai báo kiểu dữ liệu cho biến. điều này làm cho việc gán kiểu dữ liệu rất linh hoạt so với các ngôn ngữ khác. ưu điểm: dễ làm việc; thời gian nhanh. nhược điểm: có thể gây ra lỗi đối với kiểu dữ liệu dữ liệu không mong muốn. để xác định kiểu dữ liệu ta dùng hàm: **type()**
### c.String - str
- là chuỗi kí tự đặt trong " " hoặc ' '
- chú ý: với truy xuất phần tử trong String ở java không dùng truy xuất như python mà dùng: **ten_chuoi.charAt(chi_muc)** =>> **tương tác trên chuỗi của java đều thông qua phương thức đa phần sẽ khác với python (vẫn có 1 số giống nhau giữa 2 ngôn ngữ)**
- trong các chuỗi có số thứ tự gọi là chỉ mục chúng ta có thể sử dụng chỉ mục (mỗi phần tử trong chuỗi đều có 1 số thứ tự bắt đầu từ 0) để lấy hoặc cắt các phần con của chuỗi
- ví dụ: <br>![image](https://github.com/nbn-03/Python/assets/98254107/338e4117-5c62-4997-b3d6-b64ecee92cd3)
- chỉ mục được đặt trong [ ]
- ví dụ: <br>![image](https://github.com/nbn-03/Python/assets/98254107/aa1c8be9-1471-4ac9-90d1-fe7db1f5c530)<br>![image](https://github.com/nbn-03/Python/assets/98254107/a36583f0-6f36-4c55-aef2-b8e0b12fe409)
- slicing là tính năng cho phép bạn lấy 1 phần gồm nhiều kí tự (phần tử) trong chuỗi. lệnh: **ten_chuoi[start:stop:step]**. nếu không truyền đối số cho stop và step và start nó sẽ tự động stop: vị trí cuối của chuỗi, step: 1, start: vị trí bắt đầu. đảo ngược chuỗi thì step là số âm.
- câu lệnh để in ra màn hình: **print()**. print sẽ tự động xuống dòng khi thực hiện câu lệnh. \n - xuống dòng. \t sử dụng tab
- câu lệnh đo độ dài của chuỗi: **len(ten_chuoi)**
- xử lí chuỗi trong python khác java là với java có thể dùng dấu cộng "+" để nối các kiểu dữ liệu với nhau để tạo thành 1 chuỗi. với python để nối chuỗi cần phải ép kiểu thành KDL String để nối chuỗi. ngoài ra trong python còn có phép nhân "*" => để nhân các chuỗi giống nhau; phép so sánh "< > <= >= ==" để so sánh chuỗi (với java so sánh chuỗi cần phương thức hỗ trợ).
- ép kiểu: **KDL(ten_bien)** <br> ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/3cf9b24f-8994-46a1-82f5-6d771b352245)
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
- nối list sư dụng phép cộng "+". ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/116b3167-5512-4872-a447-32aa265a4548)
- có sự khác biệt là với chuỗi không thể thay đổi được phần tử trong chuỗi (vẫn có cách dùng phương thức replace) nhưng tại list thì có thể thay đối các phần tử. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/6741ca7f-c82f-46e8-aa6c-169b82a4471c)
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
- lưu ý: với set do không có thứ tự nên khi so sánh không quam tâm đến thứ tự các phần tử
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
## 3. toán tủ so sánh trong python
- ![image](https://github.com/nbn-03/Python/assets/98254107/b16ca2df-5443-4303-8700-b2d8ff73a576)
- **and**: và; **or**: hoặc; **not**: phủ định (giống với ! trong java và C)
## 4. câu lệnh trong python
### a. if; elif; else
- là câu lệnh điều kiện nếu-thì. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/70833ec2-0897-4c0c-bf38-941fe976e05f) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/073e464c-062f-43b9-ab07-46101facf222)
### b. for loop
- là lặp lại thực hiện câu lệnh dưới vòng lặp.
- ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/4b54bc45-1e35-43b4-8f0a-d4ca79f1db6a) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/3a56153d-cd54-44bf-8be9-f626979158df) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/d0e5cdf0-96f6-4139-a81b-b0e9da2eab34) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/f5a1e1fc-d4d2-4214-8185-41b495792c52) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/b14c386f-8d95-457e-a4e5-73274ab94464) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/8b28f1fc-0993-461c-b1a2-870388f701e0) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/3cb3b1d4-060a-4d6e-9807-b98f2557ac02) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/4f9a31ae-7516-48bd-b781-216796f3220e) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/b4620112-1559-4be2-af7f-6d09f9e3151e) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/b0f1de9f-b56b-4ef5-834b-975cb856fa87) <br> **vòng for giống C và Java** <br> ![image](https://github.com/nbn-03/Python/assets/98254107/73976048-2e8a-4d11-b1da-a1e0c4ff2c78)
- **các ví dụ trên có thể thấy tại python vòng lặp for nó khác với Java và C không chỉ dừng lại là for(int i=0;i<n;i++)**
### c. while loop
- là lặp lại câu lệnh dưới điều kiện nào đó (khác với for là tại while không biết được số lần lặp lại)
- ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/4da63b0f-9732-47cc-b40c-79af4b2d6751)
- trong python không có do while nhưng lại có while else. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/73f49073-214e-49ff-a859-db183e8ebe92)
- tại vòng lặp sẽ có 2 từ khóa hay dùng là: **break**-dùng để kết thúc vòng lặp; **continue**-bỏ qua vòng lặp này đến vòng lặp tiếp.
### d. mở rộng
- **range(start,stop,step)**. nếu chỉ có stop thì start = 0 và step = 1. lưu ý: **< stop**.
- từ câu lệnh range tạo thành 1 list, set, tuple: **loai(range(strat,stop,step))**
- tích hợp truy xuất ra cả vị trí phần tử và giá trị: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/ba4f1325-defc-4fb2-afb6-9cbfa0825dc4) <br> **không chỉ chuỗi mà còn list, tuple, set, dictionary**
- <br> ![image](https://github.com/nbn-03/Python/assets/98254107/747070a7-b015-48ee-a6f7-bd107fc155ca) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/70406ac3-d397-4c69-a2d9-d5d12bc10b67)
- có thể dung **in** để kiểm tra phân tử có nằm trong chuỗi, list,... hay không. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/492a201c-6997-48c4-913b-9bc9b5b7090c)
- max, min trong chuỗi, list,...: **max(ten)**' **min(ten)**
- **nhập từ bàn phím** câu lệnh: **input()**. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/1a330537-f3ca-450c-ad49-17323b9879b7) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/2a4f2fb9-2b01-4110-b989-16371be05de8) <br> **vì nhập vào từ bàn phím kiểu dữ liệu lúc nào cũng là String vì vậy có thể ép kiểu từ khi nhập** <br> ![image](https://github.com/nbn-03/Python/assets/98254107/bb955ff9-7ac2-4b20-b396-cf67cd78d0dd)
- **khuyến cáo nên dùng cách tường mình cách này nên đọc cho biết, đây được gọi là comprehensio và chỉ tạo được list comprehensio và set comprehensio** <br> ![image](https://github.com/nbn-03/Python/assets/98254107/ceae7e86-7d39-43b0-8946-dc20a1bcad31) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/df97b9b0-ab63-42e8-9f7d-99d94c952096) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/d0676e94-2cdb-48c5-a635-3fd8c5b360ea) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/2d8748e0-08d6-4a13-bf34-6ed9ab52c6f2) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/4d39c05d-1767-4801-b892-10a48251abea) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/b15fadc5-dd6f-408c-9897-26b49aae27a1) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/b2156a6e-0fc3-4f10-88b1-079cc9ecc3ab)
## 5. hàm
- tạo hàm sẽ dùng đến từ khóa **def** cú pháp: **def ten_ham(doi_so):**
- ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/685abf9e-6c16-4fd9-bce1-4925bba7bdaf)
- nếu hàm có kết quả trả về là 1 giá trị thì cần có từ khóa **return**.
- ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/962e525b-1fbc-4c7f-bbb8-882c660a4da7) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/bb6891df-304a-405f-a142-e3ebc62da8b4) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/cb443ba1-cd63-4b75-b500-1572c39b1f5f)
- tương tác giữa các hàm: hàm này có thể làm đối số phục vụ hàm kia. ví dụ: bài tìm 1 quả bóng trong 3 cái cốc (lưu trên github)
- tìm hiểu về 2 từ khóa *args và **kwargs:
  - *args: được sử dụng để truyền một số lượng biến đối số không cố định vào hàm. Nó cho phép hàm nhận được bất kỳ số lượng đối số nào được truyền vào và đặt chúng trong một tuple. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/4abe36f2-94b7-4521-8b5d-d695a37527f5)
  - **kwargs: được sử dụng để truyền một số lượng biến đối số không cố định vào hàm. nó nhận và đối số dạng key-value tạo thành dicnationary. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/4bd0a2d6-9323-4678-b882-cbbe938d2601)
  - kết hợp cả 2 lưu ý phải truyền đúng lần lượt thứ tự. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/46b7abf5-7c76-4f00-b5a1-32ae810665f3) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/3dbe878e-b988-4c63-93b8-6b2af4d6840a)
- trả về giá trị tuyệt đối: **abs(ten)**
- Lambda Expressions, Map, and Filter:
  - hàm **map**:  là một hàm tích hợp sẵn được sử dụng để áp dụng một hàm lên mỗi phần tử của một hoặc nhiều chuỗi, list, tuple,... kết quả trả về sẽ là 1 địa chỉ bộ nhớ của 1 dãy phần tử. để hiện thị dãy phần tử đó ta **thông thường** ép kiểu nó về 1 list hoặc tuple. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/10c1faf5-8ac3-40d1-8c74-755edc82660f)
  - hàm **filter**: kết quả trả về sẽ tương tự hàm **map** nhưng chức năng: được sử dụng để lọc các phần tử trên một hàm điều kiện. ví dụ: ![image](https://github.com/nbn-03/Python/assets/98254107/4a9a8da6-4cdc-4c3f-9adc-527f26ffa4ad)
  - **lambda**: được gọi hàm vô danh, là một loại hàm không tên và thường được sử dụng để định nghĩa các hàm ngắn gọn, đơn giản mà không cần phải dùng từ khoá **def**. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/19c242db-8ece-4008-9f61-1ea402836b9f) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/9bda9b04-f808-4027-987c-4d1be29962c5)
  - kết hợp: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/6680ead9-44b0-4e06-ae92-7991e47f8c89)
- các phạm vi thứ tự tìm kiếm trong python:
  - **local**:  Phạm vi local chứa các biến được định nghĩa trong hàm hiện tại. Biến local chỉ có thể truy cập được từ bên trong hàm đó.
  - **Enclosing**: Phạm vi enclosing là phạm vi bên ngoài hàm hiện tại, chứa các biến của hàm bao bọc hàm hiện tại (nếu có). Nó thường xuất hiện trong trường hợp các hàm lồng nhau
  - **Global**: Phạm vi global chứa các biến được định nghĩa ở mức module hoặc ở mức toàn cục của chương trình. Các biến global có thể truy cập được từ bất kỳ nơi nào trong chương trình
- ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/4690853e-114d-4ec6-b4a3-22a557f2937d)
- trong C và Java: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/ee3a6ebe-7282-4e14-b593-3ad676e25009) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/8a6a2177-31ee-4f35-8139-5f9da477142c)
- **chú ý**: đặc biệt tại python khi đặt tên hàm có thể trùng tên với những câu lệnh có sẵn **(chú ý này thuộc mục ghi đè)**. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/fa4744f5-813a-44b8-8763-1dfe6e86e18b)
-  **chú ý** khác với C và Java khi truy cập đến mức độ thấp hơn để thay đổi giá trị có thể thay đổi **trực tiếp** giá trị biến đấy nhưng với python khi thay đổi giá trị biến ở mức độ thấp hơn cần phải gọi ra. cách gọi với global: **global** ten_bien <br> ![image](https://github.com/nbn-03/Python/assets/98254107/15e2c7cb-650a-4cd7-a055-c6536ae4804f) <br> với enclosing: **nonlocal** ten_bien <br> ![image](https://github.com/nbn-03/Python/assets/98254107/00f5b79b-67a1-4b97-a77c-1e34b960c453)
## 6. lập trình hướng đối tượng
- khái niệm: OOP là gì, lớp, đối tượng, phương thức, thuộc tính, ưu điểm nhìn lại java
- cấu trúc lệnh <br> ![image](https://github.com/nbn-03/Python/assets/98254107/fde26f95-e476-4021-ba41-611d04a3ea00)
- 4 tính chất của OOP trong java (tính đóng gói, kế thừa, đa hình, trừu tượng) đều có ở python giống nhau về nội dung tuy nhiên cách thể hiện có 1 vài tự khác biệt
- chú ý: vì tính chất của python (không cần khai báo KDL) nên **không cần** khai bao thuộc tính
### a. constructor
- định nghĩa: Java
- cấu trúc: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/4c837d09-4dbe-452c-b5d4-b0a2c5eb798f) <br> **self** là một quy ước (không phải là từ khóa nên cần khai báo tại vị trí đối số) dùng để tham chiếu đến thuộc tính của lớp đó. tuy nhiên trong java có this có thể bỏ this (từ khóa - khuyến cáo nên có) nhưng trong python không khai báo thuộc tính vì vậy sẽ không nhận biết được thuộc tính của đối tượng nên phải có **self**
- với constructor có tham số hay không có tham số thì từ **self** vẫn luôn có tại vị trí đối số <br> ![image](https://github.com/nbn-03/Python/assets/98254107/db6ab145-76a1-458a-a5cb-b008b819597d)
### b. phương thức
- ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/b2cbd2e1-efce-49c9-aeaf-4f2ff31b03d7) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/3d0c7603-4714-45a0-afaa-3dbc9e4180f6)
- các phương thức cũng tương tự constructor là luôn có **self** tại vị trí đối số <br> ![image](https://github.com/nbn-03/Python/assets/98254107/7e732ecf-16f4-4b59-bb84-0980742a388f)
- **chú ý**: **self** trong constructor, phương thức có thể thay thế được bằng **tên class**, self trong vị trí đối số truyền vào constructor, phương thức vẫn phải có (không làm theo cách này chỉ nên đọc-biết). ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/45606ef1-e916-4a74-847d-d838f87c91a6)
### c. kế thừa
- cấu trúc: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/e3d35113-3610-472e-be6c-9a4e4d215ce6)
- khác với java trong python có tính đa kế thừa 
- **chú ý**: có sự khác biệt với java là  Python, nếu lớp con có một constructor, lớp cha cũng có một constructor và lớp con không gọi constructor của lớp cha bằng super().constructor_lop_cha **(super() có thể thay bằng ten_lop_cha)**, thì constructor của lớp cha sẽ không tự động được gọi khi bạn tạo một thể hiện của lớp con.
- ghi đè: giống với java
- nạp chồng phương thức: giống java. hoặc trong Python có 1 cách khác dùng từ khóa **None** ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/38e46e73-c99e-4f46-853a-115ee9ee7343)
### d. đa hình
- **khác so với Java ở Python không có khuôn mãu, không được thể hiện mạnh mẽ**
### e. trìu tượng
- **lưu ý**: tại python không có interface và lớp trìu tượng như Java chỉ có phương thức trìu tượng. để tạo phương thức trìu tượng ta import module **abc** (abstract base class)
- cấu trúc: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/250f764c-6586-44b4-881c-3fa96ba36b35)
- **lưu ý**: @abstractmethod là 1 decorator - một tính năng mạnh mẽ cho phép bạn thay đổi hoặc mở rộng hành vi của một hàm hoặc một lớp một cách linh hoạt mà không cần thay đổi mã nguồn gốc của chúng. Decorator này được sử dụng để xác định một phương thức là trừu tượng. Khi một phương thức được đánh dấu bằng @abstractmethod, điều đó có nghĩa là lớp chứa phương thức đó là một lớp trừu tượng và phương thức đó phải được triển khai (định nghĩa) trong các lớp con của nó.
- từ khóa **pass**: là một từ khóa được sử dụng để chỉ ra một khối mã không làm gì cả. Nó thường được sử dụng khi không có hành động cụ thể nào cần thực hiện.
### f. đóng gói
- **public**: là trạng thái công khai nhất trong ba mức độ, khi một thành phần trong class được khai báo ở dạng public tức là chúng ta có thể sử dụng được thành phần đó từ bất kỳ đâu trong chương trình. khai báo: **giống default trong java**
- **private**: phạm vị hẹp nhất trong lập trình hướng đối tượng, khi một thành phần trong đối tượng được khai báo ở dạng private, thì nó chỉ có phạm vi hoạt động ở trong class khai báo nó. khai báo: **__tenbien**
- ví dụ tổng hợp: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/f9242018-2a6d-4edc-9f32-20abf2b16c40)
### g. phương thức đặc biệt <đọc - biết - tự tìm hiểu thêm>
- chính là những hàm có sẵn tại python <br> ![image](https://github.com/nbn-03/Python/assets/98254107/dd5c221c-638e-4ff9-b0eb-a89ed18181e7)
- có thể tạo hoặc ghi thêm (nếu có từ trước ví dụ như: del - phần ví dụ) với mỗi đối tượng
- ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/e300708a-f4f9-4327-926b-9e2277df7f65)
### h. xóa đối tượng, phương thức và thuộc tính (chỉ có tại python)
- xóa một đối tượng: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/7d26a47b-a61a-4fc1-88be-4f3d2a0b1419)
- xóa một phương thức: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/984ffb4d-b555-4d58-8bc2-62f91170d09f)
- xóa một thuộc tính: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/ba7a86ab-326c-4e0f-bc2e-6ce5326caa77)
## 7. modules và package
### a. pip install và pypi
- pypi là một kho lưu trữ các package, module, tool và thư viện python của bên thứ 3, là mã nguồn mở.
- tool và thư viện chính được coi là modulo hoặc package tùy vào quy mô mức độ của mã nguồn
- sử dụng câu lệnh **pip install** trên cmd để tải các package trên pypi
- tải: **pip install ten_package**
- kiểm tra: **pip list** hoặc **pip show ten_package**
- xóa: **pip uninstall ten_package**
### b. modules and package
- trong python, module chính là 1 tập lệnh <1 file .py> để giải quyết 1 vấn đề hoặc cung cấp các chức năng 
- package là tập hợp các module <có thể chứa 1 hoặc nhiều module>, các package con. trong package bắt buộc phải có 1 file, file đó có thể trống hoặc chứa mã Python khởi tạo hoặc cấu hình cần thiết cho package. <br> ![image](https://github.com/nbn-03/Python/assets/98254107/dea1e066-9580-4672-beed-ad985db78532)
- cách sử dụng dựa trên import và from ... import ...
- ví dụ: **trong hình tại chú thích file --> module** <br> ![image](https://github.com/nbn-03/Python/assets/98254107/a3886116-b5cb-4375-8e53-e8a4e8a0f008)
- có thể import cùng lúc nhiều module trên 1 dòng
### c. bổ sung
- ![image](https://github.com/nbn-03/Python/assets/98254107/9b6cd56f-c454-4e00-98a8-dc11e1a4bf0b)
- với câu lệnh trên đúng khi chạy chính file đó
- còn else khi mà file đấy đóng vai trò làm module cho file khác
- cách tạo 1 hàm main trong python: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/b5055da7-d073-4913-a2d9-5e89258b52a0)
## 8. Errors and Exception
- lỗi chắc chắn có thể xảy ra trong quá trình code. có thể sử dụng tính năng xử lí lỗi để cố gắng lên kế hoạch cho những sai sót có thể xảy ra
- ví dụ: người dùng cố gắng ghi vào 1 tệp chỉ được mở ở mode = 'r'
- hiện tại khi gặp 1 lỗi bất kì chương trình sẽ dừng lại
- chúng ta có thể sử dụng xử lí lỗi để cho phép chương trình tiếp tục chạy ngay cả khi có lỗi
- 3 từ khóa sử dụng cho việc đó: **try**; **except**; **finally**
- cấu trúc basic: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/c11919c9-7090-45d3-b128-9989a647d3f7)
- trường hợp chỉ xử lý lỗi cụ thể: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/6648c92c-d907-4c19-a481-549dd06b4cfc)
- ví dụ tổng quát: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/ece758ec-5990-4b78-901d-7d6aecde285b)
- khi mở rộng sang nhiều tệp lớn hơn, các dự án, điều quan trọng là phải thực hiện các thử nghiệm tại chỗ.
- có 2 tool kiểm tra là **pylint** và **unittest**
### a. Pylint
- là tool xem xét code của bạn và báo cáo lại các vấn đề có thể xảy ra.
- tải package: **pip install pylint**
- để sử dụng: chạy lệnh **pylint ten_file.py** trên cmd,... vì là tool kiểm tra nên không cần import.
### b. unittest
- là module tích hợp này sẽ cho phép kiểm tra các chương trình của riêng bạn và kiểm tra xem bạn có nhận được kết quả đầu ra mong muốn hay không
- không cần download mà trực tiếp import sử dụng: **import unittest** ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/17a9136e-0c64-46fb-bf41-bdefa130f68b)
## 9. Python decorators
- định nghĩa: đã đề cập
- ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/6d0808c8-e2d0-4c64-b23b-512be7086de8) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/6b2193e2-dd1c-4e91-9e99-76bbb8b6ef3c)
## 10. Python Generators
- là một cách tiện lợi và hiệu quả để tạo ra các dãy giá trị một cách lười biếng (lazy evaluation), tức là giá trị chỉ được sinh ra khi cần thiết và không lưu trữ tất cả giá trị trong bộ nhớ như list. hiểu đơn giản là từ khóa **yield** giúp add sau vào 1 list ảo không lưu trong bộ nhớ
- ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/066cd717-6906-4923-94ce-eb3dcc90d35f) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/76f83574-4214-4c7f-a254-d3d125585a06)
- từ generators có thể ép kiểu sang list, tuple, ... cú pháp như ép kiểu thông thường
- **chú ý**:
  - vẫn có 1 cách dùng genetators ngoài từ khóa **yield** <br> ![image](https://github.com/nbn-03/Python/assets/98254107/c9982813-c195-4041-afc3-dd88c4c2bf80)
  - còn 1 phần mở rộng đọc tại link github đã đề cập bên trên
## 11. advanced python modules (đề cập giới thiệu qua một số module với phương thức và vẫn còn rất rất nhiều module với phương thức khác)
### a. Collections Module
- là một module chuẩn cung cấp một số cấu trúc dữ liệu mở rộng so với các cấu trúc dữ liệu cơ bản như list, tuple, và dictionary. Module này cung cấp các công cụ giúp bạn làm việc với dữ liệu một cách hiệu quả hơn trong nhiều tình huống khác nhau.
- hàm **Counter**: là một lớp trong module collections được sử dụng để đếm số lần xuất hiện của các phần tử. ví dụ:
- hàm **defaultdict**: là một lớp trong module collections cung cấp một cấu trúc từ điển mở rộng so với dict tiêu chuẩn. defaultdict cho phép bạn xác định một giá trị mặc định cho các key mà không tồn tại trong từ điển. Khi bạn truy cập một key không tồn tại, defaultdict sẽ tự động tạo ra key đó và gán giá trị mặc định cho nó. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/85d7978a-b11e-4da3-86d1-fd0ec545e223)
- hàm **nametuple**: là một lớp trong module collections cho phép bạn tạo ra các kiểu dữ liệu giống như tuple, nhưng mỗi trường (field) có thể được truy cập thông qua tên thay vì chỉ số như trong tuple thông thường (lưu ý: vẫn truy cập thông qua chỉ số được). ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/b4309a6c-6775-48c2-990f-32a018ae3b5c)
### b. OS module (tập chung vào opening and reading file and folders)
- câu lệnh: **import os**
- lệnh **os.getcwd()**:  là một hàm được sử dụng để lấy đường dẫn thư mục làm việc hiện tại
- lệnh **os.listdir("duong_dan)**: là một hàm được sử dụng để lấy danh sách các tên của tất cả các tệp và thư mục trong một thư mục cụ thể. nếu không truyền đối số thì sẽ hiểu là đường dẫn hiện tại
- di chuyển giữa các file và folder:
  - **import shutill**
  - câu lệnh: **shutill.move("duong_dan_source", "duong_dan_des")**
- xóa file và folder:
  - **os.unlink("duong_dan")**: phương thức này cũng xóa một tệp tin cụ thể được chỉ định bởi đường dẫn
  - **os.rmdir("duong_dan)**: được sử dụng để xóa thư mục cụ thể được chỉ định bởi đường dẫn path. Tuy nhiên, điều quan trọng cần lưu ý là phương thức này chỉ hoạt động nếu thư mục đó trống. Nếu thư mục chứa bất kỳ tệp tin hoặc thư mục con nào, phương thức này sẽ không thể xóa được và sẽ gây ra một ngoại lệ
  - **shutil.rmtree("duong_dan")**: xóa tất cả file và folder trong đường dẫn
  - **lưu ý**: Trước khi xóa một tệp tin hoặc thư mục, hãy đảm bảo rằng bạn đã kiểm tra và xác nhận rằng bạn đang xóa tệp tin/thư mục đúng và bạn muốn xóa nó. Xóa tệp tin/thư mục sẽ không thể đảo ngược, và mọi dữ liệu trong chúng sẽ bị mất vĩnh viễn.
  - một giải pháp an toàn được đưa ra là sử dụng module **send2trash**: được sử dụng để gửi các tệp và thư mục vào thùng rác thay vì xóa chúng một cách vĩnh viễn, giúp tránh việc mất dữ liệu không cần thiết hoặc nhầm lẫn khi xóa tệp.
  - tải: **pip install send2trash**
  - **import send2trash**
  - câu lệnh: **send2trash.send2trash("duong_dan)**
- **os.walk("duong_dan")**: là một hàm được sử dụng để duyệt qua tất cả các thư mục, tệp tin và các thư mục con bên trong một thư mục cụ thể. Hàm này trả về một bộ giá trị mỗi lần vòng lặp, bao gồm đường dẫn của thư mục hiện tại, danh sách các thư mục con và danh sách các tệp tin trong thư mục hiện tại. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/90822ef5-9f7d-4f6f-9ae3-6e24af0d4cc8) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/271ddb78-7143-43cd-a2fd-53b21ee534e9) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/4ea908cc-5304-4690-996d-3d1049e5b944)
### c. Datetime module
- câu lệnh **import datetime**
- **datetime.time(giờ,phút,giây)**: là một lớp được gọi là time. Lớp này được định nghĩa trong module datetime và được sử dụng để biểu diễn các đối tượng thời gian được truyền vào. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/3dfb5212-1de2-48df-b4c2-de02d428a5ca)
- **datetime.date(năm, tháng, ngày)**: giống phương thức **datetime.time(giờ,phút,giây)**. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/5ad18766-c917-4458-ab41-c70757eae77a)
- **datetime.datetime(năm, tháng, ngày, giờ, phút, giây): giống phương thức **datetime.time(giờ,phút,giây)**.
- nếu để thay đổi 1 đối số trên 3 phương thức trên: **.replace(ten_doiso = gia_tri_moi)** ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/f07ba738-0858-4c5a-b477-170812d18c62)
- trả về năm tháng ngày giờ phút giây hiện tại: **datetime.datetime.now()**
- hiện thị thứ: **ten_bien = datetime.datetime.now()** đồng thời **ten_bien.weekday()**. tại đây sẽ là trả về số hiểu là 0:Monday;.....
- thao tác tính khoảng thời gian: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/c5ca88b3-d810-4ed4-9fa8-1d25feb65af8)
- hiển thị lịch: **import calendar**
  - lịch của tháng: **calendar.month(nam, thang)**
  - lịch cả năm: **calendar.calendar(nam)**
### d. math and random module
- câu lệnh: **import math**
- hiển thị phương thức trong math: **help(math)**
- làm tròn xuống số nguyên: **math.floor(ten_bien)**
- làm tròn lên số nguyên: **math.ceil(ten_bien)**
- **round(ten_bien, chu_so_lam_tron)**: làm tròn đến chữ số yêu cầu. nếu không có chữ số làm tròn sẽ làm tròn đến số nguyên.
- số pi: **math.pi**
- hằng số euler: **math.e**
- **math.log(hang_so, co_so)** nếu không truyền cơ số sẽ auto là **math.e**
- câu lệnh: **import random**
- **random.randint(start, end)**: sinh ra số nguyên bất kì trong phạm vi đề ra
- **random.seed(chi_so)**: được sử dụng trong tạo số ngẫu nhiên. đảm bảo với với 1 giá trị truyền vào một seed sẽ cố định với một số hoặc bộ số random. bất kì lần nào chạy cùng 1 giá trị seed sẽ tạo ra cùng 1 số hoặc bộ số
- **random.choice(ten)**: dùng với list và tuple để random 1 số trong bộ số đó
- **random.choises(ten, k = so_phan_tu)**: random ra 1 list có so_phan_tu và các phần tử có thể trùng lặp nhau
- để không random ra 1 list không có phần tử nào trùng nhau: **random.sample(ten, k = so_phan_tu)**
- **random.shuffle(ten_list)**: chỉ dùng cho list để xáo trộn các phần tử trong list
- **random.uniform(start, end)**: random 1 số thực bất kì
### e. python debugger
- câu lệnh: **import pdb**
- **pdb.set_trace()**: là một cách để thêm điểm dừng (breakpoint) vào mã Python của bạn để bạn có thể kiểm tra giá trị của các biến và dòng lệnh trong quá trình chạy chương trình.
- chi tiết tại: https://www.geeksforgeeks.org/debugging-in-python-with-pdb/
### f. regular expressions
- câu lệnh: **import re**
- câu lệnh **in** để tìm chuỗi con trong chuỗi lớn kết quả trả về true hoặc false
- **re.search(chuoi_con, chuoi_lon)**: kết quả trả về lần xuất hiện đầu tiên của chuỗi con trong chuỗi lớn nếu có sẽ là (vị trí bắt đầu+1, vị trí kết thúc) và 1 số thông tin khác, nếu không thì sẽ là None
  - ten_bien = re.search(chuoi_con, chuoi_lon)
  - để truy cập lấy dữ liệu sử dụng: **ten_bien.span()** -> tuple; **ten_bien.start()**, **ten_bien.end()** -> int 
- **re.findall(chuoi_con, chuoi_lon)**: trả về các lần xuất hiện của chuỗi con trong chuỗi lớn -> list
  - ten_bien = re.findall(chuoi_con, chuoi_lon)
  - số lần xuất hiện: **len(ten_bien)**
- **re.filliter(chuoi_con, chuoi_lon)**: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/2ceb9204-fa88-448d-ac5c-58b1218fc09e) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/e959d63a-7852-4d5d-82c8-2a92ae8f0ee7) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/d1941061-041d-40ca-9f06-d61465365907)
- **điều đặc biệt: chuoi_con có thể thay bằng 1 mẫu định dạng chung để tìm ra những chuỗi con có định dạng giống nhau**
- cách viết định dạng:
  - định dạng: **r"mau"**, đặt r phía trước để hiểu dấu \ không có nghĩa là dấu như: \n; \t; ...
  - \d: một số
  - \w: một chữ hoặc số hoặc kí tự đặc biệt
  - \s: khoảng trắng
  - \D: không là số
  - \W: không là chữ hoặc số hoặc kí tự đặc biệt. **! @ # $ % ^ & * ( ) - _ = + [ ] { } ; : ' " , . < > / ? \ | `**
  - \S: không có khoảng cách
  - ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/91db05b6-8d83-4918-becb-2d80de2949fb)
  - **với \ xuất hiện nhiều lần có thể gây rối để thu gọn lại sẽ dùng:** <br> ![image](https://github.com/nbn-03/Python/assets/98254107/56c34a0c-26e3-4292-b152-2c8fa963d219)
  - ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/47bbf2e2-9495-4541-9263-7b0a8e028b2a)
- với 1 dãy định dạng ta muốn nhóm lại thành các nhóm để phục vụ xử lí: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/8f60cf3d-f005-4733-8603-cff4ce886c3b) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/7e73afcd-5a2f-421d-b14c-c4eb4a874664)
- để tìm kiếm nhiều thuật ngữ có thể sử dụng toán tử **or**: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/17cbfb24-cebd-4222-98c3-ae22bc8dd35f)
- chú ý với từ khóa **re.findall(chuoi_con, chuoi_cha)**: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/7d915ccc-b5d8-409d-b087-156471721a9f) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/59fe081e-e5ca-45e9-b86f-94c94d95a937) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/7495645e-d972-4a8c-a946-304d96d8ff91) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/2acb6a9b-5553-4edb-8330-51008200bba9)
- Để loại trừ các ký tự, chúng ta có thể sử dụng ký hiệu ^ kết hợp với bộ dấu ngoặc []. Bất cứ điều gì bên trong dấu ngoặc đều bị loại trừ. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/947ffda0-ca50-4cbf-ab76-7455c48340c5) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/1bb5a082-9cdf-40e4-8552-5be107fe1553) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/131f6b03-d674-496e-8061-66c336babf66)
- để lọc ra dạng **word-word**: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/83d1b035-1c9c-40bc-887f-a2fc6d0cdce5)
- tìm kiếm trong text để tìm chuỗi "cat" kết hợp với một trong các từ "fish", "nap", hoặc "claw". ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/ad32452d-f933-451b-aff2-2500fc76634d)
### g. timing your python code (có 2 cách)
- câu lệnh: **import time**
- thời gian bắt đầu: **ten_bien1 = time.time()**
- thời gian kết thúc: **ten_bien2= time.time()**
- khoảng thời gian chạy code: **ten_bien2 - ten_bien1**
- câu lệnh: **import timeit**
- **timeit.timeit( , ,number =  )**: một hàm trong Python được sử dụng để đo thời gian thực thi của một đoạn mã Python. Nó thường được sử dụng để đo thời gian thực thi của một đoạn mã nhất định hoặc một hàm cụ thể với number là số lần thực hiện lặp lại. <br> ![image](https://github.com/nbn-03/Python/assets/98254107/d1c14911-05a8-4c69-b255-08cddf199a59) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/c2e855c4-8d6f-4d26-9fae-9d087568ae84)
### h. zipping and unzipping file trong python
- câu lệnh: **import zipfile**
- nén:
  - **ten_bien = zipfile.ZipFile("duong_dan_va_ten_file_zip.zip","w")**: khi tạo xong file này sẽ trống giờ ta sẽ nén các file hoặc folder rồi chèn vào
  - **ten_bien.write("duong_dan_file_hoac_folder_nen", zipfile.ZIP_DEFLATED)**
  - **ten_bien.close()**
- giải nén:
  - **ten_bien = zipfile.ZipFile("duong_dan", "r")**
  - **ten_bien.extractall("duong_dan_va_ten_gian_nen")**
- ví dụ: <br>  ![image](https://github.com/nbn-03/Python/assets/98254107/411454a3-2766-4572-b0bd-0ae9df1b0907) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/6186bad0-1c15-4bac-9ab0-d8091ca9afbd)
- bên trên sẽ nén từng file hoặc folder rồi chèn vào file zip có cách tối ưu là thêm hết những file hoặc folder và folder chung rồi nén
  - **import shutil**
  - **shutil.make_archive("duong_dan_va_ten_file, 'zip',"duong_dan_folder_chung")**: nén
  - **shutil.unpack_archive("duong_dan_filezip.zip", "duong_dan_va_ten_giai_nen", 'zip')**: giải nén
- ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/ba3f14c9-5a83-4637-805a-bb809aaeffad) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/6d8dfa5b-a56e-407d-bdb7-2830917acf6e)
- **chú ý:** ví dụ trên tại giải nén output_filename chính là đường dẫn file.zip
## 12. web scraping
- là một thuật ngữ dùng cho kĩ thuật liên quan đến việc tự động thu thập dữ liệu từ 1 web ví dụ như: tải hình ảnh hoặc thông tin;...
- quá trình này thường bao gồm việc truy cập vào web, tìm kiếm và phân tích cấu trúc của web để trích xuất thông tin mong muốn
- những điều chính cần hiểu:
  - quy tắc của web scraping
  - hạn chế của web scraping
  - HTML và CSS cơ bản
- **tóm tắt quy tắc và hạn chế**: Hãy nhớ rằng bạn phải luôn có quyền đối với trang web mà bạn đang thu thập dữ liệu (nếu không có hãy cố gắng xin quyền)! Kiểm tra các điều khoản và điều kiện của trang web để biết thêm thông tin. Ngoài ra, hãy nhớ rằng máy tính có thể gửi yêu cầu đến một trang web rất nhanh, vì vậy trang web đó có thể chặn địa chỉ IP máy tính của bạn nếu bạn gửi quá nhiều yêu cầu với tốc độ nhanh. Cuối cùng, các trang web luôn thay đổi! Rất có thể bạn sẽ cần cập nhật mã của mình thường xuyên cho các công việc quét web dài hạn. 
- thành phần chính của front-end (giao diện người dùng) của web
  - front-end: HTML + CSS + JavaScript
  - khi xem 1 web, trình duyệt sẽ không hiển thị toàn bộ mã nguồn phía sau thay vào đó nó hiển thị HTML, và một số CSS và JS mà trang web gửi tới trình duyệt của bạn
  - HTML được sử dụng để tạo cấu trúc cơ bản và nội dung của web
  - CSS được sử dụng để thiết kế và tạo kiểu cho 1 web, nơi các phần tử được đặt và trông thế nào
  - JS được sử dụng để xác đính tính tương tác các thành phần của 1 web
  - để web scraping hiệu quả sẽ tập chung vào **HTML và CSS**
- HTML
  - không phải là ngôn ngữ lập trình
  - có mặt trên mọi trang web
  - để xem HTML của 1 web: chuột phải -> select "view page source"
  - `<DOCTYPE html>`: Tài liệu HTML sẽ luôn bắt đầu bằng khai báo kiểu này, cho trình duyệt biết đó là tệp HTML.
  - Các khối thành phần của tài liệu HTML được đặt giữa `<html>` và `</html>`.
  - Các kết nối dữ liệu và tập lệnh (như liên kết tới tệp CSS hoặc tệp JS) thường được đặt trong khối  `<head>`.
  - Khối thẻ `<title>` xác định tiêu đề của trang web (nó hiển thị trong tab của trang web bạn đang truy cập).
  - Nằm giữa thẻ `<body>` và `</body>` là các khối sẽ hiển thị cho khách truy cập trang web.
  - Tiêu đề được xác định bởi thẻ `<h1>` đến `<h6>`, trong đó số biểu thị cấp độ của tiêu đề.
  - Các đoạn văn được xác định bằng thẻ `<p>`, đây thực chất chỉ là văn bản bình thường trên trang web.
  - ngoài ra có nhiều thẻ khác ngoài những thẻ này
- CSS
  - sử dụng tags để xác định phần tử html nào sẽ được tạo kiểu
  - ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/a65c4ca1-992b-45cc-8e81-301a06f416d1)
  - `<link rel="stylesheet" href="styles.css">`: Đây là một thẻ `<link>` được sử dụng để liên kết với một tệp CSS bên ngoài để trang web có thể sử dụng các quy tắc kiểu từ tệp đó. Trong trường hợp này, tệp CSS có tên là "styles.css".
  - `<p id='para2'>Some Text</p>` hoặc `<p class='cool'>Some Text</p>`: văn bản "Some Text" được đặt bên trong thẻ `<p>`. Đặc biệt, có một thuộc tính với giá trị là ... được gán cho phần tử này, cho phép nó được xác định và tùy chỉnh bằng CSS hoặc JavaScript. id là id duy nhất cho thẻ HTML và phải là duy nhất trong tài liệu HTML, về cơ bản là một kết nối sử dụng một lần. lớp xác định một kiểu chung mà sau đó có thể được liên kết với nhiều thẻ HTML. Về cơ bản, nếu bạn chỉ muốn một thẻ html có màu đỏ, bạn sẽ sử dụng thẻ id, nếu bạn muốn một số thẻ/khối HTML có màu đỏ, bạn sẽ tạo một lớp trong tài liệu CSS của mình và sau đó liên kết nó với phần còn lại trong số này khối. <br> ![image](https://github.com/nbn-03/Python/assets/98254107/919012ff-09df-4471-9d53-d58f054ca9b1)
- để web scraping chúng ta cần dùng những thư viện ngoài không tích hợp sẵn như: **request**, **lxml**, **bs4**
### a. lấy page title
