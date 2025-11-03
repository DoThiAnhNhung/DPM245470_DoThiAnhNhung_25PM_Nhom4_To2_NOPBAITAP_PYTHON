#Câu 5: Xử lý chuỗi với các hàm cơ bản
'''Yêu cầu:
Viết chương trình cho phép nhập vào 1 chuỗi. Yêu cầu xuất ra:
- Bao nhiêu chữ IN HOA
- Bao nhiêu chữ in thường
- Bao nhiêu chữ là chữ số
- Bao nhiêu chữ là ký tự đặc biệt
- Bao nhiêu chữ là khoảng trắng
- Bao nhiêu chữ là Nguyên Âm
- Bao nhiêu chữ là Phụ âm'''

s=input("Nhập chuỗi: ")
sochuhoa=0
sochuthuong=0
sochuso=0
sokydacbiet=0
sokhoangtrang=0
songuyenam=0
sophuam=0
nguyenam="aAeEiIoOuUyY"
for c in s:
    if c.isupper():
        sochuhoa+=1
    elif c.islower():
        sochuthuong+=1
    elif c.isdigit():
        sochuso+=1
    elif c.isspace():
        sokhoangtrang+=1
    else:
        sokydacbiet+=1
    if c in nguyenam:
        songuyenam+=1
    elif c.isalpha():
        sophuam+=1
print("Số chữ IN HOA =",sochuhoa)
print("Số chữ in thường =",sochuthuong)
print("Số chữ số =",sochuso)
print("Số ký tự đặc biệt =",sokydacbiet)
print("Số khoảng trắng =",sokhoangtrang)
print("Số Nguyên Âm =",songuyenam)
print("Số Phụ âm =",sophuam)


