#Câu 6: Trích lọc số âm trong chuỗi
'''Yêu cầu:
Viết một hàm đặt tên là NegativeNumberInStrings(str). Hàm này có đối số truyền vào
là một chuỗi bất kỳ, Hãy viết lệnh để xuất ra các số nguyên âm trong chuỗi.
Ví dụ: Nếu nhập vào chuỗi “abc-5xyz-12k9l--p” thì hàm phải xuất ra được 2 số nguyên
âm đó là -5 và -12'''

def NegativeNumberInStrings(s):
    i = 0
    result = []
    while i < len(s):
        if s[i] == '-' and i + 1 < len(s) and s[i + 1].isdigit():
            j = i + 1
            number = '-'  
            while j < len(s) and s[j].isdigit():
                number += s[j]
                j += 1
            result.append(int(number))  
            i = j
        else:
            i += 1

    print("\n🔍 Các số nguyên âm tìm thấy trong chuỗi:")
    if result:
        for num in result:
            print(num)
    else:
        print("Không có số nguyên âm nào trong chuỗi.")

chuoi = input("Nhập vào một chuỗi bất kỳ: ")
NegativeNumberInStrings(chuoi)


