# Câu 9: Phần mềm tính BMI

import tkinter as tk
from tkinter import messagebox

def tinh_bmi():
    try:
        h = float(entry_chieu_cao.get())
        w = float(entry_can_nang.get())
        
        if h <= 0 or w <= 0:
            raise ValueError

        bmi = w / (h * h)
        bmi_var.set(f"{bmi:.2f}")

        # Xác định tình trạng cân nặng
        if bmi < 18.5:
            tinh_trang_var.set("Gầy")
            nguy_co_var.set("Thấp")
        elif bmi < 25:
            tinh_trang_var.set("Bình thường")
            nguy_co_var.set("Trung bình")
        elif bmi < 30:
            tinh_trang_var.set("Hơi béo")
            nguy_co_var.set("Hơi cao")
        else:
            tinh_trang_var.set("Béo phì")
            nguy_co_var.set("Cao")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

def thoat():
    window.destroy()


# ================= TẠO GIAO DIỆN ==================

window = tk.Tk()
window.title("Phần mềm tính BMI")
window.geometry("400x420")
window.config(bg="yellow")

# Nhập chiều cao
tk.Label(window, text="Nhập chiều cao:", bg="yellow").pack(pady=5)
entry_chieu_cao = tk.Entry(window, width=20, justify="center")
entry_chieu_cao.pack()

# Nhập cân nặng
tk.Label(window, text="Nhập cân nặng:", bg="yellow").pack(pady=5)
entry_can_nang = tk.Entry(window, width=20, justify="center")
entry_can_nang.pack()

# Nút tính BMI
tk.Button(window, text="Tính BMI", command=tinh_bmi).pack(pady=10)

# BMI của bạn
tk.Label(window, text="BMI của bạn:", bg="yellow").pack()
bmi_var = tk.StringVar()
tk.Label(window, textvariable=bmi_var, bg="yellow", fg="blue").pack(pady=5)

# Tình trạng
tk.Label(window, text="Tình trạng của bạn:", bg="yellow").pack()
tinh_trang_var = tk.StringVar()
tk.Label(window, textvariable=tinh_trang_var, bg="yellow", fg="red").pack(pady=5)

# Nguy cơ
tk.Label(window, text="Nguy cơ phát triển bệnh:", bg="yellow").pack()
nguy_co_var = tk.StringVar()
tk.Label(window, textvariable=nguy_co_var, bg="yellow", fg="red").pack(pady=5)

# Nút thoát
tk.Button(window, text="Thoát", command=thoat, fg="blue").pack(pady=10)

window.mainloop()
