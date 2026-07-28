#Bài 1: FizzBuzz 
#In ra các số từ 1 đến 100. Số chia hết cho 3 → in "Fizz". 
# Chia hết cho 5 → in "Buzz". Chia hết cho cả 3 và 5 → in "FizzBuzz". 
# Còn lại → in chính số đó.
def fizz_buzz():
    for i in range(1, 101):
        if  i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizz_buzz()


#Bài 2: Kiểm tra số nguyên tố (Prime Check) 
#Viết hàm nhận vào 1 số nguyên, trả về True nếu là số nguyên tố, False nếu không.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int (n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))
print(is_prime(8))  
print(is_prime(1))


# Bài 3: Dãy Fibonacci
# In ra n số đầu tiên của dãy Fibonacci 
# (mỗi số = tổng 2 số liền trước, bắt đầu từ 0, 1).
def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib_list = [0, 1]
    for i in range(2, n):
        next_value = fib_list[-1] + fib_list[-2]
        fib_list.append(next_value)
    return fib_list
print(generate_fibonacci(10))


# Bài 4: Đảo ngược chuỗi thủ công
# Đảo ngược 1 chuỗi mà KHÔNG dùng [::-1] hoặc reversed().
def reverse_string(text):
    reverse_text = ""
    for char in text:
        reverse_text = char + reverse_text
    return reverse_text
print(reverse_string("Hello"))


# Bài 5:Tìm UCLN của 2 số (GCD - Euclid)
# Tìm ước chung lớn nhất của 2 số nguyên dương, dùng thuật toán Euclid.
def find_gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
print(find_gcd(10, 11))


#Bài 6: Two Sum — Tìm cặp số có tổng bằng giá trị cho trước
# Cho 1 list số và 1 giá trị target. 
# Tìm 2 phần tử trong list có tổng bằng target, trả về chỉ số (index) của 2 phần tử đó.
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None
print(two_sum([2, 7, 11, 15], 9))