# Bài 1
# Thêm "Chelsea" vào vị trí thứ 2.
def insert_team(teams):
    # Cách này dùng vòng lặp chạy qua từng phần tử của mảng cũ, 
    # đến vị trí index 1 (vị trí thứ 2) thì nhét chữ "Chelsea" vào mảng mới res trước, 
    # rồi mới thêm phần tử hiện tại vào sau. Nếu mảng ngắn quá chưa tới 2 phần tử thì xử lý thêm ở cuối.
    res = []
    for i in range(len(teams)):
        if i == 1:
            res.append("Chelsea")
        res.append(teams[i])
    if len(teams) < 2:
        res.append("Chelsea")
    return res



# bài 2:
# Xóa "Chelsea" khỏi List.
def remove_team(teams):
    # Duyệt qua mảng cũ, dùng biến cờ removed để đánh dấu. 
    # Nếu gặp "Chelsea" lần đầu tiên thì bỏ qua (không đưa vào mảng mới), 
    # còn lại thì cứ add hết vào res.
    res = []
    removed = False
    for item in teams:
        if item == "Chelsea" and not removed:
            removed = True
        else:
            res.append(item)
    return res

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(remove_team(teams))


# bài 3:
# Trả về phần tử cuối cùng.
def last_team(teams):
    # Dùng vòng lặp while đếm từ đầu đến cuối mảng để lấy tổng số phần tử, 
    # sau đó trừ đi 1 để lấy vị trí index cuối cùng và trả về phần tử đó.
    idx = 0
    while idx < len(teams):
        idx += 1
    return teams[idx - 1]

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(last_team(teams))


# bài 4:
# Xóa phần tử cuối cùng.
def remove_last_team(teams):
    # Tạo một mảng mới và dùng vòng lặp chạy từ đầu đến sát phần tử cuối cùng (len(teams) - 1), 
    # copy hết vào để bỏ qua phần tử cuối.
    res = []
    for i in range(len(teams) - 1):
        res.append(teams[i])
    return res

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(remove_last_team(teams))


# bài 5:
# Trả về phần tử đầu tiên.
def first_team(teams):
    # Dùng vòng lặp duyệt qua mảng và bắt ngay phần tử đầu tiên rồi return luôn, khỏi cần dùng index [0].
    for item in teams:
        return item

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(first_team(teams))


# bài 6:
# Kiểm tra "Chelsea" có trong List hay ko.
# Trả về True or False.
def has_team(teams):
    # Tạo biến found = False, duyệt qua từng phần tử,
    # nếu thấy khớp chữ "Chelsea" thì đổi trạng thái thành True rồi trả về kết quả.
    found = False
    for item in teams:
        if item == "Chelsea":
            found = True
    return found

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(has_team(teams))


# bài 7:
# Đếm số phần tử.
def team_count(teams):
    # Khởi tạo biến đếm bằng 0, duyệt qua từng phần tử trong mảng, mỗi lần qua một phần tử thì cộng dồn biến đếm lên 1.
    count = 0
    for _ in teams:
        count += 1
    return count

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(team_count(teams))


# bài 8:
# Đảo ngược List.
def reverse_teams(teams):
    # Dùng vòng lặp while chạy lùi từ vị trí phần tử cuối cùng về 0, nhét lần lượt các phần tử đó vào mảng mới res để tạo chuỗi đảo ngược.
    res = []
    i = len(teams) - 1
    while i >= 0:
        res.append(teams[i])
        i -= 1
    return res

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(reverse_teams(teams))


# bài 9:
# Sắp xếp theo alphabet.
def sort_teams(teams):
    # Dùng thuật toán sắp xếp nổi bọt (Bubble Sort) kinh điển. So sánh 2 phần tử đứng cạnh nhau, 
    # nếu đứa đứng trước lớn hơn đứa đứng sau theo thứ tự chữ cái thì đổi chỗ cho nhau.
    arr = []
    for x in teams:
        arr.append(x)
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

teams = ["Liverpool", "Chelsea", "Real Madrid"]
print(sort_teams(teams))


# bài 10:
# Xóa toàn bộ phần tử.
def clear_teams(teams):
    # Dùng vòng lặp while kiểm tra chừng nào mảng vẫn còn độ dài lớn hơn 0 thì liên tục dùng hàm pop() để bứng dần phần tử cuối đi cho đến khi sạch bóng.
    while len(teams) > 0:
        teams.pop()
    return teams

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(clear_teams(teams))


# bài 11:
# Đổi thành chữ thường.
def lower_text(text):
    # Duyệt qua từng ký tự trong chuỗi, lấy mã ASCII của nó thông qua hàm ord(). 
    # Nếu nằm trong khoảng chữ hoa (65 đến 90) thì cộng thêm 32 để chuyển thành mã ASCII chữ thường, rồi đổi ngược lại thành ký tự bằng hàm chr().
    res = ""
    for char in text:
        code = ord(char)
        if 65 <= code <= 90:
            res += chr(code + 32)
        else:
            res += char
    return res

