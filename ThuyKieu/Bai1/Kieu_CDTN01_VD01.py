
import pandas as pdkieu
import numpy as npkieu

##Bài 1: Thống kê-Pandas

print("Bài 1: Thống kê:\n")

##Create a Dictionary of series
d = {'Name':pdkieu.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pdkieu.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pdkieu.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
#Create a DataFrame
df = pdkieu.DataFrame(d)

print("In dataframe ra màn hình:\n")
print (df)  #in dataframe ra man hinh

print("Trả về tổng các giá trị theo chiều dọc:\n")
print (df.sum())  #Trả về tổng các giá trị cho trục được yêu cầu. Mặc định trục dọc Oy=0. Do cột Name là string nên sẽ tự động bỏ qua

print("Trả về tổng các giá trị theo chiều ngang:\n")
print (df.sum(1))   #Trả về tổng các giá trị cho trục ngang Ox=1.Do trục Ox sẽ cộng cả cột Name (datatype=string nên sẽ xuất hiện warning numeric_only)

print("Trả về giá trị trung bình:\n")
print (df.mean())   #Trả về giá trị trung bình

print("In bảng tóm tắt thống kê:\n")
print (df.describe())   #Trả về một bản tóm tắt thống kê liên quan đến các cột DataFrame(Age, Rating): count, mean, std, min, max, 25%, 50%, 75%

#----------------------###----------------------#

#Bài 10: Đọc dữ liệu và kĩ thuật- reindexing - Python Pandas

print("Đọc dữ liệu và kỹ thuật reindexing:\n")

df = pdkieu.read_csv('./sales_14.csv',header=0, index_col='Date', parse_dates=True)
print("in ra 5 bản ghi đầu tiên:\n")
print (df.head())   #in ra n bản ghi đầu tiên của dataframe. Mặc định = 5 dòng.
print("\n\n")
#----------------------###----------------------#

#Bài 11: Làm việc với dữ liệu Text (P1) -Pandas

#Series trong NumPy có thể hiểu như mảng 1 chiều bao gồm cả mảng dữ liệu và một mảng chỉ mục (index) được truy cập qua 2 thuộc tính values và index. DataFrame là Series ở dạng mảng 2 chiều
#npkieu.nan  "not a number" Special values defined in numpy,if you don’t care what the original value was and cannot use equality to test

print("Làm việc với dữ liệu text:\n")

s = pdkieu.Series(['Tom', 'William Rick', 'John', 'Alber@t', npkieu.nan, '1234','SteveSmith'])

print("In dataframe ra màn hình:\n")
print (s)               #in dataframe s ra man hinh

print("Chuyển chuỗi String thành chữ thường:\n")
print (s.str.lower())   #chuyển chuỗi String thành chữ thường

print("Chuyển chuỗi String thành chữ hoa:\n")
print (s.str.upper())   #chuyển chuỗi String thành chữ in hoa

print("In độ dài chuỗi:\n")
print (s.str.len())     #Độ dài chuỗi

print("\n\n")
s = pdkieu.Series([' Tom ', ' William Rick ', 'John  ', ' Alber@t '])
#print (s)
print ("After Stripping:")
print (s.str.strip())   #Loại bỏ khoảng trắng ở đầu và cuối. Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (Mặc định là xóa khoảng trắng ở đầu và cuối)
print("\n\n")

#----------------------###----------------------#

#Bổ sung: Dataframe là Dictionary
#Từng Cột DL trong DataFrame có thể được truy cập theo kiểu dictionary bằng cách index vào tên của cột tương ứng. VD: data['Dân số']
#có thể thêm/Xóa các cặp dữ liệu bằng cách tương tự. VD: Thêm: data['Mật độ'] = data['Dân số'] / data['Diện tích']

print("Dataframe là Dictionary:\n")

population = pdkieu.Series({'TP.HCM': 8993, 'Hanoi': 8053, 'Lam Dong': 1297, 'Quang Tri': 623})
area = pdkieu.Series({'TP.HCM': 2061, 'Hanoi': 3359, 'Lam Dong': 9765, 'Quang Tri': 4746})
 
data = pdkieu.DataFrame({'Dân số': population, 'Diện tích': area})
print(data)
print("\n\n")
#----------------------###----------------------#

#Bổ sung: Indexing trong DataFrame
#sử dụng 2 thuộc tính là loc và iloc. 
#Với iloc, ta sẽ thao tác không khác gì một mảng 2 chiều trong NumPy với các hàng và cột tương ứng

print("Indexing trong DataFrame:\n")

# Lấy hàng đầu tiên
print("\nDữ liệu của TP.HCM:\n ",data.iloc[0])
 
# Lấy dữ liệu 3 hàng đầu tiên
print("\nDữ liệu của TP.HCM, Hà Nội và Lâm Đồng:\n ",data.iloc[:3])
 
# Lấy dữ liệu 2 hàng và 2 cột đầu tiên
print("\nDữ liệu dân số và diện tích của TP.HCM và Hà Nội:\n ",data.iloc[:2, :2])
 
# Lấy dữ liệu tất cả các hàng và cột cuối cùng
print("\nDiện tích của các tỉnh / thành phố:\n ",data.iloc[:, -1])
