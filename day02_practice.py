# Bài 1
# Cho một List.
# Thêm "Chelsea" vào vị trí thứ 2.

def insert_team(teams):
    teams.insert(1, "Chelsea")
    return teams

teams = ["Real Madrid", "Liverpool"]
print(insert_team(teams))


# bài 2:
# Cho một List.
# Xóa "Chelsea" khỏi List.
def remove_team(teams):
    teams.remove("Chelsea")
    return teams

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(remove_team(teams))


# bài 3:
# Cho một List.
# Trả về phần tử cuối cùng.
def last_team(teams):
    return teams[-1]

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(last_team(teams))


# bài 4:
# Cho một List.
# Xóa phần tử cuối cùng.
def remove_last_team(teams):
    teams.pop()
    return teams

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(remove_last_team(teams))


# bài 5:
# Cho một List.
# Trả về phần tử đầu tiên.
def first_team(teams):
    return teams[0]

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(first_team(teams))


# bài 6:
# cho một List.
# Kiểm tra "Chelsea" có trong List hay ko.
# Trả về True or False.
def has_team(teams):
    return "Chelsea" in teams

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(has_team(teams))


# bài 7:
# Cho một List.
# Đếm số phần tử.
def team_count(teams):
    return len(teams)

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(team_count(teams))


# bài 8:
# Cho một List.
# Đảo ngược List.
def reverse_teams(teams):
    teams.reverse()
    return teams

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(reverse_teams(teams))


# bài 9:
# Cho một List.
# Sắp xếp theo alphabet.
def sort_teams(teams):
    return sorted(teams)

teams = ["Liverpool", "Chelsea", "Real Madrid"]
print(sort_teams(teams))


# bài 10:
# Cho một List.
# Xóa toàn bộ phần tử.
def clear_teams(teams):
    teams.clear()
    return teams

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(clear_teams(teams))


# bài 11:
# Cho một chuỗi.
# Đổi thành chữ thường.
def lower_text(text):
    return text.lower()

print(lower_text("PYTHON"))


# bài 12:
# Cho một chuỗi.
# Đổi thành chữ hoa.
def upper_text(text):
    return text.upper()

print(upper_text("python"))


# bài 13:
# Cho một List.
# Đếm số lần xuất hiện của "Chelsea".
def team_frequency(teams):
    return teams.count("Chelsea")

teams = ["Chelsea", "Real Madrid", "Chelsea", "Liverpool"]
print(team_frequency(teams))


# bài 14:
# Cho một List.
# Thêm "Barcelona" vào cuối List,
# Sau đó sắp xếp theo alphabet
def add_and_sort(teams):
    teams.append("Barcelona")
    teams.sort()
    return teams
teams = ["Liverpool", "Chelsea", "Real Madrid"]
print(add_and_sort(teams))


# bài 15:
# Cho một List.
# Nếu "Chelsea" chưa có thì thêm vào cuối List.
# Nếu đã có thì giữ nguyên.
def add_team_if_not_exists(teams):
    if "Chelsea" not in teams:
        teams.append("Chelsea")
    return teams

teams = ["Real Madrid", "Liverpool"]
print(add_team_if_not_exists(teams))


# bài 16:
# Cho một List.
# Xóa tất cả "Chelsea" khỏi List.
def remove_all_chelsea(teams):
    while "Chelsea" in teams:
        teams.remove("Chelsea")
    return teams

teams = ["Chelsea", "Real Madrid", "Chelsea", "Liverpool", "Chelsea"]
print(remove_all_chelsea(teams))


# bài 17:
# Cho một List.
# Đổi "Chelsea" thành "Arsenal"
def replace_team(teams):
    if "Chelsea" in teams:
        index = teams.index("Chelsea")
        teams[index] = "Arsenal"
    return teams

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(replace_team(teams))


# bài 18:
# Cho một List.
# Trả về List không có phần tử trùng nhau.
def unique_teams(teams):

    return list(set(teams))

teams = ["Chelsea", "Liverpool", "Chelsea", "Real Madrid", "Liverpool"]
print(unique_teams(teams))


# bài 19:
# Cho một List.
# Nối các phần tử thành một chuỗi, ngăn cách bởi dấu ",".
def join_teams(teams):
    return ",".join(teams)

teams = ["Chelsea", "Liverpool", "Real Madrid"]
print(join_teams(teams))