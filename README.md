branch test

# Streamlit サンプルアプリ

このプロジェクトは、Streamlitを使用したデータ可視化とインタラクティブな分析のサンプルアプリケーションです。

## 機能

- 📊 複数のグラフタイプ（折れ線グラフ、散布図、棒グラフ、ヒートマップ）
- 📈 リアルタイムデータ可視化
- 🎯 インタラクティブなフィルタリング機能
- 📋 統計情報の表示
- 📱 レスポンシブデザイン

## ローカルでの実行

1. 依存関係をインストール:
```bash
pip install -r requirements.txt
```

2. アプリを起動:
```bash
streamlit run app.py
```

## Streamlit Cloud でのデプロイ

### 方法1: GitHub連携

1. このリポジトリをGitHubにプッシュ
2. [Streamlit Cloud](https://share.streamlit.io/) にアクセス
3. GitHubアカウントでログイン
4. "New app" をクリック
5. リポジトリを選択
6. メインファイルパスを `app.py` に設定
7. "Deploy" をクリック

### 方法2: 手動デプロイ

1. Streamlit Cloudでアプリを作成
2. ファイルをアップロード:
   - `app.py`
   - `requirements.txt`
   - `.streamlit/config.toml`

## ファイル構成

```
lifeschool-sandbox/
├── app.py                 # メインアプリケーション
├── requirements.txt       # 依存関係
├── .streamlit/
│   └── config.toml       # Streamlit設定
└── README.md             # このファイル
```

## 技術スタック

- **Streamlit**: Webアプリケーションフレームワーク
- **Pandas**: データ処理
- **NumPy**: 数値計算
- **Plotly**: インタラクティブなグラフ

## ライセンス

MIT License
