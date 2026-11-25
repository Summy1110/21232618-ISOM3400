import streamlit as st
import pandas as pd

st.set_page_config(page_title="Submission Template", layout="wide")

st.title("📝 Assignment Submission")

# ==========================================
# Task 1
# ==========================================
st.header("Task 1: Build a stock dashboard with sidebar controls")


# Starter code
ticker_info = pd.read_csv("https://raw.githubusercontent.com/justinjiajia/datafiles/refs/heads/main/ticker_info.csv")

# extract S&P 100 tickers from ticker_info
ticker_list = list(ticker_info.Ticker.unique())

# Load the stock data
stock_data = pd.read_csv(
    "https://github.com/justinjiajia/datafiles/raw/refs/heads/main/stock_data_yf.csv", 
    parse_dates=['Date']
)

 
 

st.info("Write your Task 1 code below ...")

# --- STUDENT CODE AREA START ---
st.sidebar.header("Dashboard Controls")

# 1. Checkbox to toggle Market Cap by Sector chart (checked by default)
show_market_cap = st.sidebar.checkbox("Show Market Cap by Sector", value=True)

# 2. Multiselect for tickers (default: TSLA, NVDA, AAPL)
default_tickers = [t for t in ["TSLA", "NVDA", "AAPL"] if t in ticker_list]
selected_tickers = st.sidebar.multiselect(
    "Select Companies",
    options=ticker_list,
    default=default_tickers,
)

# 3. Slider for year range (2020 to 2025, default: 2024 to 2025)
selected_years = st.sidebar.slider(
    "Select Year Range",
    min_value=2020,
    max_value=2025,
    value=(2024, 2025),
)

st.subheader("S&P 100 Stock Dashboard 📊")

# Market Cap by Sector bar chart
if show_market_cap:
    st.subheader("Market Cap by Sector")
    sector_df = (
        ticker_info.groupby(["Sector", "Ticker"], as_index=False)["Market Cap (B)"]
        .sum()
    )
    # Pivot or pass wide/long format to st.bar_chart
    market_cap_pivot = sector_df.pivot(
        index="Sector", columns="Ticker", values="Market Cap (B)"
    ).fillna(0)
    st.bar_chart(market_cap_pivot)

# Stock trend analysis charts
st.subheader(f"Stock Trend Analysis ({selected_years[0]} - {selected_years[1]})")

if not selected_tickers:
    st.error("Please select at least one stock!")
else:
    filtered_df = stock_data.query(
        f"Date <= '{selected_years[1]}-12-31' and Date >= '{selected_years[0]}-01-01' and Ticker in {selected_tickers}"
    )

    if filtered_df.empty:
        st.warning("No stock data available for the selected companies and year range.")
    else:
        st.markdown("### Closing Prices")
        close_chart_df = filtered_df.pivot(
            index="Date", columns="Ticker", values="Close"
        ).sort_index()
        st.line_chart(close_chart_df)

        st.markdown("### Trading Volume")
        volume_chart_df = filtered_df.pivot(
            index="Date", columns="Ticker", values="Volume"
        ).sort_index()
        st.bar_chart(volume_chart_df)
# --- STUDENT CODE AREA ---


st.divider()

# ==========================================
# Task 2
# ==========================================

st.header("Task 2: Display a video based on user input")

st.info("Write your Task 2 code below ...")

# --- STUDENT CODE AREA START ---

 




# --- STUDENT CODE AREA END ---
