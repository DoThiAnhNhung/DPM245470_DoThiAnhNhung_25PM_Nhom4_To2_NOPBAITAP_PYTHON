#Câu 7: Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày vừa nhập (ngày/tháng/năm).
import datetime


ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

d = datetime.date(nam, thang, ngay)

ngay_ke_tiep = d + datetime.timedelta(days=1)

print("Ngày kế tiếp là: {}/{}/{}".format(ngay_ke_tiep.day, ngay_ke_tiep.month, ngay_ke_tiep.year))
