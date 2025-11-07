#Câu 7: Viết chương trình nhập vào một dãy các số theo thứ tự tăng, nếu nhập sai quy cách thì yêu cầu nhập lại. In dãy số sau khi đã nhập xong 

N = int(input("Nhập số lượng phần tử N: "))

lst = []

for i in range(N):
    while True:
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        if i == 0 or x > lst[i - 1]:
            lst.append(x)
            break
        else:
            print("Sai quy tắc! Số sau phải lớn hơn số trước. Nhập lại.")

print("Dãy số tăng dần vừa nhập là:")
print(lst)
