# Bài 1: Đếm tần suất ký tự trong chuỗi
# Nhập 1 chuỗi, tạo dictionary đếm số lần xuất hiện của từng ký tự
# (không phân biệt hoa/thường).
# Ví dụ:
# "hello" -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
def dem_tan_suat (s):
    s.lower()
    counts = {}
    for char in s:
        if char != ' ':
            counts[char] = counts.get(char, 0) + 1
    return counts
print(dem_tan_suat("Hello"))


# Bài 2: Tìm 2 số có tổng bằng target
# Cho 1 list số nguyên và 1 số target.
# Tìm 1 cặp số bất kỳ trong list có tổng đúng bằng target.
# Trả về cặp đó, hoặc None nếu không tìm được.
# Ví dụ:
# numbers = [2, 7, 11, 15], target = 9
# Kết quả: (2, 7)
def Tim_2_so(numbers, target):
    seen = set() # tạo một tập hợp rỗng để ghi nhớ các số đã từng duyệt qua !
    for num in numbers:
        complement = target - num # complement = số còn thiếu để cộng với num ra đúng target
        if complement in seen: # kiểm tra xem số còn thiếu này đã từng xuất hiện ở bước trc hay chưa
            return (complement, num)
        seen.add(num) 
    return None # duyệt hết cả list mà ko tìm đc cặp nào thì trả về None
print(Tim_2_so([2, 7, 11, 15], 9))



# Bài 3: Gộp 2 dictionary điểm số
# Cho 2 dictionary tên -> điểm (2 ky thi khac nhau), co the co ten trung
# hoac khong trung nhau hoan toan.
# Tao dictionary moi chua diem trung binh cua moi nguoi:
# - Neu ten co o ca 2 dictionary -> lay trung binh cong 2 diem.
# - Neu ten chi co o 1 trong 2 -> giu nguyen diem do.
# Vi du:
# d1 = {"An": 8, "Binh": 7}
# d2 = {"An": 6, "Chi": 9}
# Ket qua: {"An": 7.0, "Binh": 7, "Chi": 9}
def diem_tb (d1, d2):
    result = {}
    all_names = set(d1) | set(d2)
    for name in all_names:
        if name in d1 and name in d2:
            result[name] = (d1[name] + d2[name]) / 2
        elif name in d1:
            result[name] = d1[name]
        else:
            result[name] = d2[name]
    return result
print(diem_tb({"An": 8, "Binh": 7}, {"An": 6, "Chi": 9}))



# Bài 4: Kiểm tra 2 chuỗi có phải anagram không
# 2 chuoi la anagram neu chua dung cac ky tu giong nhau,
# chi khac nhau ve thu tu sap xep.
# Vi du:
# "listen" va "silent" -> True
# "hello" va "world" -> False
def kiem_tra (s1, s2):
    chuoi_1 = sorted(s1)
    chuoi_2 = sorted(s2)
    return chuoi_1 == chuoi_2
s1 = "listen"
s2 = "silent"
print(f"'{s1}' và '{s2}': {kiem_tra(s1, s2)}")



# Bài 5: Loại bỏ phần tử trùng, giữ nguyên thứ tự xuất hiện đầu tiên
# Cho 1 list co phan tu trung, tra ve list moi chi giu lai
# lan xuat hien DAU TIEN cua moi gia tri, dung theo thu tu ban dau.
# (Khong duoc chi dung set() de tra ve truc tiep, vi set khong giu thu tu)
# Vi du:
# [3, 1, 2, 3, 1, 4] -> [3, 1, 2, 4]
def loai_pt_trung(a):
    seen = set()
    result = [] # tạo một list rỗng
    for num in a: 
        if num not in seen: # xem num đã có trong seen chưa
            seen.add(num) # thêm vào danh sách kết quả
            result.append(num)
    return result # trả về danh sách kết quả 
a = [3, 1, 2, 3, 1, 4]
print(loai_pt_trung(a))



