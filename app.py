import streamlit as st
import requests
import pandas as pd

# ページ設定
st.set_page_config(
    page_title="Fruityvice API Viewer",
    page_icon="🍎",
    layout="wide"
)

st.title("🍎 Fruityvice API Viewer")
st.markdown("---")

# APIエンドポイント
API_URL = "https://www.fruityvice.com/api/fruit/all"

# データ取得関数
@st.cache_data
def fetch_fruit_data():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"APIリクエストに失敗しました: {e}")
        return []

# データ取得
data = fetch_fruit_data()

if data:
    # JSON → DataFrameに変換
    df = pd.json_normalize(data)
    
    # サイドバーで列選択
    st.sidebar.header("表示設定")
    selected_columns = st.sidebar.multiselect(
        "表示する列を選択",
        options=df.columns.tolist(),
        default=["name", "family", "genus", "order"]
    )
    
    # メイン表示
    st.subheader("📋 取得データ")
    st.dataframe(df[selected_columns])
    
    # サイドバーで検索
    st.sidebar.header("フィルター")
    keyword = st.sidebar.text_input("名前でフィルタ", "")
    
    if keyword:
        filtered_df = df[df["name"].str.contains(keyword, case=False)]
        st.subheader(f"🔍 '{keyword}' を含むデータ")
        st.dataframe(filtered_df[selected_columns])
    
    # 数値データがある場合は統計情報も表示
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
    if numeric_cols:
        st.subheader("📊 数値列の統計情報")
        st.dataframe(df[numeric_cols].describe())
else:
    st.warning("データを取得できませんでした。")
