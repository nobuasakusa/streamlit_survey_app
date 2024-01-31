import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Streamlitアプリのタイトル
st.title('ワードクラウド生成器')

# ユーザー入力を受け取る
user_input = st.text_area("ここにテキストを入力してください", "")

# ワードクラウドを生成する関数
def generate_wordcloud(text):
    wordcloud = WordCloud(
        font_path='./NotoSansJP-Regular.ttf',  # Google Fontsの日本語フォントのパス
        width=800,
        height=800,
        background_color='white',
        min_font_size=10
    ).generate(text)
    return wordcloud

# ユーザー入力があればワードクラウドを表示
if user_input:
    wordcloud = generate_wordcloud(user_input)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    st.pyplot(plt)
