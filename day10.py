#bài 1:
#Kiểm tra số chính phương: Viết hàm kiểm tra một số nguyên có phải là số chính phương (perfect square) hay không (VD: 16 = 4², 25 = 5²).
def is_perfect_square(n):
    if n < 0:
        return False
    num = int(n ** 0.5) # lấy phần nguyên của căn bậc 2
    return num * num == n # bp lại , ss vs n ban đầu 

print(is_perfect_square(16))
print(is_perfect_square(25))
print(is_perfect_square(15))


#bài 2:
#Phân loại tam giác: Nhập 3 cạnh a, b, c → kiểm tra có tạo thành tam giác hợp lệ không, nếu có thì phân loại: đều / cân / vuông / thường.
def classify(a, b, c):
    if not (a + b > c and b + c > a and a + c > b):
        return "ko phai tam giac hop le"

    if a == b == c:
        return "Tam giac deu"

    x, y, z = sorted([a, b, c])  # sap xep tang dan, z luon la canh lon nhat
    is_vuong = x ** 2 + y ** 2 + z ** 2
    is_can = a == b or b == c or a == c

    if is_vuong and is_can:
        return "Tam giac vuong can"
    if is_vuong:
        return "Tam giac vuong"
    if is_can:
        return "Tam giac can"
    return "Tam giac thu"


        
print(classify(3, 3, 3))   
print(classify(3, 3, 5))   
print(classify(3, 4, 5))   
    

#bài 3:
#Tính tiền điện: Tính hóa đơn tiền điện theo bậc thang (VD: 50 số đầu giá X, 50 số tiếp giá Y cao hơn, trên 100 số giá Z), tương tự cấu trúc bài taxi.
def electricity_bill(kwh):
    if kwh <= 50:
        total = kwh * 50
    elif kwh <= 100:
        total = 50 * 50 + (kwh - 50) * 100
    elif kwh <= 200:
        total = 50 * 50 + 50 * 100 + (kwh - 100) * 150
    else:
         total = 50 * 50 + 50 * 100 + 100 * 150 + (kwh - 200) * 200
    return total

try:
    kwh_used = float(input("So kwh da dung: "))
    if kwh_used < 0:
        print("So kwh ko hop le. Vui long nhap lai")
    else:
        total = electricity_bill(kwh_used)
        print(f"Tong so kwh la: {total} VND")
except ValueError:
    print("Vui lòng điền số nguyên hợp lệ.")


#bài 4:
#Đếm chữ số & tổng chữ số: Nhập 1 số nguyên dương, đếm xem có bao nhiêu chữ số và tính tổng các chữ số đó (không dùng str(), chỉ dùng % và //).
def count_and_sum_digits(n):
    if n == 0:
        return 1, 0
    count = 0
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        count += 1
        n = n // 10
    return count, total
print(count_and_sum_digits(1234))  
print(count_and_sum_digits(7))     
print(count_and_sum_digits(999))   
print(count_and_sum_digits(100))   
print(count_and_sum_digits(0))     


#bài 5:
#In hình tam giác sao: In ra hình tam giác vuông bằng dấu *, số dòng do người dùng nhập (dùng vòng for lồng nhau như bảng cửu chương).
def print_triangle(n):
    for i in range(1, n + 1):
        for j in  range(i):
            print('*', end = '')
        print()
print_triangle(5)


#bài 6:
#Đảo ngược số nguyên: Nhập 1 số, in ra số đó viết ngược (VD: 1234 → 4321), dùng vòng while.
def dao_nguoc(n):
    if n == 0:
        return 0
    
    dao_nguoc = 0
    while n > 0:
        digit = n % 10
        dao_nguoc = dao_nguoc * 10 + digit
        n =  n // 10
    return dao_nguoc

print(dao_nguoc(1234))  
print(dao_nguoc(1200))  
print(dao_nguoc(7))     
print(dao_nguoc(0))     
print(dao_nguoc(1000))  


#bài 7:
#Kiểm tra số Armstrong: Số Armstrong là số bằng tổng lập phương (hoặc lũy thừa n) các chữ số của nó (VD: 153 = 1³+5³+3³). Kiểm tra 1 số có phải Armstrong không.
def is_armstrong(n):
    original = n

    temp = n
    num_digits = 0
    while temp > 0:
        num_digits += 1
        temp = temp // 10

    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total = total + digit ** num_digits
        temp = temp // 10

    return total == original
print(is_armstrong(153)) 
print(is_armstrong(123))


#bài 8:
#Tìm số nhỏ nhất & lớn nhất trong list: Nhập một danh sách số nguyên (giống bài 8), tự viết hàm tìm min và max không dùng min()/max().
def find_min_max(numbers):
    lon_nhat = numbers[0]
    nho_nhat = numbers[0]
    for number in numbers:
        if number > lon_nhat:
            lon_nhat = number
        if numbers < nho_nhat:
            nho_nhat = number
        return lon_nhat, nho_nhat
print(find_min_max([3, 7, 1, 9, 4])) 
print(find_min_max([5]))



#bài 9:
#Bội chung nhỏ nhất (BCNN/LCM): Viết hàm tính BCNN của 2 số, có thể tận dụng lại hàm gcd() đã viết ở bài 10 (gợi ý: LCM = a*b / GCD(a,b)).
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
print(lcm(4, 6))
print(lcm(21, 6))



#bài 10:
#Đếm nguyên âm & phụ âm trong chuỗi: Nhập 1 chuỗi (câu tiếng Việt không dấu hoặc tiếng Anh), 
#đếm số nguyên âm (a, e, i, o, u) và số ký tự còn lại là chữ cái.
def count_vowel_consonants(text):
    count_vowel = 0
    count_consonants = 0
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in "aeiou":
                count_vowel += 1
            else:
                count_consonants += 1
    return count_vowel, count_consonants
print(count_vowel_consonants("Hello World"))