#Câu 12: Hàm oscillate
'''Yêu cầu:
Cho mã lệnh:
for n in oscillate(-3 ,5):
    print(n, end=' ')
print()
'''

def oscillate(a, b):
    for i in range(a, 0):
        yield i
        yield -i

    yield 0
    yield 0

    for i in range(1, b):
        yield i
        yield -i

for n in oscillate(-3, 5):
    print(n, end=' ')
print()
