#Câu 7: Tối ưu chuỗi danh từ
'''Yêu cầu:
Viết chương trình tối ưu Chuỗi danh từ
Một Chuỗi được gọi là tối ưu khi: Không chứa các khoảng trắng dư thừa, các từ cách
nhau bởi một khoảng trắng, Ký tự đầu tiên của các từ Viết Hoa
Ví dụ:
Input “ TRần duY thAnH ”
Output “Trần Duy Thanh”'''

def toiUuChuoiDanhTu(s):
    tu_list = s.strip().split()
    tu_list = [tu.capitalize() for tu in tu_list]
    ket_qua = ' '.join(tu_list)
    return ket_qua

chuoi = input("Nhập chuỗi danh từ: ")
chuoi_toi_uu = toiUuChuoiDanhTu(chuoi)

print("Chuỗi sau khi tối ưu:", chuoi_toi_uu)
