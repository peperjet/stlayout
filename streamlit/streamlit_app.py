import streamlit as st
import pandas as pd


st.title("streamlit_app 앱의 사용자 테마 정의하기")
st.write("이 앱의 `.streamlit/config.toml` 파일 내용")


number = st.number_input("숫자를 입력하세요", 0, 10, 5)
st.write(f"입력한 숫자는 {number}입니다.")


number = st.sidebar.slider('숫자를 선택하세요', 0, 10, 5)
st.write('슬라이더 위젯에서 선택된 숫자:', number)


st.title('st.secrets')
st.write(st.secrets['message'])


# 업로드
st.title('st.file_uploader')

st.subheader('CSV 파일 입력')
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('DataFrame')
    st.write(df)
    st.subheader('기술 통계')
    st.write(df.describe())
else:
    st.info('CSV 파일을 업로드해주세요.')

