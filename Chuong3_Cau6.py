#Câu 6: Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.(vd: n=35 => Ba mươi lăm, n=5 => năm). 

n = int(input("Nhập số (0-99): "))

so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

if n < 10:
    print(so[n].capitalize())
else:
    chuc = n // 10
    donvi = n % 10
    doc = ""

    # Hàng chục
    if chuc == 1:
        doc = "mười"
    else:
        doc = so[chuc] + " mươi"

    # Hàng đơn vị
    if donvi == 0:
        pass
    elif donvi == 1 and chuc > 1:
        doc += " mốt"
    elif donvi == 5:
        doc += " lăm"
    else:
        doc += " " + so[donvi]

    print(doc.capitalize())

