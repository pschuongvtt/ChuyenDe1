# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np


## Cau 1
# =============================================================================
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#     'Lee','David','Gasper','Betina','Andres']),
#     'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#     'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }
# 
# 
# df = pd.DataFrame(d)
# print (df)
# =============================================================================



## Cau 2
# =============================================================================
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#     'Lee','David','Gasper','Betina','Andres']),
#     'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#     'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }
# 
# 
# df = pd.DataFrame(d)
# print (df.sum())
# =============================================================================



## Cau 3
# =============================================================================
# 
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#     'Lee','David','Gasper','Betina','Andres']),
#     'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#     'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }
#   
# 
# df = pd.DataFrame(d)
# print (df.sum(1))
# 
# =============================================================================


## Cau 4
# =============================================================================
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#     'Lee','David','Gasper','Betina','Andres']),
#     'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#     'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }
# 
# 
# df = pd.DataFrame(d)
# print (df.mean())
# 
# =============================================================================




## Cau 5
# =============================================================================
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#     'Lee','David','Gasper','Betina','Andres']),
#     'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#     'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }
# df = pd.DataFrame(d)
# print (df.describe())
# 
# =============================================================================

## Bài 10: Đọc dữ liệu và kĩ thuật reindexing - Python Pandas

# =============================================================================
# 
# df = pd.read_csv('sales_14.csv',header=0, index_col='Date', parse_dates=True)
# 
# print (df.head())
# 
# 
# =============================================================================

## Bai 11
# =============================================================================
# s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
# print(s)
# =============================================================================


# =============================================================================
# s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
# print (s.str.lower())
# =============================================================================


# =============================================================================
# s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
# print (s.str.upper())
# =============================================================================

# =============================================================================
# s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
# print (s.str.len())
# 
# =============================================================================


# =============================================================================
# s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
# print (s)
# print ("After Stripping:")
# print (s.str.strip())
# =============================================================================


## a. DataFrame là Dictionary
## DataFrame chứa các Series là dữ liệu dân số và diện tích của một số tỉnh / thành phố ở Việt Nam sau:


population = pd.Series({'TP.HCM': 8993, 'Hanoi': 8053, 'Lam Dong': 1297, 'Quang Tri': 623})
area = pd.Series({'TP.HCM': 2061, 'Hanoi': 3359, 'Lam Dong': 9765, 'Quang Tri': 4746})
data = pd.DataFrame({'Dân số': population, 'Diện tích': area})

# =============================================================================
# print(data)
# =============================================================================



## Từng Series trong DataFrame có thể được truy cập theo kiểu dictionary bằng cách index vào tên của cột tương ứng:
# =============================================================================
# print(data['Dân số'])
# =============================================================================


## Và ta cũng có thể thêm các cặp dữ liệu mới bằng cách tương tự như Series:
# =============================================================================
# data['Mật độ'] = data['Dân số'] / data['Diện tích']
# print(data)
# =============================================================================

## c. Indexing trong DataFrame

print(data)

# Lấy hàng đầu tiên
# =============================================================================
# print("\nDữ liệu của TP.HCM:\n ",data.iloc[0])
# =============================================================================



# =============================================================================
# # Lấy dữ liệu 3 hàng đầu tiên
# print("\nDữ liệu của TP.HCM, Hà Nội và Lâm Đồng:\n ",data.iloc[:3])
# =============================================================================



# =============================================================================
# # Lấy dữ liệu 2 hàng và 2 cột đầu tiên
# print("\nDữ liệu dân số và diện tích của TP.HCM và Hà Nội:\n ",data.iloc[:2, :2])
# =============================================================================




# Lấy dữ liệu tất cả các hàng và cột cuối cùng
# =============================================================================
# print("\nMật độ dân số của các tỉnh / thành phố:\n ",data.iloc[:, -1])
# =============================================================================






















