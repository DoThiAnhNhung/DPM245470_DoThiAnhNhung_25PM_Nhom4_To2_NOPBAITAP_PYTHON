#Câu 14: Cho biết bao nhiêu dấu * được in ra trên màn hình
'''Yêu cầu:
a = 0
while a < 100:
    b = 0
    while b < 40:
        if (a + b) % 2 == 0:
            print("*", end='')
        b += 1
    print()
    a += 1
'''

'''
a chạy từ 0 đến 99 (100 lần lặp)
b chạy từ 0 đến 39 (40 lần lặp)
Tổng số dấu * được in ra là: 100*40/2=2000 dấu *    
'''