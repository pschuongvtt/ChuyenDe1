import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}

df = pd.DataFrame(d)
print('Câu 1: In dữ liệu ra màn hình')
print(df)
print('\n')

print('Câu 2a: Trả về tổng các giá trị')
print(df.sum())
print('\n')

print('Câu 2b: Tính tổng phần trăm')
print(df.sum(1))
print('\n')

print('Câu 3: Trả về giá trị trung bình')
print(df.mean())
print('\n')

print('Câu 4: Bảng thống kê các cột DataFrame')
print(df.describe())
print('\n')

print('Câu 5: Đọc dữ liệu và kĩ thuật reindexing - Python Pandas')
df = pd.read_csv("E:\DHSPKT\CN1\BT1/sales_14.csv",
                     header=0, index_col='Date', parse_dates=True)
print(df.head())
print('\n')

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

print('Câu 6: in ra màn hình')
print(s)

print('Câu 7: chuyển chuỗi String thành chữ thường')
print(s.str.lower())

print('Câu 8: chuyển chuỗi String thành chữ in hoa')
print(s.str.upper())

print('Câu 9: Độ dài chuỗi')
print(s.str.len())

print('Câu 10: Loại bỏ khoảng trắng')
print(s)
print("After Stripping:")
print(s.str.strip())
print('\n')

print('Câu 11: Dân số và diện tích của một số tỉnh / thành phố ở Việt Nam')
population = pd.Series({'TP.HCM': 8993, 'Hanoi': 8053, 'Lam Dong': 1297, 'Quang Tri': 623})
area = pd.Series({'TP.HCM': 2061, 'Hanoi': 3359, 'Lam Dong': 9765, 'Quang Tri': 4746})
data = pd.DataFrame({'Dân số': population, 'Diện tích': area})
print(data)
print('\n')


print('Câu 12: Bảng dân số Việt Nam')
data['Dân số']
print(data)
print('Name: Dân số, dtype: int64')
print('\n')

print('Câu 13: Bảng mật độ, dân số, diện tích Việt Nam')
data['Mật độ'] = data['Dân số'] / data['Diện tích']
data
print(data)
print('\n')

print('Câu 14: Lấy hàng đầu tiên')
print("\nDữ liệu của TP.HCM:\n ",data.iloc[0])
print('\n')

print('Câu 15: Lấy dữ liệu 3 hàng đầu tiên')
print("\nDữ liệu của TP.HCM, Hà Nội và Lâm Đồng:\n ",data.iloc[:3])
print('\n')

print('Câu 16: Lấy dữ liệu 2 hàng và 2 cột đầu tiên')
print("\nDữ liệu dân số và diện tích của TP.HCM và Hà Nội:\n ",data.iloc[:2, :2])
print('\n')

print('Câu 17: Lấy dữ liệu tất cả các hàng và cột cuối cùng')
print("\nMật độ dân số của các tỉnh / thành phố:\n ",data.iloc[:, -1])