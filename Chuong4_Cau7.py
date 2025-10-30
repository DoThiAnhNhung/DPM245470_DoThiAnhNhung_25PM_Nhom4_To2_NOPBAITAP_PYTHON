#Câu 7: Tính và xuất độ dài đoạn AB
'''Yêu cầu:
Nhập toạ độ 2 điểm A(xA,yA), B(xB,yB). Tính và xuất độ dài đoạn AB. '''

import math

xA = float(input("Nhập tọa độ x của điểm A: "))
yA = float(input("Nhập tọa đột y của điểm A: "))

xB = float(input("Nhập tọa độ x của điểm B: "))
yB = float(input("Nhập toạ độ y của điểm B: "))

dAB = math.sqrt((xB - xA)**2 + (yB - yA)**2)

print("Độ dài đoạn AB là:", dAB)
