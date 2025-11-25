import numpy as np
def tai_du_lieu_diem(ten_file):
    du_lieu = np.loadtxt(ten_file, delimiter=',', dtype=str, skiprows=1)
    
    if du_lieu.ndim == 1:
        diem_so = du_lieu.astype(float)
    else:
        # Lấy cột cuối cùng (giả định là điểm số)
        diem_so = du_lieu[:, -1].astype(float)
    return diem_so

# Tải điểm số từ file
diem_hk1 = tai_du_lieu_diem('semester1_scores.csv')
diem_hk2 = tai_du_lieu_diem('semester2_scores.csv')

# --- Đồng nhất Kích thước Mảng ---
kich_thuoc_toi_thieu = min(diem_hk1.size, diem_hk2.size)
diem_hk1 = diem_hk1[:kich_thuoc_toi_thieu]
diem_hk2 = diem_hk2[:kich_thuoc_toi_thieu]

# Tạo Mã sinh viên (np.arange)
so_luong_sv = len(diem_hk1)
ma_sv = np.arange(1, so_luong_sv + 1)
print(f" Đã tải, phân tích dữ liệu của {so_luong_sv} sinh viên.")
# Thống kê Mô tả Chung

print(" Thống kê Chung cho 2 Học kỳ")
print(f"HK1: Trung bình={np.mean(diem_hk1)}, ĐL chuẩn={np.std(diem_hk1)}, Min={np.min(diem_hk1)}, Max={np.max(diem_hk1)}, Trung vị={np.median(diem_hk1)}")
print(f"HK2: Trung bình={np.mean(diem_hk2)}, ĐL chuẩn={np.std(diem_hk2)}, Min={np.min(diem_hk2)}, Max={np.max(diem_hk2)}, Trung vị={np.median(diem_hk2)}")
# Phân tích Thay đổi Điểm

diem_gop = np.vstack((diem_hk1, diem_hk2))
thay_doi_diem = np.diff(diem_gop, axis=0).flatten()
thay_doi_diem_lam_tron = np.round(thay_doi_diem, 2) 

print(" Phân tích Thay đổi Điểm")
print(f"Thay đổi điểm trung bình: {np.mean(thay_doi_diem)}")
print(f"Thay đổi lớn nhất: {np.max(thay_doi_diem)}, Nhỏ nhất: {np.min(thay_doi_diem)}")
# Xác định Tiến bộ/Giảm sút Mạnh

NGUONG_TIEN_BO = 2
NGUONG_GIAM_SUT = -2

chi_so_tien_bo = np.where(thay_doi_diem >= NGUONG_TIEN_BO)[0]
chi_so_giam_sut = np.where(thay_doi_diem <= NGUONG_GIAM_SUT)[0]

print(" Danh sách tiến bộ, giảm sút Mạnh")
print(f"Ngưỡng: Tiến bộ (số điểm giữa 2 học kỳ tăng) >= {NGUONG_TIEN_BO},Giảm sút (số điểm giữa 2 học kỳ giảm) <= {NGUONG_GIAM_SUT}")

print(" Danh sách tiến bộ mạnh:")
if chi_so_tien_bo.size > 0:
    print(f"{'Mã SV':<6} | {'HK1':<20} | {'HK2':<20} | {'Thay đổi':<10}")
    sv_tb = ma_sv[chi_so_tien_bo]
    diem_hk1_tb = diem_hk1[chi_so_tien_bo]
    diem_hk2_tb = diem_hk2[chi_so_tien_bo]
    diem_tb_tien_bo = thay_doi_diem[chi_so_tien_bo] 
    
    for i in range(len(sv_tb)):
        # Bỏ định dạng trong vòng lặp in
        print(f"{sv_tb[i]:<6} | {diem_hk1_tb[i]:<20} | {diem_hk2_tb[i]:<20} | {diem_tb_tien_bo[i]:<10}")
else:
    print("Không có sinh viên tiến bộ mạnh.")
print(" Danh sách giảm sút mạnh:")
if chi_so_giam_sut.size > 0:
    print(f"{'Mã SV':<6} | {'HK1':<20} | {'HK2':<20} | {'Thay đổi':<10}")
    sv_gs = ma_sv[chi_so_giam_sut]
    diem_hk1_gs = diem_hk1[chi_so_giam_sut]
    diem_hk2_gs = diem_hk2[chi_so_giam_sut]
    diem_tb_giam_sut = thay_doi_diem[chi_so_giam_sut]

    for i in range(len(sv_gs)):
        print(f"{sv_gs[i]:<6} | {diem_hk1_gs[i]:<20} | {diem_hk2_gs[i]:<20} | {diem_tb_giam_sut[i]:<10}")
else:
    print("Không có sinh viên giảm sút mạnh.")