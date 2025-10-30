#Câu 9: Viết chương trình tính căn bậc 2 lồng nhau

import math

n = int(input("Nhập n: "))
S = 0  
for i in range(n):
    S = math.sqrt(2 + S)
print(f"S({n}) = {S}")
