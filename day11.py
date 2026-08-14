# Bài 1: Tính tổng theo quy luật
# Cho dãy số nguyên `a` gồm `n` phần tử:
# a = [a₁, a₂, ..., aₙ]
# Tính giá trị:
# a₁ + a₂ - a₃ + a₄ + a₅ - a₆ + ...
# Tức là **cứ mỗi phần tử thứ 3 thì lấy dấu âm**.
# Ví dụ:
# ```text
# a = [1, 2, 3, 4, 5, 6]
# Kết quả:
# 1 + 2 - 3 + 4 + 5 - 6 = 3

def total_number(a):
    total = 0
    for i, x in enumerate(a): # i = vi tri (bat dau tu 0), x = gia tri phan tu
        # (i+1): quy doi ve vi tri dem tu 1 nhu de bai; chia het cho 3 -> la vi tri can lay dau am
        if (i + 1) % 3 == 0:
            total = total - x
        else:
            total = total + x
    return total
print(total_number([1, 2, 3, 4, 5, 6]))



# Bài 2: Tính giá trị biểu thức
# Cho dãy số nguyên `a` gồm `n` phần tử và một số thực `x`:
# a = [a₁, a₂, ..., aₙ]
# Tính giá trị:
# a₁ + a₂x + a₃x² + a₄x³ + ... + aₙxⁿ⁻¹
# Ví dụ:
# ```text
# a = [1, 2, 3]
# x = 2
# Kết quả:
# 1 + 2 × 2 + 3 × 2² = 17

def Calculate_value(a, x):
    total = 0
    for i, a_i in enumerate(a):
          total = total + a_i * (x ** i)
    return total
a = [1, 2, 3]
x = 2
print(Calculate_value(a, x))

# Bài 3: Đếm phần tử lớn hơn giá trị trung bình
# Cho dãy số nguyên `a`.
# Tính giá trị trung bình của tất cả các phần tử trong dãy.
# Sau đó, đếm số lượng phần tử **lớn hơn giá trị trung bình**.
# Ví dụ:
# ```text
# a = [1, 2, 3, 4, 5]
# Giá trị trung bình = 3
# Có 2 phần tử lớn hơn giá trị trung bình: 4 và 5.
# Kết quả: 2
def count_above_average(a):
    average = sum(a) / len(a)
    
    count = 0
    for number in a:
        if number > average:
            count += 1
    return count
print(count_above_average([1, 2, 3, 4, 5]))


# Bài 4: Kiểm tra phần tử trùng nhau
# Cho dãy số nguyên `a`.
# Kiểm tra xem trong dãy có ít nhất hai phần tử có cùng giá trị hay không.
# * Trả về `True` nếu có phần tử trùng nhau.
# * Trả về `False` nếu tất cả các phần tử đều khác nhau.
# # Ví dụ:
# # ```text
# [1, 2, 3, 4] → False
# [1, 2, 3, 2] → True
def has_duplicates(a):
    s = set(a)
    return len(a) != len(s)
print(has_duplicates([1, 2, 3, 4]))
print(has_duplicates([1, 2, 3, 2]))




# Bài 5: Đếm số lần xuất hiện
# Cho dãy số nguyên `a`.
# Tạo một `dictionary` lưu số lần xuất hiện của mỗi giá trị trong dãy.
# Ví dụ:
# ```text
# a = [2, 3, 2, 5, 3, 2]
# ```
# Kết quả:
# ```python
# {
#     2: 3,
#     3: 2,
#     5: 1
# }
# ```
# Trong đó:
# * `2` xuất hiện 3 lần.
# * `3` xuất hiện 2 lần.
# * `5` xuất hiện 1 lần.
# ---
def count_occurrences(a):
    counts = {}
    for i in a:
        counts[i] = counts.get(i, 0) + 1
    return counts
a = [2, 3, 2, 5, 3, 2]
print(count_occurrences(a))



