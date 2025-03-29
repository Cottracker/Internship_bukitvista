import streamlit as st
import pandas as pd
import numpy as np

# Judul Dashboard
st.title('Destinasi Penginapan Bukitvista')

# Fungsi untuk mengunggah dan memproses CSV
def load_data():
    uploaded_file = st.file_uploader("Pilih file CSV", type="csv")
    if uploaded_file is not None:
        # Membaca CSV
        df = pd.read_csv(uploaded_file)
        st.write("Data yang Diupload:")
        st.dataframe(df)  # Menampilkan DataFrame yang telah di-upload
        return df
    return None

# Menggunakan fungsi untuk memuat data
df = load_data()

if df is not None:
    # Menambahkan opsi filter berdasarkan kolom di CSV
    st.sidebar.header("Pilih Filter")

    # Menampilkan nama kolom yang ada di CSV
    columns = df.columns.tolist()

    # Memilih kolom untuk filter
    column_filter = st.sidebar.selectbox("Pilih Kolom untuk Filter", columns)
    unique_values = df[column_filter].unique().tolist()
    
    # Memilih nilai untuk filter
    value_filter = st.sidebar.selectbox(f"Pilih nilai untuk {column_filter}", unique_values)

    # Melakukan filter berdasarkan kolom yang dipilih
    filtered_df = df[df[column_filter] == value_filter]

    # Menampilkan data yang telah difilter
    st.write("Data yang Telah Difilter:")
    st.dataframe(filtered_df)

    # Input jumlah orang yang akan melakukan booking
jumlah_orang = st.number_input("Jumlah Orang", min_value=1, max_value=10, value=1)
# Input waktu booking (jam)
jam_booking = st.selectbox("Pilih Waktu Booking", ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"])

st.write(f"Jumlah orang: {jumlah_orang}")
st.write(f"Waktu booking: {jam_booking}")

# Tombol untuk melakukan pemesanan
if st.button("Dapatkan Penawaran"):
    st.success(f"Check your email, Penawaran berhasil dikirim untuk {jumlah_orang} orang pada pukul {jam_booking}")