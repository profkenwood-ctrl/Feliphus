import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Bike Sharing Analysis", layout="wide")
sns.set(style="darkgrid")

st.markdown("- Nama: Feliphus, S.Kom  \n- Email: prof.kenwood@gmail.com")


@st.cache_data
def load_data(url: str) -> pd.DataFrame:
    df = pd.read_csv(url, parse_dates=["dteday"], dayfirst=False)
    return df


DATA_URL = "https://raw.githubusercontent.com/adinurrohkhim/analisadata_pyton/main/day.csv"

tab1, tab2, tab3 = st.tabs(["FILE DATASET", "VISUALISASI", "CONCLUSION"])

with tab1:
    st.header("File dataset yang digunakan dalam analisa")
    try:
        day_df = load_data(DATA_URL)
        st.dataframe(day_df)
        st.markdown("### Metadata singkat")
        st.write(
            """
            - instant: index
            - dteday : Tanggal
            - season : musim (1=musim dingin, 2=semi, 3=panas, 4=gugur)
            - yr : tahun (0:2011, 1:2012)
            - mnth : bulan (1 to 12)
            - hr : jam (0 to 23)
            - holiday : Hari libur, 0 = tidak, 1 = libur
            - weekday : Hari dalam seminggu
            - workingday : 1 = hari kerja, 0 = libur
            - weathersit : kondisi cuaca (1..4)
            - temp, atemp, hum, windspeed, casual, registered, cnt
            """
        )
    except Exception as e:
        st.error(f"Gagal memuat data: {e}")

with tab2:
    st.header("Visualisasi: pilih sumbu X dan Y")
    # Load once (cached)
    data = load_data(DATA_URL)

    # X choices: all columns
    x_column = st.selectbox(
        "Pilih kolom untuk sumbu X",
        options=list(data.columns),
        index=list(data.columns).index("season") if "season" in data.columns else 0,
        key="x_column",
    )

    # Y choices: numeric only
    numeric_cols = data.select_dtypes(include=["number"]).columns.tolist()
    y_column = st.selectbox(
        "Pilih kolom untuk sumbu Y (numeric)", options=numeric_cols, index=numeric_cols.index("cnt") if "cnt" in numeric_cols else 0, key="y_column"
    )

    agg_method = st.selectbox("Agregasi (jika X kategorikal)", options=["sum", "mean", "median"], index=1, key="agg_method")

    if x_column and y_column:
        fig, ax = plt.subplots(figsize=(10, 5))

        # if X is non-numeric or has few uniques -> aggregate
        if data[x_column].dtype == "O" or data[x_column].nunique() <= 50:
            if agg_method == "sum":
                plot_df = data.groupby(x_column)[y_column].sum().reset_index()
            elif agg_method == "median":
                plot_df = data.groupby(x_column)[y_column].median().reset_index()
            else:
                plot_df = data.groupby(x_column)[y_column].mean().reset_index()

            # sort by y desc for readability
            plot_df = plot_df.sort_values(by=y_column, ascending=False)
            sns.barplot(data=plot_df, x=x_column, y=y_column, ax=ax)
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
        else:
            # numeric x: scatter
            sns.scatterplot(data=data, x=x_column, y=y_column, ax=ax, s=20)
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)

        st.pyplot(fig)

with tab3:
    st.header("Kesimpulan Analisa")
    st.write(
        """
        - Pertanyaan 1: Bagaimana pengaruh musim dan cuaca terhadap jumlah penyewaan sepeda?
          - Gunakan sumbu X: `season` atau `weathersit`, sumbu Y: `cnt` pada menu VISUALISASI.

        - Pertanyaan 2: Apakah hari kerja dan hari libur mempengaruhi jumlah penyewaan?
          - Gunakan sumbu X: `holiday` atau `workingday`, sumbu Y: `cnt` pada menu VISUALISASI.

        Note: Untuk variabel kategorikal kita melakukan agregasi (mean/median/sum) agar visualisasinya lebih informatif.
        """
    )
