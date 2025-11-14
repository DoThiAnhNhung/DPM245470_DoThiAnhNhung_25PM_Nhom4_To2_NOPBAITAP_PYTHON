#Câu 6: Màn hình cấu hình Style cho Button

from tkinter import *

root = Tk()
root.title("frame 2")

frame = Frame(root, padx=10, pady=10)
frame.pack()

styles = ["raised", "sunken", "flat", "ridge", "groove", "solid"]

# tạo 5 dòng ứng với borderwidth = 0 → 4
for bw in range(5):
    # cột 1: label borderwidth
    Label(frame, text=f"borderwidth = {bw}", width=18).grid(row=bw, column=0, padx=5, pady=5)

    # các button style
    for i, st in enumerate(styles):
        btn = Button(frame,
                     text=st,
                     width=10,
                     relief=st,
                     borderwidth=bw)
        btn.grid(row=bw, column=i+1, padx=5, pady=5)

root.mainloop()
