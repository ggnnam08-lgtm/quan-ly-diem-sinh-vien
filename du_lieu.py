import pandas as pd

DATA = {'Ho_ten': ['Nguyễn Minh Anh', 'Trần Quốc Bảo', 'Lê Thị Chi', 'Phạm Gia Huy', 'Võ Ngọc Lan', 'Đặng Minh Khoa', 'Bùi Thảo My', 'Hoàng Anh Tuấn', 'Đỗ Khánh Linh', 'Phan Đức Long'], 'Chuyen_can': [9, 8, 10, 7, 9, 6, 10, 8, 7, 5], 'Giua_ky': [9, 7, 8, 6, 9, 5, 10, 8, 4, 3], 'Cuoi_ky': [9, 8, 9, 7, 10, 4, 9, 8, 5, 3]}

def xep_loai(diem):
    if diem >= 8.5:
        return 'Giỏi'
    if diem >= 7.0:
        return 'Khá'
    if diem >= 5.0:
        return 'Trung bình'
    return 'Yếu'

def tao_bang_diem():
    df = pd.DataFrame(DATA)
    df['Tong_ket'] = (df['Chuyen_can']*.2 + df['Giua_ky']*.3 + df['Cuoi_ky']*.5).round(2)
    df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)
    return df
