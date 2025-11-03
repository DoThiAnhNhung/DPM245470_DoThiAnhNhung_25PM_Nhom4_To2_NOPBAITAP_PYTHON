#Câu 8: Tách lấy tên bài hát
'''Yêu cầu:
Cho một chuỗi là đường dẫn của 1 file nhạc, ví dụ: d:\\music\muabui.mp3
Hãy viết 2 hàm để:
- Lấy ra muabui.mp3
- Lấy ra muabui
Lưu ý đường dẫn bài hát là bất kỳ. Nên khi truyền vào bài hát nào thì lấy chính xác theo
bài hát đó.'''

def layTenBaiHat(path):

    parts = path.replace("\\", "/").split("/")
    return parts[-1]

def layTenBaiHat1(path):
    ten_file = layTenBaiHat(path)

    return ten_file.split(".")[0]
duong_dan = input("Nhập đường dẫn file nhạc: ")

print("Tên file có đuôi:", layTenBaiHat(duong_dan))
print("Tên file không có đuôi:", layTenBaiHat1(duong_dan))

