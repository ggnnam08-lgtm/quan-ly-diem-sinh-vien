# Web App Streamlit: Quản lý điểm sinh viên
import streamlit as st
import matplotlib.pyplot as plt
from du_lieu import tao_bang_diem
st.set_page_config(page_title='Quản lý điểm sinh viên', page_icon='🎓', layout='wide')
st.title('QUẢN LÝ ĐIỂM SINH VIÊN')
st.caption('Dữ liệu minh họa của 10 sinh viên | Thang điểm 10')
df = tao_bang_diem()

st.subheader('1. Bảng điểm sinh viên')
st.dataframe(df.rename(columns={
    'Ho_ten': 'Họ tên', 'Chuyen_can': 'Chuyên cần', 'Giua_ky': 'Giữa kỳ',
    'Cuoi_ky': 'Cuối kỳ', 'Tong_ket': 'Tổng kết', 'Xep_loai': 'Xếp loại'
}), use_container_width=True, hide_index=True)

st.subheader('2. Thống kê lớp')
cao = df.loc[df['Tong_ket'].idxmax()]
thap = df.loc[df['Tong_ket'].idxmin()]
so_dat = int((df['Tong_ket'] >= 5).sum())
c1,c2,c3,c4 = st.columns(4)
c1.metric('Điểm trung bình', f"{df['Tong_ket'].mean():.2f}")
c2.metric('Điểm cao nhất', f"{cao['Tong_ket']:.2f}")
c2.caption(cao['Ho_ten'])
c3.metric('Điểm thấp nhất', f"{thap['Tong_ket']:.2f}")
c3.caption(thap['Ho_ten'])
c4.metric('Số sinh viên đạt', f'{so_dat}/{len(df)}')

st.subheader('3. Tra cứu điểm sinh viên')
ten = st.selectbox('Chọn một sinh viên', df['Ho_ten'].tolist())
sv = df.loc[df['Ho_ten'] == ten].iloc[0]
st.write(f"**Chuyên cần:** {sv['Chuyen_can']:.2f} | **Giữa kỳ:** {sv['Giua_ky']:.2f} | **Cuối kỳ:** {sv['Cuoi_ky']:.2f}")
st.write(f"**Điểm tổng kết:** {sv['Tong_ket']:.2f} | **Xếp loại:** {sv['Xep_loai']}")

st.subheader('4. Biểu đồ điểm tổng kết')
fig, ax = plt.subplots(figsize=(12,5.5))
bars = ax.bar(df['Ho_ten'], df['Tong_ket'], color='#3979b8')
ax.set_title('Điểm tổng kết của 10 sinh viên')
ax.set_xlabel('Họ và tên sinh viên')
ax.set_ylabel('Điểm tổng kết (thang 10)')
ax.set_ylim(0,10.5)
ax.tick_params(axis='x', rotation=35)
for lab in ax.get_xticklabels(): lab.set_horizontalalignment('right')
for bar in bars:
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.12,
            f'{bar.get_height():.2f}', ha='center', fontsize=8)
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.divider()
st.markdown('<p style="font-size:12px;color:gray">Người thực hiện: [ĐIỀN HỌ TÊN] | MSSV: [ĐIỀN MSSV]</p>', unsafe_allow_html=True)