# Bài 6: Nhóm số theo chẵn/lẻ vào dictionary
# Cho 1 list so nguyen, tra ve 1 dictionary co 2 khoa "chan" va "le",
# moi khoa chua list cac so tuong ung.
# Vi du:
# [1, 2, 3, 4, 5] -> {"chan": [2, 4], "le": [1, 3, 5]}
def chan_le(numbers):
    result = {"chan": [], "le": []}
    for num in numbers:
        if num % 2 == 0:
            result ["chan"].append(num)
        else:
            result ["le"].append(num)
    return result
a = [1, 2, 3, 4, 5]
print(chan_le(a))



# Bài 7: Tìm khoảng cách lớn nhất giữa 2 phần tử liên tiếp (sau khi sắp xếp)
# Cho 1 list so, sap xep tang dan, roi tim hieu LON NHAT
# giua 2 so lien ke nhau trong day da sap xep.
# Vi du:
# [1, 5, 3, 19, 18, 25] -> sap xep: [1, 3, 5, 18, 19, 25]
# Hieu lon nhat: 18 - 5 = 13
def kh_ca_ln(a):
    a.sort() # sắp xếp tăng dần 
    best = 0 # biến lưu hiệu lớn nhất tìm đc
    for i in range(len(a) - 1):
        diff = a[i + 1] - a[i] # hiệu giữa 2 phần tử liền kề
        if diff > best:
            best = diff
    return best
print(kh_ca_ln([1, 5, 3, 19, 18, 25]))   



# Bài 8: Tính số dư tiết kiệm qua nhiều năm, có rút gốc từng phần
# Cho so tien goc, lai suat %/nam co dinh, va 1 list so tien rut ra moi nam.
# Tinh so du con lai sau n nam.
# Moi nam: cong lai truoc, roi tru so tien rut trong nam do.
# Vi du:
# von = 1000000, lai_suat = 5, rut = [50000, 0, 100000]
# Nam 1: 1000000*1.05 - 50000 = ...
def ttk (von, ls, rut):
    so_du = von # khởi tạo số vốn ban đầu
    for tien_rut in rut:
        so_du *= (1 + ls / 100) # cộng lại suất vào số dư hiện tại trc
        so_du = so_du - tien_rut # trừ đi số tiền rút ra trong năm đó
    return so_du # trả về số dư cuối cùng sau khi qua các năm
print(ttk(1000000, 5, [50000, 0, 100000]))



# Bài 9: Tìm từ dài nhất trong câu
# Cho 1 chuoi cau (nhieu tu cach nhau boi dau cach),
# tra ve tu dai nhat.
# Neu co nhieu tu cung do dai lon nhat, tra ve tu xuat hien DAU TIEN.
# Vi du:
# "toi dang hoc python moi ngay" -> "python"
def tu_dai_nhat(a):
    tdn = ""
    for i in a.split():
        if len(i) > len(tdn):
            tdn = i
    return tdn
print(tu_dai_nhat("toi dang hoc python moi ngay"))


# Bài 10: Thống kê điểm danh
# Cho 1 dictionary ten -> list cac buoi co mat (1 = co mat, 0 = vang).
# Tinh ty le di hoc (%) cua tung nguoi,
# va tim nguoi co ty le di hoc THAP NHAT.
# Vi du:
# {"An": [1,1,0,1], "Binh": [1,0,0,1]}
# An: 75%, Binh: 50% -> nguoi thap nhat: Binh
def tk_dd(data):
    min_ty_le = 100  # Khởi tạo tỷ lệ thấp nhất ban đầu là 100%
    ng_th_nh = ""  # Khởi tạo biến lưu tên người có tỷ lệ thấp nhất
    for ten, buoi_hoc in data.items():  # Duyệt qua từng học viên và danh sách điểm danh của họ
        ty_le = (sum(buoi_hoc) / len(buoi_hoc)) * 100  # Tính tỷ lệ đi học phần trăm

        if ty_le < min_ty_le:  # Nếu tỷ lệ hiện tại thấp hơn mức thấp nhất đang lưu
            min_ty_le = ty_le  # Cập nhật lại tỷ lệ thấp nhất mới
            ng_th_nh = ten  # Cập nhật lại tên người có tỷ lệ thấp nhất
            
    return ng_th_nh  # Trả về tên người có tỷ lệ đi học thấp nhất





