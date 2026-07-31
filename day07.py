# Bai 1: Array + Hash Map + String
# Cho một mảng số nguyên nums.
# Trả về True nếu có ít nhất một phần tử xuất hiện từ 2 lần trở lên, ngược lại trả về False.
def containDuplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
print(containDuplicate([1,2,3,1]))     
print(containDuplicate([1,2,3,4]))    
print(containDuplicate([]))          
print(containDuplicate([1]))          
print(containDuplicate([5,5]))


# bai 2: Valid Anagram
# Cho hai chuỗi s và t.
# Kiểm tra xem t có phải là anagram của s hay không.
from collections import Counter
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)
print(isAnagram("listen", "silent"))


# bai 3: Move Zeroes
# Cho một mảng số nguyên.
# Di chuyển tất cả số 0 xuống cuối mảng.
# # Giữ nguyên thứ tự của các số khác 0.
def moveZeroes(nums: list[int]) -> None:
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    for i in range(insert_pos, len(nums)):
        nums[i] = 0
nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums) 


# bai 4: Best Time to Buy and Sell Stock
# Cho mảng prices.
# Chỉ được mua 1 lần và bán 1 lần.
# Tìm lợi nhuận lớn nhất.
def max_Profit(prices: list[int]) -> int:
    min_price = float('inf')
    max_Profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_Profit:
            max_Profit = price - min_price
    return max_Profit
prices = [7,1,5,3,6,4]
print(max_Profit(prices))


# bai 5: Longest Consecutive Sequence
# Cho một mảng số nguyên chưa sắp xếp.
# Tìm độ dài dãy số liên tiếp dài nhất.
def LongestConsecutive(nums: list[int]) -> int:
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1
            while (current_num + 1) in num_set:
                current_num += 1
                current_streak +=1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak
print(LongestConsecutive([100,4,200,1,3,2]))
print(LongestConsecutive([0,3,7,2,5,8,4,6,0,1]))

