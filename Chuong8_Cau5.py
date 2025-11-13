#Câu 5: Màn hình đăng nhập

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Enter New Password")
root.geometry("300x200")
root.readprofile(False,False)

Label(root, text="Enter New Password", fg= "purple", font=("Arial", 12, "bold")).pack(pady=5)

frame = Frame(root)
frame.pack()

Label(frame, text="Old Password: ").grid(row=0, column=0, sticky= "e", pady = 5, padx=5)
Label(frame, text="New Password: ").grid(row=1, column=0, sticky= "e", pady = 5, padx=5)
Label(frame, text="Enter New Password Again: ").grid(row=2, column=0, sticky= "e", pady = 5, padx=5)

old_pass = Entry(frame, show="*",width=25)
new_pass = Entry(frame, show="*",width=25)
re_pass = Entry(frame, show="*",width=25)

old_pass.grid(row=0, column =1)
new_pass.grid(row=1, column =1)
re_pass.grid(row=2, column =1)

def doi_mk():
    old = old_pass.get()
    new = new_pass.get()
    re = re_pass.get()

    if old !="123":
        messagebox.showerror("Lỗi", "Mật khẩu cũ không đúng!")
    elif new == "" or re == "":
        messagebox.showerror("Cảnh báo", "Vui lòng nhập đủ các ô!")
    elif new != re:
        messagebox.showerror("Lỗi", "Mật khẩu không khớp!")
    else:
        messagebox.showerror("Thành công", "Đổi mật khẩu thành công!")

def huy():
        root.destroy()

frame_btn = Frame(root)
frame_btn.pack(pady = 10)

Button(frame_btn, text="Ok", width = 10,command=doi_mk).grid(row=0,column=0, padx = 5)
Button(frame_btn, text="Cancel", width = 10,command=huy).grid(row=0,column=1, padx = 5)

root.mainloop()