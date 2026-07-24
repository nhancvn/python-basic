#bài 1:
#Đếm xem có bao nhiêu số dương
def num1 (numbers):
    count = 0
    for n in numbers:
        if n > 0:
            count += 1
    return count
numbers = [24, 10, 11, 40, 29, 23]
print(num1(numbers))


#bài 2:
#Đếm xem có bao nhiêu số âm
def num2 (numbers):
    count = 0
    for n in numbers:
        if n < 0:
            count += 1
    return count
numbers = [11, -12, -10, -24, -29, -40, 26]
print(num2(numbers))

#bài 3:
#Tính tổng các số dương 
def num3 (numbers):
    total = 0
    for n in numbers:
        if n > 0:
            total += n
    return total
numbers = [11, -12, -10, -24, -29, -40, 26]
print(num3(numbers))

#bài 4:
#Tính tổng các số âm
def num4 (numbers):
    total = 0
    for n in numbers:
        if n < 0:
            total += n
    return total 
numbers = [11, -12, -10, -24, -29, -40, 26]
print(num4(numbers))

#bài 5:
#Tìm vị trí của số lớn nhất
def num5 (numbers):
    A = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[A]:
            A = i
    return A
numbers = [11, -12, -10, -24, -29, -40, 26]
print(num5(numbers))

#bài 6:
#Tìm vị trí của số nhỏ nhất
def num6 (numbers):
    M = 0
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[M]:
            M = i
    return M
numbers = [11, -12, -10, -24, -29, -40, 26]
print(num6(numbers))

#bài 7:
#Đổi chỗ số lớn nhất và số nhỏ nhất
def num7 (numbers):
    if not numbers:
        return numbers
    A = num5(numbers)
    M = num6(numbers)
    numbers[A], numbers[M] = numbers[M], numbers[A]
    return numbers
numbers = [11, -12, -10, -24, -29, -40, 26]
print(num7(numbers))

#bài 8:
#Xóa phần tử tại một vị trí
def num8 (numbers, position):
    if position < 0 or position >= len(numbers):
        return numbers
    numbers.pop(position)
    return numbers
numbers = [11, -12, -10, -24, -29, -40, 26]
print(num8(numbers, 1))

#bài 9:
#Kiểm tra xem list có đối xứng hay ko ?
def num9 (numbers):
    n = len(numbers) 
    for i in range(n // 2):
        if numbers[i] != numbers[n - 1 - i]:
            return False
    return True
print(num9([1,2,4,5,9]))

#bài 10:
#Dịch trái list một lần
def num10 (numbers):
    if not numbers:
        return numbers
    first = numbers[0]
    numbers = numbers[1:]
    numbers.append(first)
    return numbers
print(num10([1,2,4,5,9]))


