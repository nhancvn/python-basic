# bài 1:
# Đếm xem có bao nhiêu số dương
def count_positive(numbers):
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count

positive_numbers = [24, 10, 11, 40, 29, 23]
print(count_positive(positive_numbers))


# bài 2:
# Đếm xem có bao nhiêu số âm
def count_negative(numbers):
    count = 0
    for number in numbers:
        if number < 0:
            count += 1
    return count

sample_numbers = [11, -12, -10, -24, -29, -40, 26]
print(count_negative(sample_numbers))


# bài 3:
# Tính tổng các số dương
def sum_positive(numbers):
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total

print(sum_positive(sample_numbers))


# bài 4:
# Tính tổng các số âm
def sum_negative(numbers):
    total = 0
    for number in numbers:
        if number < 0:
            total += number
    return total

print(sum_negative(sample_numbers))


# bài 5:
# Tìm vị trí của số lớn nhất
def get_index_max(numbers):
    max_index = 0
    for index in range(1, len(numbers)):
        if numbers[index] > numbers[max_index]:
            max_index = index
    return max_index

print(get_index_max(sample_numbers))


# bài 6:
# Tìm vị trí của số nhỏ nhất
def get_index_min(numbers):
    min_index = 0
    for index in range(1, len(numbers)):
        if numbers[index] < numbers[min_index]:
            min_index = index
    return min_index

print(get_index_min(sample_numbers))


# bài 7:
# Đổi chỗ số lớn nhất và số nhỏ nhất
def swap_max_min(numbers):
    if not numbers:
        return numbers

    max_index = get_index_max(numbers)
    min_index = get_index_min(numbers)

    numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]
    return numbers

print(swap_max_min(sample_numbers.copy()))


# bài 8:
# Xóa phần tử tại một vị trí
def remove_at_position(numbers, position):
    if position < 0 or position >= len(numbers):
        return numbers

    numbers.pop(position)
    return numbers

print(remove_at_position(sample_numbers.copy(), 1))


# bài 9:
# Kiểm tra xem list có đối xứng hay không
def is_palindrome(numbers):
    length = len(numbers)

    for index in range(length // 2):
        if numbers[index] != numbers[length - 1 - index]:
            return False

    return True

print(is_palindrome([1, 2, 3, 2, 1]))


# bài 10:
# Dịch trái list một lần
def rotate_left(numbers):
    if not numbers:
        return numbers

    first_value = numbers[0]
    numbers = numbers[1:]
    numbers.append(first_value)

    return numbers

print(rotate_left([1, 2, 4, 5, 9]))


# bài 11:
# Kiểm tra tất cả các phần tử có phải số dương hay không
def all_positive(numbers):
    if not numbers:
        return True

    for number in numbers:
        if number <= 0:
            return False

    return True

print(all_positive(sample_numbers))


# bài 12:
# Tìm hiệu giữa số lớn nhất và số nhỏ nhất
def max_min_difference(numbers):
    if not numbers:
        return 0

    max_index = get_index_max(numbers)
    min_index = get_index_min(numbers)

    return numbers[max_index] - numbers[min_index]

print(max_min_difference(sample_numbers))