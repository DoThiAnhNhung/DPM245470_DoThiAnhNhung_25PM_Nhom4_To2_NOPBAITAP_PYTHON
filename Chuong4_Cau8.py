#Câu 8: Viết chương trình tính loga^x
'''
Yêu cầu:
Viết chương trình tính loga
x với a, x là các số thực nhập vào từ bàn phím, và x>0, a>0, a
!= 1.( dùng logax=lnx/lna)
'''
import math
a = float(input("Nhập cơ số a (a>0 và a!=1): "))
x = float(input("Nhập số mũ x (x>0): "))

if a <= 0 and a == 1 and x <= 0:
    print("Giá trị a hoặc x không hợp lệ.")
else:
    log_ax = math.log(x) / math.log(a)
    print(f"log_{a}^({x}) =", log_ax)

    