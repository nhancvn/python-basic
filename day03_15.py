#bài 1:
#tìm số lớn nhất
def find_max(numbers):
   max_num = numbers[0]
   for num in numbers:
     if num > max_num:
        max_num = num
   return max_num
numbers = [24, 10, 11, 40, 29, 23]
print(find_max(numbers))


#bai 2:
#tìm số nhỏ nhất 
def find_min(numbers):
   min_num = numbers[0]
   for num in numbers:
      if num < min_num:
         min_num = num
   return min_num
numbers = [24, 10, 11, 40, 29, 23]
print(find_min(numbers))


#bài 3:
#tính tổng tất cả các phần tử
def sum_elements(numbers):
   total = 0
   for num in numbers:
      total += num
   return total
numbers = [24, 10, 11, 40, 29, 23]
print(sum_elements(numbers))

#bài 4:
#đếm có bao nhiêu số chẵn
def num1(numbers):
   count = 0
   for num in numbers:
       if num % 2 == 0:
         count += 1
   return count
numbers = [24, 10, 11, 40, 29, 23]
print(num1(numbers))

#bài 5:
#tính tổng các số chẵn 
def num2(numbers):
   total = 0
   for num in numbers:
      if num % 2 == 0:
         total += num
   return total
numbers = [24, 10, 11, 40, 29, 23]
print(num2(numbers))

#bài 6:
#đếm số lượng số lẻ
def num3(numbers):
   count = 0
   for num in numbers:
       if num % 2 != 0:
         count += 1
   return count
numbers = [24, 10, 11, 40, 29, 23]
print(num3(numbers))

#bài 7:
#tính sô lớn thứ hai
def num4(numbers):
   if len(numbers) < 2:
      return None
   first = float("-inf")
   second = float("-inf")
   for num in numbers:
      if num > first:
         second = first
         first = num 
      elif first > num > second:
         second = num
   return second
numbers = [24, 10, 11, 40, 29, 23]
print(num4(numbers))


#bài 8:
#kiểm tra list có đc sắp xếp tăng dần hay ko ?
def num5(numbers):
   for i in range(len(numbers)):
      if numbers[i] > numbers[i + 1]:
         return False
   return True
numbers = [24, 10, 11, 40, 29, 23]
print(num5(numbers))

#bài 9:
#trả x về vị trí đầu tiên nếu ko có thì trả về -1
def num6 (numbers, x):
   for i in range(len(numbers)):
      if numbers[i] == x:
         return i
   return -1
numbers = [24, 10, 11, 40, 29, 23]
print(num6(numbers, 11))
   

#bài 10:
#đảo ngược list bằng thuật toán ko dùng reverse()
def num7 (numbers):
    left = 0
    right = len(numbers) - 1
    while left < right:
       temp = numbers[left]
       numbers[left] = numbers[right]
       numbers[right] = temp
       left += 1
       right -= 1
    return numbers
numbers = [24, 10, 11, 40, 29, 23]
print(num7(numbers))

#bài 11:
#loại bỏ tất cả các phần tử trùng nhau và giữ nguyên thứ tự xuất hiện
def num8 (numbers):
   result = []
   for num in numbers:
      if num not in result:
         result.append(num)
   return result
numbers = [24, 10, 11, 40, 29, 23, 40, 29, 10, 14]
print(num8(numbers))


#bài 12:
#Sắp xếp tăng dần bằng thuật toán Selection Sort.
def num9 (numbers):
   n = len(numbers)
   for i in range(n):
      z = i
      for j in range(i + 1, n):
         if numbers[j] < numbers[z]:
            z = j
      temp = numbers[i]
      numbers[i] = numbers[z]
      numbers[z] = temp
   return numbers
numbers = [24, 10, 11, 40, 29, 23, 40, 29, 10, 14]
print(num9(numbers))

#bài 13:
#sắp xếp giảm dần bằng thuật toán Bubble Sort
def num10 (numbers):
   n = len(numbers)
   for i in range(n):
      for j in range(0, n - i - 1):
         if numbers[j] < numbers[j + 1]:
             temp = numbers[i]
             numbers[j] = numbers[j + 1]
             numbers[j + 1] = temp
   return numbers
numbers = [24, 10, 11, 40, 29, 23, 40, 29, 10, 14]
print(num10(numbers))


#bài 14:
#Di chuyển tất cả số chẵn lên đầu và giữ nguyên thứ tự các số chẵn và số lẻ
def num11 (numbers):
   E = []
   O = []
   for num in numbers:
      if num % 2 == 0:
         E.append(num)
      else:
         O.append(num)
   return E + O
numbers = [24, 10, 11, 40, 29, 23, 40, 29, 10, 14]
print(num11(numbers))


#bài 15:
#tìm cặp 2 số có tổng bằng x
def num12 (numbers, x):
   for i in range(len(numbers)):
      for j in range(i + 1, len(numbers)):
         if numbers[i] + numbers[j] == x:
            return (numbers[i], numbers[j])
   return None
numbers = [24, 10, 11, 40, 29, 23, 40, 29, 10, 14]
print(num12(numbers, 34))