# # Bài 6: Thống kê điểm học sinh
# Cho một `dictionary` chứa tên và điểm của các học sinh:
# ```python
# {
#     "An": 8.5,
#     "Bình": 7.0,
#     "Chi": 9.0,
#     ...
# }
# ```
# ### A.
# Tính **điểm trung bình** của tất cả học sinh.
# ### B.
# Tính **điểm trung vị (median)** của tất cả học sinh.
# Quy tắc tính median:
# * Nếu có số lượng điểm lẻ, median là giá trị nằm ở chính giữa sau khi sắp xếp.
# * Nếu có số lượng điểm chẵn, median là trung bình cộng của hai giá trị nằm ở chính giữa.
# ### C.
# Tìm **tên học sinh có điểm cao nhất**.
# Ví dụ:
# ```python
# {
#     "An": 8.5,
#     "Bình": 7.0,
#     "Chi": 9.0,
#     "Dũng": 8.0# }
# ```
# Kết quả:
# ```text
# A. 8.125
# B. 8.25
# C. Chi
def average_score(scores):
    return sum(scores.values()) / len(scores) # Điểm trung bình tổng chia cho số lượng.

def median_score(scores):
    scores = sorted(list(scores.values()))
    n = len(scores)
    if n % 2 == 1:
        return scores[n // 2]
    else:
        return (scores[n // 2 - 1] + scores[n // 2]) / 2

def highest_scorer(scores):
    return max(scores, key = scores.get)
d2 = {"An": 8.5, "Bình": 7.0, "Chi": 9.0, "Dũng": 8.0}
print(average_score(d2)) #8.125
print(median_score(d2)) #8.25
print(highest_scorer(d2)) #Chi



# # Bài 7: So sánh hai dãy số
# Cho hai dãy số nguyên `a` và `b`.
# ### A.
# Tìm các giá trị **xuất hiện trong cả hai dãy**.
# Ví dụ:
# ```text
# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
# ```
# Kết quả:
# ```text
# [3, 4, 5]
# ```
# ### B.
# Tìm các giá trị **chỉ xuất hiện trong dãy `a` mà không xuất hiện trong dãy `b`**.
# Với ví dụ trên:
# ```text
# [1, 2]
# ```
# Mỗi giá trị chỉ cần xuất hiện một lần trong kết quả.
def common_values(a, b):
    sa = set(a)
    sb = set(b)
    return list(sa & sb)

def only_in_a(a, b):
    sa = set(a)
    sb = set(b)
    return list(sa - sb)
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
print(common_values(a, b))
print(only_in_a(a, b))



# # Bài 8: Đếm các giá trị khác nhau
# Cho một dãy số nguyên `a`.
# Tính số lượng **giá trị khác nhau** xuất hiện trong dãy.
# Ví dụ:
# ```text
# a = [1, 2, 2, 3, 3, 3, 4, 5, 5]
# ```
# Các giá trị khác nhau là:
# ```text
# 1, 2, 3, 4, 5
# ```
# Kết quả:
# ```text
# 5
def unique_values(a):
    set_a = set(a) # Chuyển dãy a thành set để lọc bỏ các giá trị trùng nhau
    return len(set_a) # Dùng hàm len() để đếm số lượng phần tử còn lại
a = [1, 2, 2, 3, 3, 3, 4, 5, 5]
print(unique_values(a))



# # Bài 9: Tìm 3 từ xuất hiện nhiều nhất
# Cho một dãy các từ.
# Tìm **3 từ xuất hiện nhiều nhất** trong dãy.
# Kết quả cần chứa từ và số lần xuất hiện của từ đó.
# Ví dụ:
# ```text
# words = [
#     "apple",
#     "banana",
#     "apple",
#     "orange",
#     "banana",
#     "apple",
#     "orange",
#     "banana",
#     "banana"
# ]
# ```
# Kết quả:
# ```text
# banana: 4
# apple: 3
# orange: 2
# ```
# Nếu có nhiều từ có cùng số lần xuất hiện, có thể trả về bất kỳ 3 từ nào trong số đó.
def top_3_words(words):
    # Bước 1: Đếm số lần xuất hiện của từng từ
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    # Bước 2: Sắp xếp các từ theo số lần xuất hiện giảm dần
    sorted_items = sorted(counts.items(), key = lambda x: x[1], reverse = True)
    return sorted_items[:3]
words = ["apple", "banana", "apple", "orange", "banana", "apple", "orange", "banana", "banana"]
print(top_3_words(words))



# # 10. Tính lãi kép
# Ông A bắt đầu đầu tư **x yen** vào chứng khoán từ `n` năm trước.
# Mỗi năm, khoản đầu tư của ông A tăng hoặc giảm `aᵢ%`, trong đó `a` là một dãy số gồm `n` phần tử:
# a = [a₁, a₂, ..., aₙ]
# với:
# -70 < aᵢ < 200
# Quy ước:
# * Nếu `aᵢ > 0`, khoản đầu tư tăng `aᵢ%` trong năm thứ `i`.
# * Nếu `aᵢ < 0`, khoản đầu tư giảm `|aᵢ|%` trong năm thứ `i`.
# * Thuế thu nhập từ đầu tư là **20% phần lợi nhuận**.
# * Thuế chỉ được tính khi ông A bán khoản đầu tư.
# ## A. Đầu tư dài hạn
# Ông A giữ nguyên khoản đầu tư trong `n` năm và chỉ bán toàn bộ khoản đầu tư sau năm thứ `n`.
# Tính số tiền ông A nhận được sau khi bán và nộp thuế.
# ---
# ## B. Lướt sóng
# Thay vì đầu tư dài hạn, ông A bán toàn bộ khoản đầu tư vào cuối mỗi năm và mua lại ngay lập tức bằng toàn bộ số tiền còn lại.
# Mỗi lần bán:
# * Nếu khoản đầu tư có lãi so với số tiền đã bỏ ra khi mua, ông A phải nộp **20% thuế trên phần lợi nhuận**.
# * Nếu khoản đầu tư bị lỗ, ông A không phải nộp thuế.
# Tính số tiền ông A có sau `n` năm.
# ---
# ## C. Khấu trừ lỗ trong các năm tiếp theo
# Giống trường hợp B, ông A vẫn bán và mua lại khoản đầu tư vào cuối mỗi năm.
# Tuy nhiên, khi một năm bị lỗ, khoản lỗ đó có thể được sử dụng để **khấu trừ vào lợi nhuận của các năm tiếp theo trong vòng 3 năm** khi tính thuế.
# Quy tắc:
# * Lỗ phát sinh ở năm `i` được sử dụng để khấu trừ lợi nhuận của các năm `i + 1`, `i + 2`, `i + 3`.
# * Nếu trong một năm có lợi nhuận, sử dụng các khoản lỗ còn được phép khấu trừ để giảm lợi nhuận chịu thuế.
# * Phần lợi nhuận còn lại sau khi khấu trừ chịu thuế suất 20%.
# * Nếu tổng số lỗ được khấu trừ lớn hơn lợi nhuận của năm đó, phần lỗ chưa sử dụng tiếp tục được sử dụng trong các năm tiếp theo nếu vẫn còn trong thời hạn 3 năm.
# * Khoản lỗ đã quá 3 năm mà chưa được sử dụng sẽ mất hiệu lực.
# Tính số tiền ông A có sau `n` năm.
def long_term_investment(x, a):
    money = x
    for rate in a:
        money = money * (1 + rate / 100)

    profit = money - x
    if profit > 0:
        tax = profit * 0.2
        money = money - tax
    return money

def trading_investment(x, a):
    money = x
    for rate in a:
        start_of_year = money
        money = money * (1 + rate / 100)
        profit = money - start_of_year
        if profit > 0:
            tax = profit * 0.2
            money = money - tax
    return money
print(long_term_investment(1000000, [50, -30, 20]))   
print(trading_investment(1000000, [50, -30, 20]))      

print(long_term_investment(1000000, [10, 10, 10]))     
print(trading_investment(1000000, [10, 10, 10]))