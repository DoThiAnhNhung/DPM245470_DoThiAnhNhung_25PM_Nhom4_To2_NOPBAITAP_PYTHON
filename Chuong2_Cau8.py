# Câu 8: Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python.
'''
Có 3 loại lỗi thường gặp:
- Lỗi cú pháp (Syntax errors): được thông báo bởi trình dịch
- Lỗi ngữ nghĩa (Semantic error): sử dụng kinh nghiệm của lập trình viên để gỡ lỗi
- Lỗi thực thi (Runtime error): xử lí ngoại lệ
a) Sử dụng khối try ... except
Cú pháp:
    try:
        # đoạn code có thể gây lỗi
    except Tên Lỗi:
        # xử lý khi lỗi xảy ra

b) Sử dụng khối try ... except ... else
Cú pháp:
    try:
        # đoạn code
    except Tên lỗi:
        # nếu như có lỗi xảy ra thực thi đoạn code này
    else:
        # nếu không có lỗi xảy ra thực thi đoạn code này

c) Sử dụng khối try ... except ... finally
Cú pháp:
    try:
        # đoạn code
    except Tên lỗi:
        # nếu như có lỗi xảy ra thực thi đoạn code này
    finally:
        # dù có lỗi hay không vẫn thực thi đoạn code này

d) Sử dụng khối try ... except ... else ... finally
Cú pháp:
    try:
        # đoạn code
    except Tên lỗi:
        # nếu như có lỗi xảy ra thực thi đoạn code này
    else:
        # nếu không có lỗi xảy ra thực thi đoạn code này
    finally:
        # dù có lỗi hay không vẫn thực thi đoạn code này
    
'''