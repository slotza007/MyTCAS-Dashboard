import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===== โหลดข้อมูล =====
df = pd.read_excel("engineering_ai_programs_full.xlsx")

# ===== ทำความสะอาดค่าเทอมให้เป็นตัวเลข =====
def extract_fee(x):
    try:
        num = ''.join(c for c in x if c.isdigit() or c == ',')
        return int(num.replace(',', ''))
    except:
        return np.nan

df['ค่าเทอม (บาท)'] = df['ค่าเทอม'].apply(extract_fee)

# ===== Header =====
st.title("📊 Dashboard หลักสูตร AI และ คอมพิวเตอร์ วิศวกรรมในไทย")
st.markdown("ข้อมูลจากมหาวิทยาลัยต่างๆ ที่เปิดสอนหลักสูตรด้าน AI และวิศวกรรมคอมพิวเตอร์")

# ===== Summary Cards =====
col1, col2, col3 = st.columns(3)
col1.metric("🎓 จำนวนหลักสูตร", f"{df.shape[0]}")
col2.metric("🏫 จำนวนมหาวิทยาลัย", f"{df['มหาวิทยาลัย'].nunique()}")
col3.metric("💸 ค่าเทอมเฉลี่ย", f"{df['ค่าเทอม (บาท)'].mean():,.0f} บาท")

# ===== Filters =====
with st.sidebar:
    st.header("🔍 ตัวกรอง")
    univ_options = df["มหาวิทยาลัย"].unique()
    selected_univ = st.multiselect("เลือกมหาวิทยาลัย", options=univ_options, default=univ_options)
    df = df[df["มหาวิทยาลัย"].isin(selected_univ)]

# ===== กราฟแบบเลือกได้ =====
st.subheader("📈 เปรียบเทียบจำนวนหลักสูตรต่อมหาวิทยาลัย")
chart_type = st.selectbox("เลือกประเภทกราฟ", ["Bar Chart", "Pie Chart", "Line Chart"], key="course_chart")

course_count = df["มหาวิทยาลัย"].value_counts()

if chart_type == "Bar Chart":
    st.bar_chart(course_count)
elif chart_type == "Pie Chart":
    fig1, ax1 = plt.subplots()
    ax1.pie(course_count, labels=course_count.index, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)
elif chart_type == "Line Chart":
    st.line_chart(course_count)

# ===== ค่าเทอมเฉลี่ย =====
st.subheader("💵 เปรียบเทียบค่าเทอมเฉลี่ย")
chart_type2 = st.selectbox("เลือกประเภทกราฟค่าเทอม", ["Bar Chart", "Pie Chart"], key="fee_chart")

fee_avg = df.groupby("มหาวิทยาลัย")["ค่าเทอม (บาท)"].mean().sort_values()

if chart_type2 == "Bar Chart":
    st.bar_chart(fee_avg)
elif chart_type2 == "Pie Chart":
    fig2, ax2 = plt.subplots()
    ax2.pie(fee_avg, labels=fee_avg.index, autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')
    st.pyplot(fig2)

# ===== ตารางข้อมูล =====
st.subheader("📋 รายละเอียดหลักสูตร")
st.dataframe(df[["มหาวิทยาลัย", "หลักสูตร", "ค่าเทอม"]])
