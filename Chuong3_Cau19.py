import math

def tinh_S(x, n):
    S = 0
    for i in range(n + 1):
        mu = 2 * i + 1
        S += x**mu / math.factorial(mu)
    return S

def nhap_du_lieu():
    while True:
        try:
            x = float(input("Nhập giá trị x (số thực): "))
            n = int(input("Nhập giá trị n (số nguyên không âm): "))
            if n < 0:
                print("Giá trị n phải là số nguyên không âm. Vui lòng nhập lại.")
                continue
            return x, n
        except ValueError:
            print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")
            
x, n = nhap_du_lieu()
ket_qua = tinh_S(x, n)
print(f"Giá trị của S(x, n) là: {ket_qua}")