print(lower_text("PYTHON"))


# bài 12:
# Đổi thành chữ hoa.
def upper_text(text):
    # Tương tự bài trên nhưng ngược lại: duyệt mã ASCII, nếu là chữ thường (97 đến 122) thì trừ đi 32 để ép nó dịch chuyển về bảng mã chữ hoa.
    res = ""
    for char in text:
        code = ord(char)
        if 97 <= code <= 122:
            res += chr(code - 32)
        else:
            res += char
    return res

print(upper_text("python"))


# bài 13:
# Đếm số lần xuất hiện của "Chelsea".
def team_frequency(teams):
    # Tạo biến đếm bằng 0, quét qua từng phần tử, cứ thấy chỗ nào khớp chữ "Chelsea" là tăng biến đếm lên 1 đơn vị.
    count = 0
    for item in teams:
        if item == "Chelsea":
            count += 1
    return count

teams = ["Chelsea", "Real Madrid", "Chelsea", "Liverpool"]
print(team_frequency(teams))


# bài 14:
# Thêm "Barcelona" vào cuối List,
# Sau đó sắp xếp theo alphabet
def add_and_sort(teams):
    # Copy mảng cũ sang mảng mới, nhét thêm "Barcelona"
    # vào cuối rồi áp dụng thuật toán Bubble Sort tự viết để sắp xếp lại toàn bộ theo thứ tự chữ cái.
    arr = []
    for item in teams:
        arr.append(item)
    arr.append("Barcelona")
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

teams = ["Liverpool", "Chelsea", "Real Madrid"]
print(add_and_sort(teams))


# bài 15:
# Nếu "Chelsea" chưa có thì thêm vào cuối List.
# Nếu đã có thì giữ nguyên.
def add_team_if_not_exists(teams):
    # Kiểm tra một lượt xem có mặt "Chelsea" chưa.
    # Nếu sau vòng lặp mà biến cờ exist vẫn là False (tức là chưa có) thì mới dùng append() để thêm vào cuối.
    exist = False
    for item in teams:
        if item == "Chelsea":
            exist = True
            break
    if not exist:
        teams.append("Chelsea")
    return teams

teams = ["Real Madrid", "Liverpool"]
print(add_team_if_not_exists(teams))


# bài 16:
# Xóa tất cả "Chelsea" khỏi List.
def remove_all_chelsea(teams):
    # Duyệt qua mảng, lọc sạch sẽ bằng cách chỉ nhặt những phần tử nào khác "Chelsea" cho vào mảng mới res, bỏ qua toàn bộ mấy đứa tên Chelsea.
    res = []
    for item in teams:
        if item != "Chelsea":
            res.append(item)
    return res

teams = ["Chelsea", "Real Madrid", "Chelsea", "Liverpool", "Chelsea"]
print(remove_all_chelsea(teams))


# bài 17:
# Đổi "Chelsea" thành "Arsenal"
def replace_team(teams):
    # Quét từng phần tử qua vòng lặp, nếu gặp "Chelsea" thì đổi gió nhét chữ "Arsenal" vào mảng mới, còn lại giữ nguyên hiện trạng.
    res = []
    for item in teams:
        if item == "Chelsea":
            res.append("Arsenal")
        else:
            res.append(item)
    return res

teams = ["Real Madrid", "Chelsea", "Liverpool"]
print(replace_team(teams))


# bài 18:
# Trả về List không có phần tử trùng nhau.
def unique_teams(teams):
    # Dùng thuật toán lọc trùng thủ công bằng 2 vòng lặp lồng nhau: 
    # vòng ngoài lấy phần tử, vòng trong soi xem phần tử đó đã có mặt trong mảng kết quả res chưa. 
    # Nếu chưa thì mới cho vào.
    res = []
    for item in teams:
        dup = False
        for x in res:
            if x == item:
                dup = True
                break
        if not dup:
            res.append(item)
    return res

teams = ["Chelsea", "Liverpool", "Chelsea", "Real Madrid", "Liverpool"]
print(unique_teams(teams))


# bài 19:
# Nối các phần tử thành một chuỗi, ngăn cách bởi dấu ",".
def join_teams(teams):
    # Tạo một chuỗi rỗng res, dùng vòng lặp nối từng phần tử lại với nhau. 
    # Cứ sau mỗi phần tử (trừ phần tử cuối cùng ra) thì gắn thêm dấu phẩy , vào đằng sau.
    res = ""
    for i in range(len(teams)):
        res += teams[i]
        if i < len(teams) - 1:
            res += ","
    return res

teams = ["Chelsea", "Liverpool", "Real Madrid"]
print(join_teams(teams))