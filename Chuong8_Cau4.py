#Câu 4: Phần mềm máy tính bỏ túi
from tkinter import *
root = Tk()

e = Entry(root, width= 25, borderwidth = 5, justify = 'right', font = ('Arial',14))
e.grid(row = 0, column = 0, columnspan = 4, pady = 10)

def nhap(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(num))

def xoa():
    e.delete(0, END)

def ketqua():
    try:
        bieu_thuc = e.get()
        result = eval(bieu_thuc)
        e.delete(0, END)
        e.insert(0, str(result))
    except:
        e.delete(0, END)
        e.insert(0, "Lỗi")

Button(root, text="1", padx=20, pady=15, command = lambda: nhap("1")).grid(row= 1,column=0)
Button(root, text="2", padx=20, pady=15, command = lambda: nhap("2")).grid(row= 1,column=1)
Button(root, text="3", padx=20, pady=15, command = lambda: nhap("3")).grid(row= 1,column=2)

Button(root, text="4", padx=20, pady=15, command = lambda: nhap("4")).grid(row= 2,column=0)
Button(root, text="5", padx=20, pady=15, command = lambda: nhap("5")).grid(row= 2,column=1)
Button(root, text="6", padx=20, pady=15, command = lambda: nhap("6")).grid(row= 2,column=2)

Button(root, text="7", padx=20, pady=15, command = lambda: nhap("7")).grid(row= 3,column=0)
Button(root, text="8", padx=20, pady=15, command = lambda: nhap("8")).grid(row= 3,column=1)
Button(root, text="9", padx=20, pady=15, command = lambda: nhap("9")).grid(row= 3,column=2)

Button(root, text="-", padx=20, pady=15, command = lambda: nhap("-")).grid(row= 4,column=0)
Button(root, text="0", padx=20, pady=15, command = lambda: nhap("0")).grid(row= 4,column=1)
Button(root, text=".", padx=20, pady=15, command = lambda: nhap(".")).grid(row= 4,column=2)

Button(root, text="+", padx=20, pady=15, command = lambda: nhap("+")).grid(row= 5,column=0)
Button(root, text="*", padx=20, pady=15, command = lambda: nhap("*")).grid(row= 5,column=1)
Button(root, text="/", padx=20, pady=15, command = lambda: nhap("/")).grid(row= 5,column=2)

Button(root, text="=", padx=20, pady=15, command = ketqua).grid(row= 5,column=3)

Button(root, text="Clr", padx=85, pady=15, command = xoa).grid(row=6, column = 0, columnspan=4)

root.mainloop() 