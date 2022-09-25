# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''Bước 1: Import thư viện'''
import pandas as pd
import numpy as np

'''Bước 2: Khởi tạo biến d datafame có data'''
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack','Lee','David','Gasper','Betina','Andres']),
     'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
     'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}

'''Bước 3: Khởi tạo mảng với biến d vừa khai báo'''
df = pd.DataFrame(d)

'''Bài làm'''
'''Câu 1: In dữ liệu ra màn hình'''
print('Câu 1: In dữ liệu ra màn hình')
print(df)
print('\n\n')

'''
    Câu 2a: Trả về tổng các giá trị cho trục được yêu cầu theo trục Ox. 
           Theo mặc định, trục là chỉ số (trục = 0)
'''
print('Câu 2a: Trả về tổng các giá trị cho trục được yêu cầu theo trục Oy')
print(df.sum())        
print('\n\n')

'''
    Câu 2b: Trả về tổng các giá trị cho trục được yêu cầu theo trục Ox
           Theo mặc định, trục là chỉ số (trục = 0)
'''
print('Câu 2b: Trả về tổng các giá trị cho trục được yêu cầu theo trục Ox')
print(df.sum(1))        
print('\n\n')

'''Câu 3: Trả về giá trị trung bình'''
print('Câu 3: Trả về giá trị turng bình')
print(df.mean()) #Chỉ lấy cột có giá trị int, float để sum, chuỗi không sum dc 
print('\n\n')

'''
    Bài toán tổng hợp dữ liệu
    description (): tính toán một bản tóm tắt thống kê liên quan đến các cột DataFrame
'''
print('Câu 4: Trả về giá trị turng bình')
print(df.describe()) #Chỉ lấy cột có giá trị int, float để sum, chuỗi không sum dc 
print('\n\n')


'''Câu 5: Bài toán đọc dữ liệu và kỹ thuật từ file excel'''
print('Câu 5: Đọc dữ liệu từ file excel')
dfnew = pd.read_csv("C:/Users/NgocAnh/Desktop/ChuyenDe1/sales_dataroot.csv",header=0, index_col='Date', parse_dates=True)
print(dfnew.head())
print('\n\n')

'''---------------------------------------------------------------------------------------------------------------------'''

'''Bước 2: Khởi tạo biến d datafame có data'''
s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

'''Bài làm'''
'''Câu 1: In dữ liệu ra màn hình'''
print('Câu 1: In dữ liệu ra màn hình')
print(s)
print('\n\n')

'''Câu 2: Chuyển chuỗi String thành chữ thường'''
print('Câu 2: Chuyển chuỗi String thành chữ thường')
print(s.str.lower())
print('\n\n')

'''Câu 3: Chuyển chuỗi String thành chữ hoa'''
print('Câu 3: Chuyển chuỗi String thành chữ in hoa')
print(s.str.upper())
print('\n\n')

'''Câu 4: Tính độ dài chuỗi'''
print('Câu 4: Độ dài chuỗi')
print(s.str.len())
print('\n\n')

'''Câu 5: Loại bỏ khoảng trắng'''
print('Câu 5: Loại bỏ khoảng trắng')
print(s.str.strip())
print('\n\n')

'''---------------------------------------------------------------------------------------------------------------------'''
'''Tạo 1 mảng dữ liệu cho sẵn theo biến population'''
population = pd.Series({'TP.HCM': 8993, 'Hanoi': 8053, 'Lam Dong': 1297, 'Quang Tri': 623})

'''Thêm 1 bộ dữ liệu vào bên phải của dòng theo mã là TP.HCM, Hanoi, Lam Dong, Quang Tri'''
area = pd.Series({'TP.HCM': 2061, 'Hanoi': 3359, 'Lam Dong': 9765, 'Quang Tri': 4746})

'''Tạo tiêu đề khung chứa cho dataframe của '''
data = pd.DataFrame({'Dân số': population, 'Diện tích': area})

'''In dữ liệu ra màn hình'''
print('In dữ liệu dân số diện tích ra màn hình - population theo tỉnh thành')
print(data)
print('\n\n')

'''In dữ liệu cột dân số ra màn hình'''
print('In dữ liệu cột dân số ra màn hình')
print(data['Dân số'])
print('\n\n')

'''In dữ liệu data thêm 1 cột mật độ bao gồm cột dân số / diện tích ra màn hình'''
print('In dữ liệu data thêm 1 cột mật độ bao gồm cột dân số / diện tích ra màn hình')
data['Mật độ'] = data['Dân số'] / data['Diện tích']
print(data)
print('\n\n')

'''---------------------------------------------------------------------------------------------------------------------'''
'''Indexing trong DataFrame: Tạo mảng 2 chiều với dữ liệu'''
'''Lấy hàng đầu tiên'''
print("\nDữ liệu của TP.HCM:\n ",data.iloc[0])
 
'''Lấy dữ liệu 3 hàng đầu tiên'''
print("\nDữ liệu của TP.HCM, Hà Nội và Lâm Đồng:\n ",data.iloc[:3])
 
'''Lấy dữ liệu 2 hàng và 2 cột đầu tiên'''
print("\nDữ liệu dân số và diện tích của TP.HCM và Hà Nội:\n ",data.iloc[:2, :2])
 
# '''Lấy dữ liệu tất cả các hàng và cột cuối cùng'''
print("\nMật độ dân số của các tỉnh / thành phố:\n ",data.iloc[:, -1])


















