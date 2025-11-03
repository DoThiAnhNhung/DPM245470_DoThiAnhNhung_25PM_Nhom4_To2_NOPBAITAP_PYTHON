#Câu 4: Xác định kết quả khi thực thi list
'''Yêu cầu:
Cho list
lst = [3, 0, 1, 5, 2]
x = 2
Hãy cho biết kết quả:
(a) lst[0]?
(b) lst[3]?
(c) lst[x]?
(d) lst[-x]?
(e) lst[x + 1]?
(f) lst[x] + 1?
(g) lst[lst[x]]?
(h) lst[lst[lst[x]]]?'''

'''
(a) lst[0]  -> 3
(b) lst[3]  -> 5
(c) lst[x]  -> lst[2] -> 1
(d) lst[-x] -> lst[-2] -> 5
(e) lst[x + 1] -> lst[3] -> 5
(f) lst[x] + 1 -> lst[2] + 1 -> 1 + 1 -> 2
(g) lst[lst[x]] -> lst[lst[2]] -> lst[1] -> 0
(h) lst[lst[lst[x]]] -> lst[lst[lst[2]]] -> lst[lst[1]] -> lst[0] -> 3
'''