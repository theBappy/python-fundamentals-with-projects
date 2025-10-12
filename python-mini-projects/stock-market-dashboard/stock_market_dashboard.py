# Stock Market Dashboard (2025 Fixed Version)
# ---------------------------------------------------
# Features:
# - Real-time data from Yahoo Finance
# - Bollinger Bands, MACD, RSI indicators
# - Dynamic selection by Sector and Company
#
# To Run:
# 1️⃣ pip install streamlit pandas yfinance ta
# 2️⃣ streamlit run stock_market_dashboard.py
# ---------------------------------------------------

import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator

st.set_page_config(page_title="Stock Market Dashboard", layout="wide")

# --- Load S&P 500 Company Data ---
@st.cache_data
def load_data():
    # Use an updated and reliable CSV dataset
    url = "https://datahub.io/core/s-and-p-500-companies-financials/r/constituents.csv"
    df = pd.read_csv(url)
    df.rename(columns={"Symbol": "Ticker", "Name": "Security", "Sector": "GICS Sector"}, inplace=True)
    return df

# --- Download Stock Data ---
@st.cache_data
def download_stock_data(ticker: str, start: datetime.date, end: datetime.date):
    data = yf.download(ticker, start=start, end=end, progress=False)
    return data

# --- Load Data ---
df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("Filter Options")
sorted_sector_unique = sorted(df["GICS Sector"].unique())
selected_sector = st.sidebar.multiselect("Select Sector(s)", sorted_sector_unique)
today = datetime.date.today()
before = today - datetime.timedelta(days=700)
start_date = st.sidebar.date_input("Start Date", before)
end_date = st.sidebar.date_input("End Date", today)

# --- Validation ---
if start_date >= end_date:
    st.sidebar.error("Error: End date must be after Start date.")

# --- Default View ---
if len(selected_sector) == 0:
    st.title("📊 Stock Market Dashboard (S&P 500)")
    st.write(
        """
        This dashboard visualizes **S&P 500** company stocks with key technical indicators:
        - **Bollinger Bands**
        - **MACD (Moving Average Convergence Divergence)**
        - **RSI (Relative Strength Index)**  
        Use the sidebar to select a sector and a company ticker.
        """
    )
    st.info("Select a sector from the sidebar to begin.")
else:
    df_selected_sector = df[df["GICS Sector"].isin(selected_sector)]
    st.title("🧭 Display Companies in Selected Sector(s)")
    for s in selected_sector:
        st.subheader(s)

    option = st.selectbox("Select Company Ticker:", df_selected_sector["Ticker"])
    company = df_selected_sector[df_selected_sector["Ticker"] == option]["Security"].values[0]

    st.markdown(f"### 📈 {company} ({option})")

    # --- Stock Data ---
    stock_data = download_stock_data(option, start_date, end_date)

    if stock_data.empty:
        st.warning("⚠️ No stock data found for this date range.")
    else:
        # --- Indicators ---
        indicator_bb = BollingerBands(stock_data["Close"])
        bb = stock_data.copy()
        bb["Upper Band"] = indicator_bb.bollinger_hband()
        bb["Lower Band"] = indicator_bb.bollinger_lband()

        macd = MACD(stock_data["Close"]).macd()
        rsi = RSIIndicator(stock_data["Close"]).rsi()

        # --- Display Charts ---
        st.subheader("Bollinger Bands")
        st.line_chart(bb[["Close", "Upper Band", "Lower Band"]])

        st.subheader("MACD (Moving Average Convergence Divergence)")
        st.area_chart(macd)

        st.subheader("RSI (Relative Strength Index)")
        st.line_chart(rsi)

        # --- Recent Data ---
        st.subheader("Recent 10-Day Data")
        st.dataframe(stock_data.tail(10))

        # --- Company Info ---
        ticker_data = yf.Ticker(option)
        info = ticker_data.info

        logo_url = info.get("logo_url")
        long_name = info.get("longName", company)
        summary = info.get("longBusinessSummary", "Business summary not available.")

        if logo_url:
            st.image(logo_url, width=100)
        st.markdown(f"**Company:** {long_name}")
        st.markdown(f"**Sector:** {info.get('sector', 'N/A')}")
        st.markdown(f"**Country:** {info.get('country', 'N/A')}")
        st.markdown(f"**Industry:** {info.get('industry', 'N/A')}")
        st.markdown(f"**Website:** [{info.get('website', '')}]({info.get('website', '')})")
        st.write(summary)
