import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("/workspaces/Nabila-Projek/data_siap (1).csv")

# membuat bar navigasi
nav_options = ["beranda","Bulan", "Weathersit", "Tambahan"]
nav_choice = st.sidebar.selectbox("Pilih Analisis", nav_options)

#membuat halaman beranda
if nav_choice == "beranda":

                st.title("Analisis Data Pengguna Sepeda")
                st.write("Selamat datang di analisis data pengguna sepeda!")
                st.write("Pilih jenis data analisis yang anda inginkan .")
                st.image("naik_sepeda.jpg", use_column_width=True)  
                st.header("Pencarian Data jumlah pelanggan")
                st.header("Filter Data yang diinginkan")
                bulan_filter = st.selectbox("Pilih Bulan", df["mnth"].unique())
                tahun_filter = st.selectbox("Pilih Tahun", df["yr"].unique())
                cuaca_filter = st.selectbox("Pilih Cuaca", df["weathersit"].unique())
                df_filtered = df[(df["mnth"] == bulan_filter) & (df["yr"] == tahun_filter) & (df["weathersit"] == cuaca_filter)]
                st.write("jumlahData yang sesuai:")
                sum_cnt = df_filtered["cnt"].sum()
                sum_casual = df_filtered["casual"].sum()
                sum_registered = df_filtered["registered"].sum()
                st.write("Data yang difilter:")
                st.write(df_filtered[["cnt", "casual", "registered"]])
                st.write("Total Penyewa:", sum_cnt)
                st.write("Total Casual:", sum_casual)
                st.write("Total Registered:", sum_registered)


        

elif nav_choice == "Bulan":
            # Membuat kolom baru untuk tanggal
            df['dteday'] = pd.to_datetime(df['dteday'])
            df['weekday'] = df['dteday'].dt.day_name()
            df['mnth'] = df['dteday'].dt.month_name()
            df['yr'] = df['dteday'].dt.year

            # Membuat dashboard
            st.title("Analisis Data Pengguna Sepeda")
            st.write (df)

            # Pertanyaan 1: Bagaimana performa pengguna jasa sewa sepeda tiap bulannya?
            plt.style.use('dark_background')
            st.header("Performa Pengguna Jasa Sewa Sepeda Tiap Bulannya")
            st.write("Grafik persewaan sepeda tiap bulannya pada tahun 2011-2012")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.lineplot(x="dteday", y="cnt", data=df, color='blue')
            ax.set_xlabel("Tanggal")
            ax.set_ylabel("Total Penyewa")
            ax.set_title("Grafik Persewaan Sepeda Tiap Bulannya pada Tahun 2011-2012")
            ax.set_facecolor('black')  
            ax.grid(color='white')  
            ax.tick_params(axis='x', colors='white')  
            ax.tick_params(axis='y', colors='red')  
            ax.spines['bottom'].set_color('yellow') 
            ax.spines['top'].set_color('white') 
            ax.spines['right'].set_color('yellow') 
            ax.spines['left'].set_color('yellow')
            st.pyplot(fig)


            # Tabel data bulan
            mean_df = df.groupby(by="mnth").agg({
                "mnth": "nunique",
                "cnt": ["mean", "std", "max", "min"]
            })
            mean_df = mean_df.reset_index()
            mean_df.columns = ["_".join(col) for col in mean_df.columns.values]

            # Grafik rata-rata pengguna sepeda tiap bulannya
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.lineplot(x=mean_df.index, y=mean_df["cnt_mean"], color='blue')
            sns.lineplot(x=mean_df.index, y=mean_df["cnt_std"], color='red')
            sns.lineplot(x=mean_df.index, y=mean_df["cnt_max"], color='green')
            sns.lineplot(x=mean_df.index, y=mean_df["cnt_min"], color='yellow')
            ax.set_xlabel("Bulan")
            ax.set_ylabel("Total Penyewa")
            ax.set_title("Grafik Rata-Rata Pengguna Sepeda Tiap Bulannya")
            st.pyplot(fig)



            # Data urut terbanyak penyewa berdasarkan bulan
            st.write("Data Urut Terbanyak Penyewa Berdasarkan Bulan")
            st.write(df.groupby(by="mnth").nunique().sort_values(by='cnt', ascending=False))

            # Data urut terkecil penyewa berdasarkan bulan
            st.write("Data Urut Terkecil Penyewa Berdasarkan Bulan")
            st.write(df.groupby(by="mnth").nunique().sort_values(by='cnt', ascending=True))

elif nav_choice == "Weathersit":
            # Pertanyaan 2: Bagaimana cuaca mempengaruhi kondisi perjalanan dan pengalaman pengguna saat bersepeda?
            plt.style.use('dark_background')
            st.header("Cuaca dan Pengguna Sepeda")
            st.write("Grafik persewaan sepeda berdasarkan cuaca")
            fig, ax = plt.subplots(figsize=(20, 10))
            sns.barplot(x="weathersit", y="cnt", data=df, color='blue')
            ax.set_xlabel("wcuaca")
            ax.set_ylabel("Total Penyewa")
            ax.set_title("Grafik Persewaan Sepeda Berdasarkan Cuaca")
            st.pyplot(fig)

            # Data urut terbanyak penyewa berdasarkan weathersit
            st.write("Data Urut Terbanyak Penyewa Berdasarkan Cuaca")
            st.write(df.groupby(by="weathersit").nunique().sort_values(by='cnt', ascending=False))

            # Data urut terkecil penyewa berdasarkan weathersit
            st.write("Data Urut Terkecil Penyewa Berdasarkan Cuaca")
            st.write(df.groupby(by="weathersit").nunique().sort_values(by='cnt', ascending=True))

elif nav_choice == "Tambahan":
            st.header("Analisis Data")
            st.write(df)
            
            # menampilkan data berdasarkan yr, mnth, season, weathersit, hum, temp, atemp, dan windspeed
            st.write("Data Berdasarkan Tahun (yr):")
            st.write(df.groupby('yr')[['cnt', 'registered', 'casual']].sum())

            st.write("Data Berdasarkan Bulan (mnth):")
            st.write(df.groupby('mnth')[['cnt', 'registered', 'casual']].sum())

            st.write("Data Berdasarkan Musim (season):")
            st.write(df.groupby('season')[['cnt', 'registered', 'casual']].sum())

            st.write("Data Berdasarkan Cuaca (weathersit):")
            st.write(df.groupby('weathersit')[['cnt', 'registered', 'casual']].sum())

            st.write("Data Berdasarkan Kelembaban (hum):")
            st.write(df.groupby('hum')[['cnt', 'registered', 'casual']].sum())

            st.write("Data Berdasarkan Suhu (temp):")
            st.write(df.groupby('temp')[['cnt', 'registered', 'casual']].sum())

            st.write("Data Berdasarkan Suhu Terasa (atemp):")
            st.write(df.groupby('atemp')[['cnt', 'registered', 'casual']].sum())

            st.write("Data Berdasarkan Kecepatan Angin (windspeed):")
            st.write(df.groupby('windspeed')[['cnt', 'registered', 'casual']].sum())
