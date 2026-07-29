# bai 1:
# Xóa phần tử trùng nhưng vẫn giữ đúng 2 lần xuất hiện
def limit_two_duplicates(numbers):
    result = []
    seen_count = {}
    for number in numbers:
        seen_count[number] = seen_count.get(number, 0) + 1
        if seen_count[number] <= 2:
            result.append(number)
    return result
print(limit_two_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 4]))
print(limit_two_duplicates([5, 5, 5]))

# bai 2:
# Gom tất cả số âm sang trái, số dương sang phải
def pratition_negatives_positives(numbers):
    negative_numbers = []
    positive_numbers = []
    zero_numbers = []
    for number in numbers:
        if number < 0:
            negative_numbers.append(number)
        elif number > 0:
            positive_numbers.append(number)
        else:
            zero_numbers.append(number)
    return negative_numbers + positive_numbers + zero_numbers
print(pratition_negatives_positives([3, -1, -7, 2, -4, 0]))


# bai 3:
# Tìm đoạn con có tổng lớn nhất
def find_max_subarray(numbers):
    if not numbers:
        return 0
    current_sum = numbers[0]
    max_sum = numbers[0]
    for number in numbers[1:]:
        current_sum = max(number, current_sum + number)
        max_sum = max(max_sum, current_sum)
    return max_sum
print(find_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# bai 4:
# Xoay mảng (xoay list k lần)
def rotate_array(numbers, k):
    if not numbers:
        return numbers
    length = len(numbers)
    k = k % length
    if k == 0:
        return numbers[:]
    return numbers[-k:] + numbers[:-k]
print(rotate_array([1, 2, 3, 4, 5], 2))
print(rotate_array([1, 2, 3, 4, 5], 7))


# bai 5:
# Kiểm tra chuỗi ngoặc hợp lệ
def validate_parentheses(text):
    matching_pairs = {')': '(', ']': '[', '}': '{' }
    opening_brackets = set(matching_pairs.values())
    stack = []
    for character in text:
        if character in opening_brackets:
            stack.append(character)
        elif character in matching_pairs:
            if not stack or stack[-1] != matching_pairs[character]:
                return False
            stack.pop()
    return len(stack) == 0
print(validate_parentheses("(()())"))   
print(validate_parentheses("(()("))     
print(validate_parentheses("())("))     
print(validate_parentheses("()[]{}"))   
print(validate_parentheses("([)]"))     


# bai 6:
# Hợp nhất các mảng đã sắp xếp (không dùng sắp xếp())
def merge_sorted_lists(list_a, list_b):
    result = []
    left = 0
    right = 0
    while left < len(list_a) and right < len(list_b):
        if list_a[left] <= list_b[right]:
            result.append(list_a[left])
            left += 1
        else:
            result.append(list_b[right])
            right += 1
    while left < len(list_a):
        result.append(list_a[left])
        left += 1
    while right < len(list_b):
        result.append(list_b[right])
        right += 1
    return result
print(merge_sorted_lists([1, 3, 5, 7], [2, 4, 6]))  
print(merge_sorted_lists([], [1, 2]))                 
print(merge_sorted_lists([1], []))