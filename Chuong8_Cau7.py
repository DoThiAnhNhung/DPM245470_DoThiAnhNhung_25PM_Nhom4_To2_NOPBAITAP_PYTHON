#Câu 7: Thiết kế màn hình chuyển năm Dương Lịch thành Âm Lịch

from tkinter import *

root = Tk()
root.title("Chuyển năm dương sang âm lịch")

# Màu nền theo bài
frame = Frame(root, bg="yellow", padx=20, pady=20)
frame.pack(padx=10, pady=10)

Label(frame, text="Nhập năm dương:", bg="yellow", font=("Arial", 12)).grid(row=0, column=0, pady=5)

entry_year = Entry(frame, font=("Arial", 12), width=12)
entry_year.grid(row=0, column=1, pady=5, padx=10)

result_label = Label(frame, text="Năm âm:", bg="yellow", font=("Arial", 12))
result_label.grid(row=1, column=0, pady=10)

result_value = Label(frame, text="", bg="yellow", font=("Arial", 12, "bold"))
result_value.grid(row=1, column=1, pady=10)


# Danh sách Can – Chi
CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

def convert():
    try:
        year = int(entry_year.get())
        can = CAN[(year + 6) % 10]
        chi = CHI[(year + 8) % 12]
        result_value.config(text=f"{can} {chi}")
    except:
        result_value.config(text="Năm không hợp lệ")

Button(frame, text="Chuyển", font=("Arial", 11), command=convert, width=10).grid(row=0, column=2, padx=10)

root.mainloop()
