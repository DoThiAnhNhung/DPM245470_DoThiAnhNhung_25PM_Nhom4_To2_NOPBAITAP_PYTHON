#Câu 8: Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo đúng phép toán đã nhập

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

phep_tinh = input("Nhập phép tính (+, -, *, /): ")

if phep_tinh == '+':
    ket_qua = a + b
    print(f"Kết quả: {a} + {b} = {ket_qua}")
elif phep_tinh == '-':
    ket_qua = a - b
    print(f"Kết quả: {a} - {b} = {ket_qua}")
elif phep_tinh == '*':
    ket_qua = a * b
    print(f"Kết quả: {a} * {b} = {ket_qua}")
elif phep_tinh == '/':
    if b != 0:
        ket_qua = a / b
        print(f"Kết quả: {a} / {b} = {ket_qua}")
    else:
        print("Lỗi: Không thể chia cho 0.")