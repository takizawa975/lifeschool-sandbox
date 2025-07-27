import streamlit as st
import pandas as pd
import numpy as np

# plotlyのインポートを試行
try:
    import plotly.express as px
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError:
    st.error("⚠️ plotlyライブラリが見つかりません。以下のコマンドでインストールしてください：")
    st.code("pip install plotly")
    PLOTLY_AVAILABLE = False

# ページ設定
st.set_page_config(
    page_title="Streamlit サンプルアプリ",
    page_icon="📊",
    layout="wide"
)

# タイトル
st.title("📊 Streamlit サンプルアプリ")
st.markdown("---")

# サイドバー
st.sidebar.header("設定")
chart_type = st.sidebar.selectbox(
    "グラフの種類を選択",
    ["折れ線グラフ", "散布図", "棒グラフ", "ヒートマップ"]
)

# データ生成
@st.cache_data
def generate_data():
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', periods=100, freq='D')
    data = pd.DataFrame({
        '日付': dates,
        '売上': np.random.normal(1000, 200, 100).cumsum(),
        '顧客数': np.random.poisson(50, 100),
        '満足度': np.random.uniform(3.5, 5.0, 100)
    })
    return data

data = generate_data()

# メインコンテンツ
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📈 データ可視化")
    
    if not PLOTLY_AVAILABLE:
        st.warning("plotlyが利用できないため、データテーブルを表示します。")
        st.dataframe(data)
    else:
        if chart_type == "折れ線グラフ":
            fig = px.line(data, x='日付', y='売上', title='売上推移')
            st.plotly_chart(fig, use_container_width=True)
            
        elif chart_type == "散布図":
            fig = px.scatter(data, x='顧客数', y='売上', 
                            color='満足度', title='顧客数と売上の関係')
            st.plotly_chart(fig, use_container_width=True)
            
        elif chart_type == "棒グラフ":
            # 月別データに変換
            monthly_data = data.set_index('日付').resample('M').mean()
            fig = px.bar(monthly_data, y='売上', title='月別平均売上')
            st.plotly_chart(fig, use_container_width=True)
            
        elif chart_type == "ヒートマップ":
            # 相関行列のヒートマップ
            corr_matrix = data[['売上', '顧客数', '満足度']].corr()
            fig = px.imshow(corr_matrix, 
                           title='相関行列',
                           color_continuous_scale='RdBu')
            st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📊 統計情報")
    
    # 基本統計
    st.metric("総売上", f"¥{data['売上'].iloc[-1]:,.0f}")
    st.metric("平均顧客数", f"{data['顧客数'].mean():.1f}")
    st.metric("平均満足度", f"{data['満足度'].mean():.2f}")
    
    # データテーブル
    st.subheader("📋 最新データ")
    st.dataframe(data.tail(10))

# インタラクティブな要素
st.markdown("---")
st.subheader("🎯 フィルタリング")

# 日付範囲選択
date_range = st.date_input(
    "日付範囲を選択",
    value=(data['日付'].min().date(), data['日付'].max().date()),
    min_value=data['日付'].min().date(),
    max_value=data['日付'].max().date()
)

# フィルタリングされたデータ
filtered_data = data[
    (data['日付'].dt.date >= date_range[0]) &
    (data['日付'].dt.date <= date_range[1])
]

if len(filtered_data) > 0:
    st.write(f"選択期