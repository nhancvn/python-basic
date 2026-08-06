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
        return "Số Chẵn"
    else:
        return "Số Lẻ"s
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


# bài 6: Bài tập yêu cầu bạn viết một chương trình để trong bảng cửu chương từ 1 đến 10. 
# Bảng cửu chương là bảng nhân, nơi mỗi số từ 1 đến 10 được nhân với số từ 1 đến 10.
# Đầu vào: No user input.
# Đầu ra: In ra bảng cửu chương từ 1 đến 10.
def multiplication_table():
    for i in range(1, 11):
        print(f"Bảng cửu chương: {i}")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print() # In dong trong de ngan cach
# Gọi hàm để in bảng cửu chương
multiplication_table()


# bài 7: Bài tập yêu cầu bạn viết một chương trình để kiểm tra 
# xem một năm có phải là tiền nhuận bút hay không.
# Một năm là một khoản tiền mặc dù:
# Năm đó chia hết cho 4 và không chia hết cho 100, hoặc
# Năm đó chia hết cho 400.
# Đầu vào : Một name(một số nguyên)
# Đầu ra : thông báo cho mọi người biết năm đó có phải năm nhuận hay ko .
def is_leep_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
try:
    year = int(input("Nhập một năm"))
    if is_leep_year(year):
        print(f"Nam {year} la Nam Nhuan.")
    else:
        print(f"Nam {year} Khong Phai Nam Nhuan.")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")


# bài 8: Bài tập yêu cầu bạn viết một chương trình để đếm số chẵn và số lẻ trong một danh sách các số nguyên.
# Đầu vào: Một danh sách các số nguyên.
#Đầu ra:
#Số lượng số bảo vệ.
#Số lượng số hoàn chỉnh.
def count_even_odd(numbers):
    count_even = 0
    count_odd = 0
    for number in numbers:
        if number % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd
try:
    input_list = ("Nhâp các số nguyên, cách nhau bằng dấu cách: ")
    numbers = [int(num) for num in input_list.split()]

    even_count, odd_count = count_even_odd(numbers)
    print(f"Số lượng số chẵn: {even_count} ")
    print(f"Số lượng số lẻ: {odd_count}")
except ValueError:
    print("Vui lòng nhập các số nguyên hợp lệ.")


# bài 9: Bài tập yêu cầu bạn viết một chương trình để chứa tất cả các số nguyên tố từ 1 đến 100.
# Đầu vào:
# No user input.
# Đầu ra:
# In out all các số nguyên tố từ 1 đến 100.
# Chương trình in tất cả các số nguyên tố từ 1 đến 100
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True

def primes_up_to_100():
    for number in range(1, 101):
        if is_prime(number):
            print(number, end = ' ')
    print()
# Gọi hàm để in các số nguyên tố từ 1 đến 100
primes_up_to_100()


# bài 10:
# Bài tập yêu cầu bạn viết một chương trình để tìm số chung lớn nhất (USCLN) của hai số nguyên.
# Ước tính số chung lớn nhất (USCLN) của hai số nguyên a và b là số lớn nhất chia trong cả hai số a và b.
# Để tìm USCLN, chúng ta có thể sử dụng thuật toán Euclid, một phương pháp hiệu quả và dễ
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
try:
    num1 = int(input("Nhập số thứ nhất: "))
    num2 = int(input("Nhấp số thứ hai:"))

    uscln = gcd(num1, num2)
    print(f"Ước số chung lớn nhất {num1} và {num2} là: {uscln}")
except ValueError:
    print("Vui lòng nhập các số nguyên hợp lệ.")