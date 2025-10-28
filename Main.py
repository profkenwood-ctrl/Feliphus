# Main.py
import pandas as pd
import plotly.express as px
import streamlit as st

# === CONFIG ===
st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# === FUNGSI BACA DATA ===
@st.cache_data
def get_data_from_excel():
    try:
        df = pd.read_excel(
            "supermarkt_sales.xlsx",
            engine="openpyxl",
            sheet_name="Sales",
            skiprows=3,
            usecols="B:R",
            nrows=1000
        )
        # Tambah kolom jam
        df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S", errors="coerce").dt.hour
        return df
    except FileNotFoundError:
        st.error("File 'supermarkt_sales.xlsx' tidak ditemukan! Letakkan di folder yang sama dengan Main.py")
        st.stop()
    except Exception as e:
        st.error(f"Error: {e}")
        st.stop()

# === LOAD DATA ===
df = get_data_from_excel()

# === CEK KOLOM YANG DIPERLUKAN ===
required_cols = ["City", "Customer type", "Gender", "Total", "Rating", "Time", "Product line"]
missing_cols = [col for col in required_cols if col not in df.columns]
if missing_cols:
    st.error(f"Kolom berikut tidak ditemukan: {missing_cols}")
    st.stop()

# === SIDEBAR FILTER ===
st.sidebar.header("Filter Data:")

city = st.sidebar.multiselect("Pilih Kota:", options=df["City"].unique(), default=df["City"].unique())
customer_type = st.sidebar.multiselect("Pilih Tipe Pelanggan:", options=df["Customer type"].unique(), default=df["Customer type"].unique())
gender = st.sidebar.multiselect("Pilih Gender:", options=df["Gender"].unique(), default=df["Gender"].unique())

# === FILTER DATA ===
df_selection = df[
    (df["City"].isin(city)) &
    (df["Customer type"].isin(customer_type)) &
    (df["Gender"].isin(gender))
]

# === MAIN PAGE ===
st.title("📊 Sales Dashboard")
st.markdown("##")

# === KPI ===
total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(), 1)
star_rating = "⭐" * int(round(average_rating, 0))
average_sale = round(df_selection["Total"].mean(), 2)

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Total Penjualan")
    st.subheader(f"US $ {total_sales:,}")
with col2:
    st.subheader("Rata-rata Rating")
    st.subheader(f"{average_rating} {star_rating}")
with col3:
    st.subheader("Rata-rata Transaksi")
    st.subheader(f"US $ {average_sale}")

st.markdown("---")

# === CHART 1: Sales by Product Line ===
sales_by_product = df_selection.groupby("Product line", as_index=False)["Total"].sum().sort_values("Total")

fig1 = px.bar(
    sales_by_product,
    x="Total", y="Product line",
    orientation="h",
    title="<b>Penjualan per Kategori Produk</b>",
    color_discrete_sequence=["#205295"],
    template="plotly_white"
)
fig1.update_layout(plot_bgcolor="rgba(0,0,0,0)", xaxis=dict(showgrid=False))

# === CHART 2: Sales by Hour ===
sales_by_hour = df_selection.groupby("hour", as_index=False)["Total"].sum()

fig2 = px.bar(
    sales_by_hour,
    x="hour", y="Total",
    title="<b>Penjualan per Jam</b>",
    color_discrete_sequence=["#205295"],
    template="plotly_white"
)
fig2.update_layout(xaxis=dict(tickmode="linear"), plot_bgcolor="rgba(0,0,0,0)", yaxis=dict(showgrid=False))

# === TAMPILKAN CHART ===
col1, col2 = st.columns(2)
col1.plotly_chart(fig1, use_container_width=True)
col2.plotly_chart(fig2, use_container_width=True)

# === HIDE STREAMLIT STYLE ===
st.markdown("""
<style>
    #MainMenu, header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)