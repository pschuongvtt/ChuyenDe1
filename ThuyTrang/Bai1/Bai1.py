# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 09:54:40 2022
@author: Đặng thị thùy trang

"""
""" import thư viện"""
import pandas as pdthuytrang
import numpy as npthuytrang

"""khởi tạo biến d"""
d = {'name':pdthuytrang.Series(['tom','james','ricky','vin','steve','smith','jack',
    'lee','david','gasper','betina','andres']),
    'age':pdthuytrang.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
    'rating':pdthuytrang.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}


"""khởi tạo dataframe"""
df = pdthuytrang.DataFrame(d)


"""câu 1: in dữ liệu ra màn hình"""
print('câu 1: in dữ liệu ra màn hình')
print(df)
print('\n\n\n')

"""câu 2a: trả về tổng các giá trị"""
print('câu 2a: trả về tổng các giá trị')
print(df.sum())
print('\n\n\n')

"""câu 2b: tính tổng theo chiều ngang"""
print('câu 2b: tính tổng theo chiều ngang')
print(df.sum(1))
print('\n\n\n')

# """câu 3: trả về giá trị trung bình"""
print('câu 3: trả về giá trị trung bình')
print(df.mean())
print('\n\n\n')

"""câu 4: tính toán một bản tóm tắt thống kê liên quan đến các cột dataframe"""
print('câu 4: bảng thống kê các cột dataframe')
print(df.describe())
print('\n\n\n')

# """bài 10: đọc dữ liệu và kĩ thuật reindexing - python pandas"""

print('câu 5: đọc dữ liệu và kĩ thuật reindexing - python pandas')
df = pdthuytrang.read_csv("./sales_14.csv", header=0, index_col='Date', parse_dates=True)
print(df.head())
print('\n\n\n')

"""bài 11: làm việc với dữ liệu text (p1) - python pandas"""

s = pdthuytrang.Series(['tom', 'william rick', 'john', 'alber@t', npthuytrang.nan, '1234','stevesmith'])

print('câu 6: in ra màn hình')
print(s)
print("\n\n\n")

print('câu 7: chuyển chuỗi string thành chữ thường')
print(s.str.lower())
print("\n\n\n")

print('câu 8: chuyển chuỗi string thành chữ in hoa')
print(s.str.upper())
print("\n\n\n")

print('câu 9: độ dài chuỗi')
print(s.str.len())
print("\n\n\n")

print('câu 10: loại bỏ khoảng trắng')
print("after stripping:")
print(s.str.strip())
print("\n\n\n")
# """""""-----------------------------------"""
# """a. dataframe là dictionary"""

print('câu 11: dân số và diện tích của một số tỉnh / thành phố ở việt nam')
population = pdthuytrang.Series({'tp.hcm': 8993, 'hanoi': 8053, 'lam dong': 1297, 'quang tri': 623})
area = pdthuytrang.Series({'tp.hcm': 2061, 'hanoi': 3359, 'lam dong': 9765, 'quang tri': 4746})
data = pdthuytrang.DataFrame({'dân số': population, 'diện tích': area})
print(data)
print('\n\n\n')


print('câu 12: bảng dân số việt nam')
print(data['dân số'])
print('\n\n\n')


print('câu 13: bảng mật độ, dân số, diện tích việt nam')
data['mật độ'] = data['dân số'] / data['diện tích']
print(data)
print('\n\n\n')

# """""""-----------------------------------"""
# """c. indexing trong dataframe"""

print('câu 14: lấy hàng đầu tiên')
print("\ndữ liệu của tp.hcm:\n ",data.iloc[0])
print("\n\n\n")
 
print('câu 15: lấy dữ liệu 3 hàng đầu tiên')
print("\n dữ liệu của tp.hcm, hà nội và lâm đồng:\n ",data.iloc[:3])
print("\n\n\n")

print('câu 16: lấy dữ liệu 2 hàng và 2 cột đầu tiên')
print("\n dữ liệu dân số và diện tích của tp.hcm và hà nội:\n ",data.iloc[:2, :2])
print("\n\n\n")

print('câu 17: lấy dữ liệu tất cả các hàng và cột cuối cùng')
print("\n mật độ dân số của các tỉnh / thành phố:\n ",data.iloc[:, -1])
