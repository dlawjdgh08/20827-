import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="국가별 MBTI Top10", layout="centered")
st.title("🌍 국가별 MBTI 유형 Top 10")

# CSV 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# 국가 선택
selected_country = st.selectbox("국가를 선택하세요", df["Country"].unique())

# 해당 국가 Top10 데이터 추출
top10_df = (
    df[df["Country"] == selected_country]
    .drop(columns=["Country"])
    .T.reset_index()
)
top10_df.columns = ["MBTI", "비율"]
top10_df = top10_df.sort_values(by="비율", ascending=False).head(10)

# Altair 바 차트
chart = (
    alt.Chart(top10_df)
    .mark_bar()
    .encode(
        x=alt.X("비율:Q", title="비율"),
        y=alt.Y("MBTI:N", sort="-x"),
        color="MBTI:N",
        tooltip=["MBTI", "비율"]
    )
    .properties(width=600, height=400, title=f"{selected_country} MBTI Top 10")
)

st.altair_chart(chart, use_container_width=True)
