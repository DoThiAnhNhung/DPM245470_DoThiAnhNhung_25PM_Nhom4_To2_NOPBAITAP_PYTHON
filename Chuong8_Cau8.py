#Câu 8: Thiết kế màn hình chuyển độ F thành độ C
import tkinter as tk
from tkinter import messagebox

def chuyen_doi():
    try:
        f = float(entry_f.get())              # Lấy giá trị F từ ô nhập
        c = (f - 32) * 5/9                    # Công thức đổi sang độ C
        ket_qua_var.set(f"{c:.2f}")           # Hiển thị kết quả lên màn hình
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Chuyển đổi độ F sang độ C")
window.geometry("350x200")
window.config(bg="yellow")

# Nhãn nhập độ F
label_f = tk.Label(window, text="Nhập độ F", bg="yellow")
label_f.pack(pady=5)

# Ô nhập độ F
entry_f = tk.Entry(window, width=15, justify="center")
entry_f.pack()

# Nút chuyển
btn = tk.Button(window, text="Chuyển", command=chuyen_doi)
btn.pack(pady=10)

# Nhãn độ C
label_c = tk.Label(window, text="Độ C", bg="yellow")
label_c.pack()

# Biến hiển thị kết quả
ket_qua_var = tk.StringVar()
label_kq = tk.Label(window, textvariable=ket_qua_var, bg="yellow", fg="blue", font=("Arial", 12))
label_kq.pack()

window.mainloop()
