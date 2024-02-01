import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# アプリのタイトルを設定
st.title("アンケート結果リアルタイム集計アプリ")

# データを格納するデータフレームを作成 (最大20行)
max_responses = 20
data = pd.DataFrame(columns=["名前", "達成度"])

# 質問と選択肢を表示
st.header("アンケート質問")
st.write("名前と達成度を選択してください。")

# 名前の入力欄
name = st.text_input("名前を入力してください:")

# 達成度の選択肢
achievement = st.selectbox("達成度を選択してください:", ["1", "2", "3", "4", "5"])

# 登録ボタンをクリックしたときの処理
if st.button("登録"):
    if name and achievement:
        if len(data) < max_responses:
            data = data.append({"名前": name, "達成度": int(achievement)}, ignore_index=True)
            st.success("データが正常に登録されました。")
        else:
            st.error("最大回答数に達しました。データを追加できません。")

# リセットボタンを追加してデータをクリア
if st.button("リセット"):
    data = pd.DataFrame(columns=["名前", "達成度"])
    st.success("データがリセットされました。")

# 集計結果を表示
st.header("集計結果")

# 達成度ごとのカウントを計算
count_by_achievement = data["達成度"].value_counts().sort_index()

# 達成度の名称と割合を計算
total_responses = len(data)
percentage_by_achievement = count_by_achievement / total_responses * 100

# 集計結果をデータフレームにまとめる
result_df = pd.DataFrame({
    "達成度": count_by_achievement.index,
    "回答数": count_by_achievement.values,
    "割合": percentage_by_achievement.values
})

# 集計結果を表示
st.write(result_df)

# バーグラフで集計結果を可視化
st.bar_chart(result_df.set_index("達成度")["割合"])

# フッター
st.write("最大回答数: 20人まで")
