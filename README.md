# DHKL18A3HN_Nhom7_case9
Ngày 25/11/2025
Bản Báo Cáo Nhóm 7 (thực hiện case 9)

Kính gửi: thầy Cao Diệp Thắng (giảng viên bộ môn)
Đây là bản báo cáo về:
	-quá trình làm việc của cả nhóm
	-dữ liệu và kết quả nhóm thu được sau khi làm việc với dữ liệu

1.Danh sách và công việc của nhóm:

Họ và tên thành viên	Nội dung công việc
1.	Đinh Văn Dự	Xử lí dữ liệu đầu vào +tách cột
2.	Lại Đình Chung	tính toán điểm tổng+siclicing+phân nhóm theo tổng điểm
3.	Lương Nguyễn Tấn Dũng	Thống kê + phân tích dữ liệu +đồng hoàn thiện báo cáo+vẽ biểu đồ
4.	Tống Tiến Đạt	Thống kê top 10 điểm của các kỳ
5.	Nguyễn Xuân Đỉnh
(NHÓM TRƯỞNG)	Tổng hợp code các thành viên+hoàn tiện file theo yêu cầu+vẽ biểu đồ+hoàn thiện báo cáo 

2.Hướng và chi tiết  xử lý dữ liệu
-phần xử lý dữ liệu đầu vào,tách cột:
. đọc file semester1_scores.csv và semester2_scores.csv bằng np.loadtxt hoặc np.genfromtxt
. kiểm trad type, shape
. tách thành các mảng: sid,midterm,final,attendance_hw
. xuất 5 giá trị đầu/ cuối
.kiểm tra dữ liệu lỗi, thiếu, định dạng
-tính toán điểm tổng+siclicing+phân nhóm theo tổng điểm:
. slicing chia nhóm sinh viên đầu- giữ- cuối.
. phân loại theo tổng điểm :
     -xuất sắc 
     -khá 
     -Trung bình 
     -Yếu ( dùng boolean mask)
-Thống kê + phân tích dữ liệu +đồng hoàn thiện báo cáo :
.tính thống kê :mean, std,min,max,median cho từng loại điểm
.tính thống kê chung mỗi học kỳ.
.dùng np.diff() để đánh giá thay đổi điểm giữa 2 học kỳ
. xác định sinh viên tiến bộ mạnh hoặc tụt mạnh

-Thống kê top 10 điểm của các kỳ:
.so sánh chi tiết 2 học kỳ bằng broadcasting
.fancy indexing để lấy:
   -top 10 điểm từng học kỳ
   -top 10 điểm tiến bộ nhất
.xây bảng tổng hợp so sánh từng sinh viên.

	-Tổng hợp code các thành viên+hoàn tiện file theo yêu cầu+hoàn thiện báo cáo :
	       .Tổng kết và kết nối các đoạn code của thành viên 
	       .Hoàn thiện và xuất file theo yêu cầu
	       .Vẽ biểu đồ
	       .Viết báo cáo chung

3.Biểu đồ và phân tích kết quả học tập
  .vẽ biểu đồ qua matplotlib.pyplot

 	 
*phân tích dữ liệu thông qua biểu đồ :

-Phân phối điểm tổng hk1:
+phổ điểm trải dài từ: 5~9(điểm) 
+ không có điểm dưới mức kém(dưới điểm 4)
+phần đa điểm nằm ở khoảng :6~7(điểm)
+điểm nhiều sinh viên đạt được nhất là :6,5(điểm)
	-phân phối điểm tổng hk2:
+phổ điểm trải dài từ 3~8(điểm)
+ xuất hiện một vài điểm kém (dưới 4 điểm)
+mức điểm phổ thông ở khoảng:6,5 đến hơn 7 (điểm)
+mức điểm chung của các sinh viên tăng 



*nhận xét chung:
+phổ điểm phần đa của các sinh viên đều trong khoảng:6~8(điểm)
+hk1 sinh viên đều có điểm ở mức trung bình ~6,5(điểm) ,ở hk2 điểm trung bình của sinh viên có xu hướng tăng  đến khoảng 7 điểm hơn nhưng lại xuất hiện và sinh viên có đi-ểm kém (dưới 4 điểm)
