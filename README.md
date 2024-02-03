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
- chú ý: với truy xuất phần tử trong String ở java không dùng truy xuất như python mà dùng: **ten_chuoi.charAt(chi_muc)** =>> **tương tác trên chuỗi của java đều thông qua phương thức đa phần sẽ khác với python (vẫn có 1 số giống nhau giữa 2 ngôn ngữ)**
- trong các chuỗi có số thứ tự gọi là chỉ mục chúng ta có thể sử dụng chỉ mục (mỗi phần tử trong chuỗi đều có 1 số thứ tự bắt đầu từ 0) để lấy hoặc cắt các phần con của chuỗi
- ví dụ: <br>![image](https://github.com/nbn-03/Python/assets/98254107/338e4117-5c62-4997-b3d6-b64ecee92cd3)
- chỉ mục được đặt trong [ ]
- ví dụ: <br>![image](https://github.com/nbn-03/Python/assets/98254107/aa1c8be9-1471-4ac9-90d1-fe7db1f5c530)<br>![image](https://github.com/nbn-03/Python/assets/98254107/a36583f0-6f36-4c55-aef2-b8e0b12fe409)
- slicing cho phép bạn lấy 1 phần gồm nhiều kí tự (phần tử) trong chuỗi. lệnh: **ten_chuoi[start:stop:step]**. nếu không truyền đối số cho stop và step và start nó sẽ tự động stop: vị trí cuối của chuỗi, step: 1, start: vị trí bắt đầu. đảo ngược chuỗi thì step là số âm.
- câu lệnh để in ra màn hình: **print()**. print sẽ tự động xuống dòng khi thực hiện câu lệnh. \n - xuống dòng. \t sử dụng tab
- câu lệnh đo độ dài của chuỗi: **len(ten_chuoi)**
- xử lí chuỗi trong python khác java là với java có thể dùng dấu cộng "+" để nối các kiểu dữ liệu với nhau để tạo thành 1 chuỗi. với python để nối chuỗi cần phải ép kiểu thành KDL String để nối chuỗi. ngoài ra trong python còn có phép nhân "*" => để nhân các chuỗi giống nhau; phép so sánh "< > <= >= ==" để so sánh chuỗi (với java so sánh chuỗi cần phương thức hỗ trợ).
- ép kiểu: **KDL(ten_bien)** <br> ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/3cf9b24f-8994-46a1-82f5-6d771b352245)
- chuyển thành chũ hoa: **ten_chuoi.upper()**
- chuyển thành chữ thường: **ten_chuoi.lower()**
- tách 1 chuỗi thành 1 list: **ten_chuoi.split("vi_tri_tach")**. chú ý đối số của hàm split không có gì sẽ auto là dấu cách.
- comment 1 câu trong python dùng #; comment 1 đoạn trong python """ """
- để nối chuỗi ngoài cách ép kiểu ta có thể dùng format <br> ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/9b446db2-3d00-4c7b-8772-66bae10647ff) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/85b6d7e5-f625-471f-a4b5-b47ca7ad3947) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/71d55a13-dccd-4cf9-b7b4-ba4a771f5c33) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/fe157ed4-7bf2-462f-8e2b-48e7ed0ec256) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/1d84f5b3-d13e-44a5-a650-9b642fedaac7) <br> **cách dùng cho python 3.6 trở lên** <br>![image](https://github.com/nbn-03/Python/assets/98254107/ff0bcaf5-748a-465d-8d26-4cf13093ef80)
- so sánh chuỗi ta có thể dùng **toán tử so sánh** còn java bắt buộc phải dùng phương thức.
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
- tích hợp truy xuất ra cả chỉ số và giá trị: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/ba4f1325-defc-4fb2-afb6-9cbfa0825dc4) <br> **không chỉ chuỗi mà còn list, tuple, set, dictionary**
- <br> ![image](https://github.com/nbn-03/Python/assets/98254107/747070a7-b015-48ee-a6f7-bd107fc155ca) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/70406ac3-d397-4c69-a2d9-d5d12bc10b67)
- có thể dung **in** để kiểm tra phân tử có nằm trong chuỗi, list,... hay không. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/492a201c-6997-48c4-913b-9bc9b5b7090c)
- max, min trong chuỗi, list,...: **max(ten)**' **min(ten)**
- **nhập từ bàn phím** câu lệnh: **input()**. ví dụ: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/1a330537-f3ca-450c-ad49-17323b9879b7) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/2a4f2fb9-2b01-4110-b989-16371be05de8) <br> **vì nhập vào từ bàn phím kiểu dữ liệu lúc nào cũng là String vì vậy có thể ép kiểu từ khi nhập** <br> ![image](https://github.com/nbn-03/Python/assets/98254107/bb955ff9-7ac2-4b20-b396-cf67cd78d0dd)
- **khuyến cáo nên dùng cách tường mình cách này nên đọc cho biết** <br> ![image](https://github.com/nbn-03/Python/assets/98254107/ceae7e86-7d39-43b0-8946-dc20a1bcad31) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/df97b9b0-ab63-42e8-9f7d-99d94c952096) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/d0676e94-2cdb-48c5-a635-3fd8c5b360ea) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/2d8748e0-08d6-4a13-bf34-6ed9ab52c6f2) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/4d39c05d-1767-4801-b892-10a48251abea) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/b15fadc5-dd6f-408c-9897-26b49aae27a1) <br> ![image](https://github.com/nbn-03/Python/assets/98254107/b2156a6e-0fc3-4f10-88b1-079cc9ecc3ab)
## 5. hàm và phương thức
###  a. hàm
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
 - ví dụ bài tập về hàm: <br> ![image](https://github.com/nbn-03/Python/assets/98254107/63d3cfc9-6944-4578-b6b6-9ef328e371f3)
 - Lambda Expressions, Map, and Filter:
  - hàm **map**
