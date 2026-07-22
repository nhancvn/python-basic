# =====================================
# Bài 1
# Đề bài:
# Cho hai số a và b.
# Trả về số lớn hơn.
# =====================================

def larger_number(a, b):
    if a > b:
        return a
    else:
        return b
print(larger_number(11, 10))
print(larger_number(24, 40))


# =====================================
# Bài 2
# Đề bài:
# Cho một tên.
# Trả về câu chào.
# =====================================

def greeting(name):
    return f"Xin chào, {name}!"
print(greeting("nha"))


# =====================================
# Bài 3
# Đề bài:
# VIết một hàm tính diện tích tròn
# =====================================

import math
def circle_area(radius):
    return math.pi * radius ** 2
print(circle_area(2))


# =====================================
# bài 4:
# Đề Bài:
# Nhận về một chuỗi và trả về độ dài của chuỗi đó.
# =====================================

def string_length(text):
    return len(text)
print(string_length("python"))


# =====================================
# bài 5:
# Đề bài:
# Nhận vào một list và trả về số lượng tử trong list bằng return.
#=====================================

def count_items(item):
    return len(item)
print(count_items(["金", "木", "水", "火", "土"]))


#=====================================
# bai 6:
# Đề bài:
# Nhận vào một List(teams), nhận vào một đội bóng mới(team), thêm đội bóng đó vào cuối danh sách và trả về list mới.
#=====================================

def add_team(teams, team):
    teams.append(team)
    return teams
team_list = ["Team A", "Team B", "Team C"]
new_team = "Team D"

result = add_team(team_list, new_team)
print(result)



