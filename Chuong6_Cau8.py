#Câu 8: Viết chương trình nhập vào một dãy n số thực M[0], M[1],..., M[n-1], sắp xếp dãy số theo thứ tự giảm dần. Xuất ra dãy số sau khi sắp xếp.

n = int(input("Nhập số lượng phần tử n: "))

M = [int(input(f"Nhập M[{i}]: ")) for i in range(n)]

print("Dãy ban đầu:", M)
M_sorted = sorted(M, reverse=True)

print("Dãy sau khi sắp xếp giảm dần:", M_sorted)
