#Câu 6: Nhập vào 1 list có N số ngẫu nhiên KHÔNG TRÙNG NHAU

import random

N = int(input("Nhập số lượng phần tử N: "))
lst = random.sample(range(0, 100), N)

print("Danh sách gồm", N, "số ngẫu nhiên không trùng nhau là:")
print(lst)
