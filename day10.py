# bài 1:
# Chương trình kiểm tra số nguyên dương hay âm
def check_numbers(n):
    if n > 0:
        return "Số Dương"
    elif n < 0:
        return "Số Âm"
    else:
        return "Số 0"
# Nhập số nguyên từ người dùng
try:
    number = int(input("Nhập một số nguyên: "))
    result = check_numbers(number)
    print(result)
except ValueError:
    print("Vui lòng điền số nguyên hợp lệ.")


# bài 2'
# Bài tập yêu cầu bạn viết một chương trình để kiểm tra xem một số nguyên mà người dùng nhập vào là số chẵn hay số lẻ.
def chec_numbers(n):
    if n % 2 == 0:
        return "Số Dương"
    else:
        return "Số Âm"
try:
    number = int(input("Nhập Số: "))
    result = chec_numbers(number)
    print(result)
except ValueError:
    print("Vui lòng điền số nguyên hợp lệ.")


# bài 3:
# Bài tập yêu cầu bạn viết một chương trình để tìm số lớn nhất trong ba số nguyên mà người dùng nhập vào.
def find_max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
try:
    num1 = int(input("Số thứ nhất: " ))
    num2 = int(input("Số thứ hai: "))
    num3 = int(input("Số thứ ba: "))

    max_number = find_max_of_three(num1, num2, num3)
    print(f"Số lớn nhất trong ba số: {max_number}")
except ValueError:
    print("Vui lòng điền số nguyên hợp lệ.")


# bài 4:
# Bài tập yêu cầu bạn viết một chương trình để tính tiền taxi dựa trên số km mà người dùng đã đi.
# Giá cước taxi có thể được tính theo các mức giá khác nhau dựa trên số km đã đi.
def calculate_taxi_fare(km):
    if km < 1:
        fare = 10000
    elif km <= 10:
        fare = 10000 + (km - 1) * 8500
    else:
        fare = 10000 + 9 * 8500 + (km -10) * 7500
    return fare
try:
    distance = float(input("Số km đã đi: "))
    if distance < 0:
        print("So km ko hop le. Vui long nhap so duong")
    else:
        total_fare = calculate_taxi_fare(distance)
        print(f"Tong so tien taxi la: {total_fare} VND")
except ValueError:
    print("Vui lòng điền số nguyên hợp lệ.")
    


# bài 5:
# Bài tập yêu cầu bạn viết một chương trình để tính điểm trung bình của học sinh dựa trên các điểm số của các môn học và xếp loại học sinh dựa trên điểm trung bình.
# Giả định về điểm số và xếp loại (có thể thay đổi theo yêu cầu cụ thể):
# Điểm trung bình >= 8.5: Xuất sắc
# Điểm trung bình >= 7.0 và < 8.5: Giỏi
# Điểm trung bình >= 5.5 và < 7.0: Khá
# Điểm trung bình >= 4.0 và < 5.5: Trung bình
# Điểm trung bình < 4.0: Yếu
# Hàm tính toán
def calculate_average(scores):
    return sum(scores) / len(scores)

# Hàm phân loại
def classify_student(average):
    if average >= 8.5:
        return "Xuất Sắc"
    elif average >= 7.0:
        return "Giỏi"
    elif average >= 5.5:
        return "Khá"
    elif average >= 4.0:
        return "Trung Bình"
    else:
        return "Yếu"
# Nhập điểm số từ người dùng
try:
    scores = []
    num_subjects = int(input("Nhập số lượng môn học:"))
    if num_subjects <= 0:
        print("Số lượng môn học phải lớn hơn 0.")
    else:
        for i in range(num_subjects):
            score = float(input(f"Nhập điểm môn học thứ {i + 1}: "))
            if score < 0 or score > 10:
                print("Điểm số phải từ 0 đến 10. Vui lòng nhập lại.")
                break
            scores.append(score)

        if len(scores) == num_subjects:
            average_score = calculate_average(scores)
            classify_student = classify_student(average_score)
            print(f"Điểm trung bình: {average_score:.2f}")
            print(f"Xếp loại: {classify_student}")
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")

