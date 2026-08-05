# --- Bài 1 — Tổng các phần tử ở vị trí LẺ ---
# Đề bài: Cho dãy số a1, a2, a3,... Tính tổng CHỈ các phần tử ở vị
# trí LẺ (a1 + a3 + a5 + ...), bỏ qua vị trí chẵn.
#
# Input:  a = [10, 20, 30, 40, 50]   (a1=10, a2=20, a3=30, a4=40, a5=50)
# Output: 90   (= a1 + a3 + a5 = 10 + 30 + 50)

a = [10, 20, 30, 40, 50]
tong = 0

# Dùng enumerate() để vừa lấy được index vừa lấy được giá trị của phần tử
for index, value in enumerate(a):
    # Kiểm tra xem index có phải là số chẵn không (0, 2, 4...) 
    # tương ứng với vị trí 1, 3, 5... trong đề bài
    if index % 2 == 0:
        tong += value

print(f"Tong cac phan tu o vi tri le la: {tong}")


# --- Bài 2 — Tổng đan dấu bắt đầu bằng dấu trừ ---
# Đề bài: Cho dãy số a. Tính: -a1 + a2 - a3 + a4 - ...
# (giống bài mẫu nhưng ĐẢO dấu bắt đầu)
#
# Input:  a = [5, 3, 8, 2]
# Output: -8   (= -5 + 3 - 8 + 2)

a = [5, 3, 8, 2]
tong = 0

for index, value in enumerate(a):
    if index % 2 == 0:
        # Index chẵn (0, 2, ... tương ứng vị trí 1, 3, ...): mang dấu trừ
        tong -= value
    else:
        # Index lẻ (1, 3, ... tương ứng vị trí 2, 4, ...): mang dấu cộng
        tong += value
print(f"Output: {tong}") # Ket qua se in ra -8 (= -5 +3 -8 +2)
        


# --- Bài 3 — Lọc chia hết cho 2 HOẶC 3, nhưng KHÔNG chia hết cho 6 ---
# Đề bài: Trả về dãy con gồm các phần tử chia hết cho 2 hoặc 3,
# nhưng KHÔNG được chia hết cho 6.
#
# Input:  a = [2, 3, 6, 9, 10, 12, 15]
# Output: [2, 3, 9, 10, 15]   (6 và 12 bị loại vì chia hết cho 6)

a = [2, 3, 6, 9, 10, 12, 15]
ket_qua = []

for num in a:
    
    if (num % 2 == 0 or num % 3 == 0) and num % 6 != 0:
        ket_qua.append(num)
print(f"Output: {ket_qua}")


# --- Bài 4 — Lọc chia hết cho 5 nhưng KHÔNG chia hết cho 2 và KHÔNG chia hết cho 3 ---
# Đề bài: Trả về dãy con các phần tử chia hết cho 5, nhưng không
# chia hết cho 2 VÀ không chia hết cho 3.
#
# Input:  a = [5, 10, 15, 20, 25, 30, 35]
# Output: [5, 25, 35]   (10 loại vì chia hết 2, 15&30 loại vì chia hết 3, 20 loại vì chia hết 2)

a = [5, 10, 15, 20, 25, 30, 35]
ket_qua =[]# Giỏ ban đầu trống rỗng

for num in a:
    if num % 5 == 0 and num % 2 != 0 and num % 3 != 0:
        ket_qua.append(num) #Thỏa mãn thì bỏ vào giỏ ket_qua
print(f"Output {ket_qua}")


# --- Bài 5 — Dãy số trong khoảng, chia hết dư r ---
# Đề bài: Cho 3 số nguyên n, m, r (n < m). Trả về dãy tất cả các số
# nguyên trong khoảng từ n đến m (bao gồm cả 2 đầu) mà khi chia cho
# 4 thì dư đúng r.
#
# Input:  n=10, m=30, r=2
# Output: [10, 14, 18, 22, 26, 30]   (mỗi số % 4 đều bằng 2)

n, m, r = 10, 30, 2
ket_qua = []

# Duyệt qua các số từ n đến m (bao gồm m nên phải dùng m + 1)
for num in range(n, m + 1):
    # Kiểm tra nếu chia cho 4 dư r
    if num % 4 == r:
        ket_qua.append(num)
print(f"Output: {ket_qua}")


# --- Bài 6 — Tổng theo nhóm xen kẽ 2 phần tử ---
# Đề bài: Cho dãy số a (số lượng phần tử luôn là số chẵn). Tính:
# (a1+a2) - (a3+a4) + (a5+a6) - (a7+a8) + ...
# (nhóm 2 phần tử một, xen kẽ dấu theo TỪNG NHÓM chứ không phải từng
# phần tử)
#
# Input:  a = [1, 2, 3, 4, 5, 6, 7, 8]
# Tính:   (1+2) - (3+4) + (5+6) - (7+8) = 3 - 7 + 11 - 15 = -8
# Output: -8

a = [1, 2, 3, 4, 5, 6, 7, 8]
tong = 0
# Duyệt qua danh sách với bước nhảy là 2 (để lấy từng cặp index: 0, 2, 4, 6)
for i in range(0, len(a), 2):

   # Tính tổng của cặp 2 phần tử hiện tại
   nhom = a[i] + a[i + 1]
   
   # Xác định vị trí của nhóm (nhóm thứ 0, 1, 2, 3...)
   # Ta dùng i // 2 để ra số thứ tự nhóm: 0, 1, 2, 3...
   thu_tu_nhom = i // 2
   if thu_tu_nhom % 2 == 0:
        # Nhóm chẵn (nhóm 0, 2... tương ứng nhóm 1, 3 trong đề): mang dấu cộng
        tong += nhom
   else:
        # Nhóm lẻ (nhóm 1, 3... tương ứng nhóm 2, 4 trong đề): mang dấu trừ
        tong -= nhom
print(f"Output: {tong}")


# --- Bài 7 — Đếm phần tử thỏa 2 điều kiện: vị trí VÀ giá trị ---
# Đề bài: Cho dãy số a. Đếm xem có bao nhiêu phần tử VỪA nằm ở VỊ TRÍ
# CHẴN (a2, a4, a6...) VỪA có giá trị chia hết cho 3.
#
# Input:  a = [9, 6, 4, 12, 7, 18]   (a1=9,a2=6,a3=4,a4=12,a5=7,a6=18)
# Vị trí chẵn: a2=6, a4=12, a6=18 — cả 3 đều chia hết cho 3
# Output: 3

a = [9, 6, 4, 12, 7, 18]
dem = 0

for index, value in enumerate(a):
    if index % 2 != 0 and value % 3 == 0:
        dem += 1
print(f"Output: {dem}")
