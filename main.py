import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 제목
st.title("🌏 Global MBTI Distribution & Correlation Dashboard")

# 파일 업로드
dist_file = st.file_uploader("Upload MBTI Distribution CSV", type=["csv"])
corr_file = st.file_uploader("Upload MBTI Correlation CSV", type=["csv"])

if dist_file is not None:
    df_dist = pd.read_csv(dist_file)
    st.subheader("MBTI Type Distribution")
    st.dataframe(df_dist)

    # 막대그래프
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(df_dist["MBTI"], df_dist["AvgPercentAcrossCountries"], color="skyblue", edgecolor="black")
    ax.set_xlabel("MBTI Type")
    ax.set_ylabel("Average % Across Countries")
    ax.set_title("Global MBTI Distribution")
    plt.xticks(rotation=45)
    st.pyplot(fig)

if corr_file is not None:
    df_corr = pd.read_csv(corr_file, index_col=0)
    st.subheader("MBTI Type Correlation Matrix")
    st.dataframe(df_corr)

    # 히트맵 (matplotlib으로 직접 그림)
    fig, ax = plt.subplots(figsize=(8, 6))
    cax = ax.matshow(df_corr, cmap="coolwarm")
    fig.colorbar(cax)
    ax.set_xticks(range(len(df_corr.columns)))
    ax.set_yticks(range(len(df_corr.index)))
    ax.set_xticklabels(df_corr.columns, rotation=90)
    ax.set_yticklabels(df_corr.index)
    ax.set_title("Correlation Heatmap", pad=20)
    st.pyplot(fig)
