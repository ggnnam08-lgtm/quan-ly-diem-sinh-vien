import pandas as pd


def tao_bang_diem():
    # 1. Tao du lieu 10 sinh vien
    data = {
        'Ho_ten': [
            'Nguyễn Minh Anh',
            'Trần Quốc Bảo',
            'Lê Hoàng Chi',
            'Phạm Gia Huy',
            'Võ Ngọc Linh',
            'Đặng Tuấn Kiệt',
            'Bùi Khánh Vy',
            'Hoàng Đức Minh',
            'Đỗ Phương Thảo',
            'Phan Nhật Nam'
        ],
        'Chuyen_can': [9.0, 8.0, 9.5, 7.0, 8.5, 6.5, 9.2, 5.0, 7.5, 4.0],
        'Giua_ky': [8.5, 7.5, 9.0, 6.5, 8.0, 5.5, 9.5, 6.0, 8.0, 5.0],
        'Cuoi_ky': [9.2, 8.0, 8.8, 7.2, 8.6, 6.0, 9.0, 5.5, 7.8, 4.5]
    }

    df = pd.DataFrame(data)

    # 2. Tinh diem tong ket
    df['Tong_ket'] = (
        0.2 * df['Chuyen_can']
        + 0.3 * df['Giua_ky']
        + 0.5 * df['Cuoi_ky']
    )

    # 3. Xep loai
    def xep_loai(diem):
        if diem >= 8.5:
            return 'Giỏi'
        elif diem >= 7.0:
            return 'Khá'
        elif diem >= 5.0:
            return 'Trung bình'
        else:
            return 'Yếu'

    df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)
    df['Tong_ket'] = df['Tong_ket'].round(2)

    return df
