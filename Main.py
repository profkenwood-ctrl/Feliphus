import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')
 
st.write(
    """
    # Proyek Analisis Data: Bike Sharing Dataset
- Nama : Feliphus, S.Kom
- Email: prof.kenwood@gmail.com
    """
)


tab1, tab2, tab3 = st.tabs(["FILE DATASET", "VISUALISASI", "CONCLUSION"])
 
with tab1:

    csv_url = "https://raw.githubusercontent.com/adinurrohkhim/analisadata_pyton/main/day.csv"
    st.header("File dataset yang di gunakan dalam analisa")     
    day_df=pd.read_csv(csv_url)
    st.dataframe(day_df)
    
     
    st.write(
    """
        #METADATA
    - instant: index
    - dteday : Tanggal
    - season : musim ( 1=salju, 2=semi, 3=panas, 4=gugur)
    - yr : tahun (0: 2011, 1:2012)
    - mnth : bulan( 1 to 12)
    - hr : jam (0 to 23)
    - holiday : Hari libur , 0 = tidak libur , 1 = libur
    - weekday : Hari dalam seminggu 
    - workingday : hari kerja libur = 1, kerja masuk = 0
    - weathersit : Cuaca
        1: Cerah, Sedikit awan, Berawan sebagian, Berawan sebagian
        2: Kabut + Berawan, Kabut + Awan pecah, Kabut + Sedikit awan, Kabut
        3: Salju Ringan, Hujan Ringan + Badai Petir + Awan berserakan, Hujan Ringan + Awan berserakan
        4: Hujan Lebat + Palet Es + Badai Petir + Kabut, Salju + Kabut
    - temp : Suhu normal dalam Celsius (t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (only in hourly scale)
    - atemp: Suhu dalam. The values are derived via (t-t_min)/(t_max-t_min), t_min=-16, t_max=+50 (only in hourly scale)
    - hum:  Kelembapan . The values are divided to 100 (max)
    - windspeed: Kecepatan angin
    - casual: jumlah pengguna biasa 
    - registered: jumlah pengguna terdaftar
    - cnt: jumlah total sepeda sewaan termasuk sepeda kasual dan terdaftar
        """
            )


with tab2:
    st.header("Pilihlah sumbe X dan Y") 
    def load_data(file_path):
        data = pd.read_csv(file_path)
        return data
    def create_bar_chart(data, x_column, y_column):
        fig, ax = plt.subplots()
        ax.bar(data[x_column], data[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        st.pyplot(fig)
    uploaded_file = ("https://raw.githubusercontent.com/adinurrohkhim/analisadata_pyton/main/day.csv")
    if uploaded_file is not None:
        data = load_data("https://raw.githubusercontent.com/adinurrohkhim/analisadata_pyton/main/day.csv")
        x_column = st.selectbox('Pilih kolom untuk sumbu x', data.columns)
        y_column = st.selectbox('Pilih kolom untuk sumbu y', data.columns)
        create_bar_chart(data, x_column, y_column)    

 
with tab3:
    st.header("Kesimpulan Analisa")

    st.write(
    """
    - Conclution pertanyaan 1 
    - - pertanyaan 1 = Bagaimana pengaruh musim dan cuaca terhadap jumlah pesewaan sepeda ?
    - - Pilihlah sumbu x 'season' , 'wheater'
    - - pilihlah sumbu y 'cnt ' 
    - - pada menu VISUALISASI untuk menjawab perntayaan 1
   * Jumlah pesewaan sepeda keseluruhan ( jumlah pesewa sepeda yang terdaftar maupun yg tidak terdaftar ) paling tinggi ternjadi pada musim panas yaitu sebesar 1.061.129 orang atau sekitar 32,23 % dari total keseluruhan pesewa sepeda dalam 2 tahun terahir. dan paling rendah pada musim dingin yaitu sebesar 471.348 orang. Sedangkan Untuk Kondisi cuaca Cerah, Sedikit awan, Berawan sebagian, Berawan sebagian mendapat jumlah pesewa sepeda paling tinggi yaitu sebesar 2.257.952 orang. 
   
    *** Hal ini bisa di katakan Musim dan cuaca sangat berpengaruh terhadap Pesewaan jumlah sepeda   
    
   
    - conclution pertanyaan 2
    - pertanyaan 2 = Benarkah hari kerja dan hari libur berpengaruh terhadap jumlah pesewaan sepeda ?
    - - Pilihlah sumbu x 'holiday' , 'workingday'
    - - pilihlah sumbu y 'cnt ' 
    - - pada menu VISUALISASI untuk menjawab perntayaan 2
   * Jumlah pesewaan sepeda selama weekday tidak terdapat perbedaan yang cukup signifikan. Untuk Jumlah pesewaan sepda pada liburan ( holiday ) cukup tinggi yaitu sebesar 3.214.244 orang dari pada ketika tidak libur .sedangkan untuk jumlah pesewaan sepeda per-Workday dalam kondisi libur dan mask . jumlahnya cukup signifikan dengan perbadingan jumlah ibur dibanding jumlah tidak libur sebesar 1.000.269 : 2.292.410 orang.
   
   *** Hal ini bisa di katakan Kondisi hari libur dan workday ( saat libur maupun masuk ) sangat mempengaruhi jumlah pesewaan sepeda


    """
    )