#Câu 10: Xử lý Ma Trận
'''Yêu cầu:
Nhập 2 matrix A, B.
Cộng 2 matrix
Viết hàm tính matrix hoán vị➔áp dụng để tìm cho A, B'''

def nhap_ma_tran(ten):
    hang = int(input(f"Nhập số hàng của ma trận {ten}: "))
    cot = int(input(f"Nhập số cột của ma trận {ten}: "))
    print(f"Nhập các phần tử cho ma trận {ten}:")
    M = []
    for i in range(hang):
        row = [int(x) for x in input(f"  Hàng {i+1}: ").split()]
        M.append(row)
    return M

def in_ma_tran(M, ten):
    print(f"\nMa trận {ten}:")
    for row in M:
        print(row)

def cong_ma_tran(A, B):
    hang = len(A)
    cot = len(A[0])
    C = []
    for i in range(hang):
        dong = []
        for j in range(cot):
            dong.append(A[i][j] + B[i][j])
        C.append(dong)
    return C

def hoan_vi(M):
    hang = len(M)
    cot = len(M[0])
    HT = []
    for j in range(cot):
        dong = []
        for i in range(hang):
            dong.append(M[i][j])
        HT.append(dong)
    return HT

print("=== NHẬP MA TRẬN A ===")
A = nhap_ma_tran("A")

print("=== NHẬP MA TRẬN B ===")
B = nhap_ma_tran("B")

in_ma_tran(A, "A")
in_ma_tran(B, "B")

C = cong_ma_tran(A, B)
in_ma_tran(C, "A + B")

AT = hoan_vi(A)
BT = hoan_vi(B)
in_ma_tran(AT, "A^T (hoán vị của A)")
in_ma_tran(BT, "B^T (hoán vị của B)")
