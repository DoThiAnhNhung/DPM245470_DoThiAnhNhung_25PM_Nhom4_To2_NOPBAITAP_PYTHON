
n = int(input("Nhập kích thước n: "))

print("\nHình vuông:")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print()

print("Tam giác vuông:")
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(i):
            print("*", end=" ")
    print()